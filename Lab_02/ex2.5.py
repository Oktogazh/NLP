import nltk

np_grammar = r"""
    NP: {<POS>?(<DT>?<PRP\$>?<\#>?<CC>?<JJS?R?>*<VBG>*<NNP?S?|(CD)>+)+}
"""

np_parser = nltk.RegexpParser(np_grammar)

phrases = """another/DT sharp/JJ dive/NN
trade/NN figures/NNS
any/DT new/JJ policy/NN measures/NNS
earlier/JJR stages/NNS
Panamanian/JJ dictator/NN Manuel/NNP Noriega/NNP
his/PRP$ Mansion/NNP House/NNP speech/NN
the/DT price/NN cutting/VBG
3/CD %/NN to/TO 4/CD %/NN
more/JJR than/IN 10/CD %/NN
the/DT fastest/JJS developing/VBG trends/NNS
's/POS skill/NN""".split(
    "\n"
)
# First, we prepare the samples in order to process them with nltk
phrases = [[tuple(word.split("/")) for word in phrase.split(" ")] for phrase in phrases]
# using the chunkparser to reach an F-score of 75%
# Precision: 81% and Recall 70%
# nltk.app.chunkparser()

for phrase in phrases:
    parsed = np_parser.parse(phrase)
    print(parsed)

"""
(S (NP another/DT sharp/JJ dive/NN))
(S (NP trade/NN figures/NNS))
(S (NP any/DT new/JJ policy/NN measures/NNS))
(S (NP earlier/JJR stages/NNS))
(S (NP Panamanian/JJ dictator/NN Manuel/NNP Noriega/NNP))
(S (NP his/PRP$ Mansion/NNP House/NNP speech/NN))
(S (NP the/DT price/NN) cutting/VBG)
(S (NP 3/CD %/NN) to/TO (NP 4/CD %/NN))
(S more/JJR than/IN (NP 10/CD %/NN))
(S (NP the/DT fastest/JJS developing/VBG trends/NNS))
(S (NP 's/POS skill/NN))
"""
