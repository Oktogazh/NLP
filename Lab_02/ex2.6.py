import nltk

sentences = """
Throughout history, never has the USA seen such an incompetent administration.
Throughout history, never has the USA seen such an incompetent Administration.
Throughout history, never has the USA seen such an Incompetent administration.
The 47th president Donald Duck's impredictability is only surpassed by his amateurism.
The only thing the king of D.C. is ruining faster than the American credibility is the American economy.
Since January, the stock exchange market seems to reach new low every hour.
Especially bad is the value of Musk's companies shares, with Tesla share trading at 281$ at 8 p.m. today.
The White house is in trouble, because the USA biggest hazard is already inside.
"""

cleaned_sentences = [
    nltk.pos_tag(nltk.word_tokenize(sentence))
    for sentence in sentences.strip().split("\n")
]

for sentence in cleaned_sentences:
    print(nltk.ne_chunk(sentence))

"""
(S
  Throughout/IN
  history/NN
  ,/,
  never/RB
  has/VBZ
  the/DT
  (ORGANIZATION USA/NNP)
  seen/VBN
  such/PDT
  an/DT
  incompetent/JJ
  administration/NN
  ./.)
(S
  Throughout/IN
  history/NN
  ,/,
  never/RB
  has/VBZ
  the/DT
  (ORGANIZATION USA/NNP)
  seen/VBN
  such/PDT
  an/DT
  incompetent/JJ
  (ORGANIZATION Administration/NN)
  ./.)
(S
  Throughout/IN
  history/NN
  ,/,
  never/RB
  has/VBZ
  the/DT
  (ORGANIZATION USA/NNP)
  seen/VBN
  such/PDT
  an/DT
  Incompetent/NNP
  administration/NN
  ./.)
(S
  The/DT
  47th/CD
  president/NN
  (PERSON Donald/NNP Duck/NNP)
  's/POS
  impredictability/NN
  is/VBZ
  only/RB
  surpassed/VBN
  by/IN
  his/PRP$
  amateurism/NN
  ./.)
(S
  The/DT
  only/JJ
  thing/NN
  the/DT
  king/NN
  of/IN
  (GPE D.C./NNP)
  is/VBZ
  ruining/VBG
  faster/RBR
  than/IN
  the/DT
  (GPE American/JJ)
  credibility/NN
  is/VBZ
  the/DT
  (GPE American/JJ)
  economy/NN
  ./.)
(S
  Since/IN
  January/NNP
  ,/,
  the/DT
  stock/NN
  exchange/NN
  market/NN
  seems/VBZ
  to/TO
  reach/VB
  new/JJ
  low/JJ
  every/DT
  hour/NN
  ./.)
(S
  Especially/RB
  bad/JJ
  is/VBZ
  the/DT
  value/NN
  of/IN
  (PERSON Musk/NNP)
  's/POS
  companies/NNS
  shares/NNS
  ,/,
  with/IN
  (PERSON Tesla/NNP)
  share/NN
  trading/NN
  at/IN
  281/CD
  $/$
  at/IN
  8/CD
  p.m./NN
  today/NN
  ./.)
(S
  The/DT
  (FACILITY White/NNP)
  house/NN
  is/VBZ
  in/IN
  trouble/NN
  ,/,
  because/IN
  the/DT
  (ORGANIZATION USA/NNP)
  biggest/JJS
  hazard/NN
  is/VBZ
  already/RB
  inside/RB
  ./.)
"""
