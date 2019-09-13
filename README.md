# MarkovText

Generate sentences using a Markovian process, parameterized via an input text file.

## Example

Using Herman Melville's [Moby Dick](https://www.gutenberg.org/ebooks/2701) and a state defined by (the previous) two tokens in the sequence:

```
MarkovText me$ time python3 markov.py Texts/Melville.txt 2

17276 unique tokens.
9619 viable sentences; min. length 3, max. 446, mean 25.5, median 19.0, stdev 23.0
103783 transitions.
5286 start tuples.
3 end tokens.

Seed: "whence he" (max_attempts = 100000):

1   "Whence he came directly from the bottomless profundities the gigantic tail tendon."

2   "Whence he came to look about him, jonah throws himself into furious speed, almost incoherently."

3 * "Whence he derived that picture, and, then, the _black fish_."

4   "Whence he came forth from the original prestige of perilousness about such a spectralness over the craft with his prodigious bulk and power; how orion glitters; what a multitude, that most of them were against it; but no more, but for one swift moment seen hovering over it for an indian, to whom the question was put to further discoveries, by some whales have christenings?"

5   "Whence he came directly from the captains cabin."

6   "Whence he came in as calm, but with a grating rush, the daughter of a healthy old age, and replenishes them there for a huge drooping stalk, was horrified at the bottom of the deepest."

7   "Whence he came to know whether to buy him a prometheus; a french grenadiers, who seeking honey in the eye of the seamen resumed their work upon his ivory heel."

8 * "Whence he derived that picture to any sympathy from the white whale is often chased."

9   "Whence he came directly from the ground with their trowsers rolled high up on their mouths; the same time also helped to the gradual prolongings of the watch standing, lounging, leaning over to a strange inn, under the windlass_."

10   "Whence he came in a dark locker of the body of the peace."


real	0m1.136s
user	0m1.088s
sys	0m0.043s

```

Using the same text and a state defined by three tokens:

```
MarkovText me$ time python3 markov.py Texts/Melville.txt 3

17109 unique tokens.
9024 viable sentences; min. length 4, max. 446, mean 27.0, median 21.0, stdev 23.0
178449 transitions.
7760 start tuples.
3 end tokens.

Seed: "at first i" (max_attempts = 100000):

1 * "At first i almost thought he would sink the ship?"

2   "At first i knew not how this consciousness at last glided away from me; nor do i now drop these links."

3 * "At first i saw nobody; but i make a bandbox for queequeg, and he supposed, no doubt, and its commander from all accounts, a very dark and dismal night, bitingly cold and cheerless."

4   "At first i knew not what, i rolled away from it; but, maybe, tis well."

5   "At first i knew not what, i rolled away from my heart."

6   "At first i knew not what, i rolled away from the breast, as if sucked into a morass, moby dick rose again, and seeing how they spent their wages in _that_ place also, poor queequeg gave it up for lost."

7 * "At first i saw nobody; but i could not at all affecting the matter presently to be mentioned."

8 * "At first i saw nobody; but i have swam through libraries and sailed through oceans; i have had to do with aught that looks like it, sir."

9 * "At first i saw nobody; but i never heard what sort of unaccountable tie he soon evinced himself to be linked with ahabs peculiar fortunes; nay, to night, cause to morrows sunday, and it heads some other way."

10   "At first i almost thought that this black manikin was a real baby preserved in some similar manner."


real	0m1.225s
user	0m1.165s
sys	0m0.056s

```

Four tokens:

```
MarkovText me$ time python3 markov.py Texts/Melville.txt 4

17057 unique tokens.
8614 viable sentences; min. length 5, max. 446, mean 28.0, median 22.0, stdev 23.0
199195 transitions.
8287 start tuples.
3 end tokens.

Seed: "but look ye ," (max_attempts = 100000):

1   "But look ye, the only real owner of anything is its commander; and hark ye, my conscience is in this ships keel."

2 * "But look ye, starbuck, what is said in heat, that thing unsays itself."

3 * "But look ye, heres a crappo that is content with our leavings, the drugged whale there, wouldnt be fit to burn in a jail; no, not in a condemned cell."

4   "But look ye, heres a crappo that is content with our leavings, the drugged whale there, i mean quohog, in one of the mighty triumphs given to a roman general upon his entering the worlds capital, the bones of which almost exactly answer to the bones of the leviathan in their gigantic, full grown development, for that rare knowledge i am indebted to my late royal friend tranquo, king of tranque, one of the peculiar characteristics of the savage in his domestic hours, is his wonderful patience of industry."

5   "But look ye, heres a crappo that is content with our leavings, the drugged whale there, i mean; aye, and is content too with scraping the dry bones of that other precious fish he has there."

6   "But look ye, heres a crappo that is content with our leavings, the drugged whale there, i mean; aye, and signed a bond with him, that all the anguish of that then present suffering was but the direct issue of a former woe; and he too plainly seemed to see, that as the most poisonous reptile of the marsh perpetuates his kind as inevitably as the sweetest songster of the grove; so, equally with every felicity, all miserable events do naturally beget their like."

7 * "But look ye, heres a crappo that is content with our leavings, the drugged whale there, i mean quohog, in one of our boats."

8   "But look ye, heres a crappo that is content with our leavings, the drugged whale there, i mean quohog, in one of the mighty triumphs given to a roman general upon his entering the worlds capital, the bones of which almost exactly answer to the bones of the leviathan in their gigantic, full grown development, for that rare knowledge i am indebted to my late royal friend tranquo, king of tranque, one of the cordon, whose post was near the after hatches, whispered to his neighbor, a cholo, the words above."

9   "But look ye, heres a crappo that is content with our leavings, the drugged whale there, i mean quohog, in one of the intervals of profound darkness, following the flashes, a voice was heard at his side; and almost at the same instant a volley of thunder peals rolled overhead."

10   "But look ye, heres a crappo that is content with our leavings, the drugged whale there, i mean; aye, and not changed a wink since i first saw it, a boy, from the sand hills of nantucket!"


real	0m1.189s
user	0m1.125s
sys	0m0.059s
```

## Notes:

The larger the number of tokens used for the state definition, the less likely you are to see "new" text generated. Anything over about four tokens is unlikely to produce interesting results. Likewise, a state definition using a single token probably won't capture the feel of the original text particularly well.
