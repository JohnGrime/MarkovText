# MarkovText

Generate sentences via a Markovian process, parameterized using an input text source.

## Example

Using Herman Melville's [Moby Dick](https://www.gutenberg.org/ebooks/2701) and a state defined by the last four tokens:

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
