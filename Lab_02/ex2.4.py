import nltk
from nltk import book

np_grammar = "NP: {<DT>?<JJ>*<NN>+}"

np_parser = nltk.RegexpParser(np_grammar)

sentences = [
    nltk.pos_tag(sentence) for sentence in [book.sent2, book.sent3, book.sent7]
]
res = ""
for sentence in sentences:
    print(" ".join([token for token, tag in sentence]))
    result = np_parser.parse(sentence)
    print(result)
    result.pretty_print()
    result.draw()

"""
The family of Dashwood had long been settled in Sussex .
(S
  (NP The/DT family/NN)
  of/IN
  Dashwood/NNP
  had/VBD
  long/RB
  been/VBN
  settled/VBN
  in/IN
  Sussex/NNP
  ./.)
                                                 S                                               
   ______________________________________________|___________________________________             
  |        |          |       |       |          |        |       |       |          NP          
  |        |          |       |       |          |        |       |       |     _____|______      
of/IN Dashwood/NNP had/VBD long/RB been/VBN settled/VBN in/IN Sussex/NNP ./. The/DT     family/NN

2025-02-26 15:51:32.042 Python[6713:91178] +[IMKClient subclass]: chose IMKClient_Modern
2025-02-26 15:51:32.042 Python[6713:91178] +[IMKInputSession subclass]: chose IMKInputSession_Modern
In the beginning God created the heaven and the earth .
(S
  In/IN
  (NP the/DT beginning/NN)
  God/NNP
  created/VBD
  (NP the/DT heaven/NN)
  and/CC
  (NP the/DT earth/NN)
  ./.)
                                       S                                                             
   ____________________________________|__________________________________________________            
  |      |         |        |     |          NP                      NP                   NP         
  |      |         |        |     |     _____|_______           _____|______         _____|_____      
In/IN God/NNP created/VBD and/CC ./. the/DT     beginning/NN the/DT     heaven/NN the/DT     earth/NN

Pierre Vinken , 61 years old , will join the board as a nonexecutive director Nov. 29 .
(S
  Pierre/NNP
  Vinken/NNP
  ,/,
  61/CD
  years/NNS
  old/JJ
  ,/,
  will/MD
  join/VB
  (NP the/DT board/NN)
  as/IN
  (NP a/DT nonexecutive/JJ director/NN)
  Nov./NNP
  29/CD
  ./.)
                                                                S                                                                                 
     ___________________________________________________________|_____________________________________________________________                     
    |          |       |    |       |       |     |     |       |      |      |       |    |          NP                      NP                  
    |          |       |    |       |       |     |     |       |      |      |       |    |     _____|_____        __________|_____________       
Pierre/NNP Vinken/NNP ,/, 61/CD years/NNS old/JJ ,/, will/MD join/VB as/IN Nov./NNP 29/CD ./. the/DT     board/NN a/DT nonexecutive/JJ director/NN
"""
