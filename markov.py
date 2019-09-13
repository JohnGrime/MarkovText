import sys, io, random, statistics

#
# Generate a discrete distribution from which we can sample.
# Optimisations via e.g. bisection search in Sample(), but
# should be fast enough for our purposes.
#

class DiscrDistr:

	def __init__(self):
		self.m, self.cdf = {}, None

	def Increment(self, key, counts=1):
		self.m[key] = self.m.setdefault(key,0)+counts

	def PrepareForSampling(self):
		total, acc = sum([count for (_,count) in self.m.items()]), 0.0

		# sort cdf entries so we hit the largest contributions first.
		self.cdf = sorted( self.m.items(), key=lambda x: x[1], reverse=True)
		
		for i,(k,n) in enumerate(self.cdf):
			acc += float(n)/total
			self.cdf[i] = (k,acc)

	def Sample(self,r):
		if self.cdf == None:
			self.PrepareForSampling()
		
		for k,v in self.cdf:
			if v >= r: return k
		
		# If we get here, possible numerical problems? If so, should only
		# undersample the LEAST important entity (as cdf sorted descending)
		return None


#
# Markov generator for token sequences.
#

class Markov:

	def __init__(self):
		self.transitions = {}

	def AddTransition(self, state, next_token):
		self.transitions.setdefault(state,[]).append(next_token)

	def CountTransitions(self, state):
		return len(self.transitions[state])

	def GetNextToken(self, state):
		return random.choice(self.transitions[state])


#
# As above, using DiscrDist for reduced memory (but may be slower).
# Don't call GetNextToken() until you've added all your data!
#

class MarkovDD:

	def __init__(self):
		self.transitions = {}

	def AddTransition(self, state, next_token):
		self.transitions.setdefault(state,DiscrDistr()).Increment(next_token)

	def CountTransitions(self, state):
		return len(self.transitions[state].m)

	def GetNextToken(self, state):
		return self.transitions[state].Sample(random.random())


#
# Print some usage information
#

def print_usage(prog):
	print()
	print(f'Usage: {prog} input.txt tuple_len [min_sentence]')
	print()
	print('Where:')
	print()
	print(' - input.txt : plain text source (assumes utf-8 encoding)')
	print(' - tuple_length : number of sequential tokens defining Markov state')
	print(' - min_sentence : OPTIONAL min. sentence length to consider (default: key_tuple_length+1)')
	print()
	sys.exit(-1)


#
# Main code starts here!
#

seq_lens = []          # list of all token sequence lengths from input (unlikely to use excessive memory)
unique_toks = {}       # count of all unique token occurrences
starts = {}            # all start tuples found in input text sequences
ends = {}              # all end tokens found in input text sequences
use_counts = True      # use DiscrDistr class in Markov generator?
max_attempts = 100_000 # max. attempts to create a new sentence before stopping

markov = MarkovDD() if use_counts else Markov()

#
# Read command line params, input data
#

args = sys.argv

if len(args)<2:
	print_usage(args[0])

path = args[1]
state_tuple_len = int(args[2])

min_sentence_len = state_tuple_len+1
if len(args)>3:
	min_sentence_len = max(min_sentence_len, int(args[3]))

with io.open(path, encoding='utf-8') as f:
	raw_txt = f.read().lower()

#
# Basic preparation of input text; remove some junk, and ensure
# that certain types of punctuation are treated as separate tokens.
#

split_marker = "|"

replace = {
	# "Expand" sentence-ending punctuation to treat as distinct tokens
	'.' : ' .'+split_marker,
	'!' : ' !'+split_marker,
	'?' : ' ?'+split_marker,

	# "Expand" other misc. punctuation to treat as distinct tokens
	',' : ' , ',
	':' : ' : ',
	';' : ' ; ',

	# Swap these for a space character
	'\n' : ' ',
	'-'  : ' ',

	# Remove these entirely
	'"'  : '',
	'\'' : '',
	'('  : '',
	')'  : '',
}

txt = raw_txt

for old in replace:
	new = replace[old]
	txt = txt.replace(old,new)

#
# Break input text into sentences, tokenise, and generate state transitions
#

for sentence in txt.split(split_marker):
	toks = sentence.split()
	n_toks = len(toks)

	if n_toks < min_sentence_len: continue

	for tok in toks:
		unique_toks[tok] = unique_toks.setdefault(tok,0)+1

	seq_lens.append(n_toks)

	for i in range(0, n_toks-(state_tuple_len) ):
		j = i+state_tuple_len
		state, next_token = tuple(toks[i:j]), toks[j]

		if i == 0:
			starts[state] = 1

		if j == n_toks-1:
			ends[next_token] = 1

		markov.AddTransition(state, next_token)

# We'll seed the generation using random known-good start states with at least 2 potential transitions.
good_start_states = [ s for s in list(starts.keys()) if markov.CountTransitions(s)>1 ]

#
# Print some information for the user
#

utf8 = lambda x: x.encode('utf-8')
stuff = [(t,unique_toks[t]) for t in unique_toks]
stuff = sorted(stuff, key=lambda x: x[1], reverse=True)

print()

print(f'{len(stuff)} unique tokens.')
#for s in stuff: print( ' %10s {s[1]}' % (utf8(s[0])) )

print('%d viable sentences; min. length %.0f, max. %.0f, mean %.1f, median %.1f, stdev %.1f'%(
	len(seq_lens),
	min(seq_lens),
	max(seq_lens),
	statistics.mean(seq_lens),
	statistics.median(seq_lens),
	statistics.stdev(seq_lens)
	))

print(f'{len(markov.transitions)} transitions.')
print(f'{len(starts)} start tuples, {len(good_start_states)} good for seeding.')
print(f'{len(ends)} end tokens.')

print()

#
# Generate some sentences using Markov process
# TODO: examine potential paths through graph, bias towards paths with greatest combinatorial variation?
# Straightforward to implement via modified Dijkstra's algorithm.
#

if len(good_start_states)<1:
	print('No start states suitable to seed generation!')
	sys.exit(-1)

seed_state = random.choice(good_start_states)

print(f'Seed: "{" ".join(seed_state)}" (max_attempts = {max_attempts}):')
print()

# Attempt to generate multiple unqiue sentences from the same seed.
previous, n_attempts = {}, 0
while (len(previous)<10) and (n_attempts<max_attempts):
	n_attempts += 1
	state = seed_state

	# Sample sequence length appropriate to sentences from input text
	L = random.choice(seq_lens)

	# Build out sentence
	sequence = list(state)

	while True:
		# No valid transition from this state.
		if state not in markov.transitions: break

		next_tok = markov.GetNextToken(state)

		sequence.append(next_tok)
		state = ( *state[1:], next_tok )

		# Sentence is "long enough", and terminates with a known end token.
		if (len(sequence)>L) and (next_tok in ends): break

	# Did we end unexpectedly? Tag output so the user knows.
	tag = (len(sequence)<L) or (next_tok not in ends)
	
	# Convert token list to a string, and ensure we're not repeating ourselves
	sentence = ' '.join(sequence)
	if sentence in previous: continue
	else: previous[sentence] = True

	# Make output look a little nicer
	for x in replace: sentence = sentence.replace(' '+x,x)
	sentence = sentence[0].upper() + sentence[1:]
	
	print(f'{len(previous)} {"*" if tag else " "} "{sentence}"')
	print()
