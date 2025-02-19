import re

""" 
Started with the following to load the book corpus
in the module's data directory (only once)

nltk.download()
nltk.download('punkt_tab')
"""
from nltk import book as books

"""
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
"""

# print(books.text1.name)  # Moby Dick by Herman Melville 1851
# print(books.sent6)

books.text3.concordance("thou")
""" 
Displaying 25 of 284 matches:
saying , Of every tree of the garden thou mayest freely e But of the tree of t
 of the knowledge of good and evil , thou shalt not eat of for in the day that
shalt not eat of for in the day that thou eatest thereof thou shalt surely die
 in the day that thou eatest thereof thou shalt surely die . And the LORD God 
Adam , and said unto him , Where art thou ? And he said , I heard thy voice in
f . And he said , Who told thee that thou wast naked ? Hast thou eaten of the 
old thee that thou wast naked ? Hast thou eaten of the tree , whereof I comman
tree , whereof I commanded thee that thou shouldest not eat ? And the man said
 ? And the man said , The woman whom thou gavest to be with me , she gave me o
d unto the woman , What is this that thou hast done ? And the woman said , The
 God said unto the serpent , Because thou hast done this , thou art cursed abo
pent , Because thou hast done this , thou art cursed above all cattle , and ab
 of the field ; upon thy belly shalt thou go , and dust shalt thou eat all the
belly shalt thou go , and dust shalt thou eat all the days of thy li And I wil
eed ; it shall bruise thy head , and thou shalt bruise his heel . Unto the wom
orrow and thy conception ; in sorrow thou shalt bring forth children ; and thy
ee . And unto Adam he said , Because thou hast hearkened unto the voice of thy
of which I commanded thee , saying , Thou shalt not eat of cursed is the groun
round for thy sake ; in sorrow shalt thou eat of it all the days of thy life ;
s shall it bring forth to thee ; and thou shalt eat the herb of the field ; In
eld ; In the sweat of thy face shalt thou eat bread , till thou return unto th
thy face shalt thou eat bread , till thou return unto the ground ; for out of 
unto the ground ; for out of it wast thou tak for dust thou art , and unto dus
for out of it wast thou tak for dust thou art , and unto dust shalt thou retur
 dust thou art , and unto dust shalt thou return . And Adam called his wife ' """

print(books.text6.generate())
""" 
SOLDIER # 1 : Until you come and get a bit . # 2 : Hic ! ARTHUR : How
can we come up and have a plan , sir . roar ] MAYNARD : Armaments ,
Chapter Two , verses Nine to Twenty - one . Heh . DINGO : Yes , yes ,
you ain ' t . , great . Ni ! who , when he seemed about to recover ,
suddenly felt the icy hand of death upon him . No SCENE 19 : ARTHUR :
Walk away . squeak ] [ howl ] [ creak
SOLDIER # 1 : Until you come and get a bit . # 2 : Hic ! ARTHUR : How
can we come up and have a plan , sir . roar ] MAYNARD : Armaments ,
Chapter Two , verses Nine to Twenty - one . Heh . DINGO : Yes , yes ,
you ain ' t . , great . Ni ! who , when he seemed about to recover ,
suddenly felt the icy hand of death upon him . No SCENE 19 : ARTHUR :
Walk away . squeak ] [ howl ] [ creak
"""


# example of methods coming with a text
""" 
book.text4.collocation_list(  book.text4.concordance_list(  book.text4.generate(          book.text4.readability(                                     
book.text4.collocations(      book.text4.count(             book.text4.index(             book.text4.similar(                                         
book.text4.common_contexts(   book.text4.dispersion_plot(   book.text4.name               book.text4.tokens                                           
book.text4.concordance(       book.text4.findall(           book.text4.plot(              book.text4.vocab()                                          
>>> book.text4.
 """


# Finding the first 100 words of 'Monty Python and the Holy Grail'
# Of course, the count depends on what we define as a word
types = set()
for word in books.text6:
    if len(types) == 100:
        break
    # Include in the set if it contains a letter
    types |= {re.sub(r"^[^a-zA-Z]+$", "", word) or None}


print("Analyse of the Monty Python and the Holy Grail:")
print(
    f"""First 100 tokens: {books.text6[:100]}
First 100 wordtypes: {types}
"""
)

"""
Analyse of the Monty Python and the Holy Grail:

First 100 tokens: ['SCENE', '1', ':', '[', 'wind', ']', '[', 'clop', 'clop', 'clop', ']', 'KING', 'ARTHUR', ':', 'Whoa', 'there', '!', '[', 'clop', 'clop', 'clop', ']', 'SOLDIER', '#', '1', ':', 'Halt', '!', 'Who', 'goes', 'there', '?', 'ARTHUR', ':', 'It', 'is', 'I', ',', 'Arthur', ',', 'son', 'of', 'Uther', 'Pendragon', ',', 'from', 'the', 'castle', 'of', 'Camelot', '.', 'King', 'of', 'the', 'Britons', ',', 'defeator', 'of', 'the', 'Saxons', ',', 'sovereign', 'of', 'all', 'England', '!', 'SOLDIER', '#', '1', ':', 'Pull', 'the', 'other', 'one', '!', 'ARTHUR', ':', 'I', 'am', ',', '...', 'and', 'this', 'is', 'my', 'trusty', 'servant', 'Patsy', '.', 'We', 'have', 'ridden', 'the', 'length', 'and', 'breadth', 'of', 'the', 'land', 'in']
First 100 types: First 100 types (including punctuation): {'is', 'England', 'a', 'Ridden', 've', 'join', 'snows', 'goes', 'winter', 'Whoa', 'tropical', 'Found', None, 'am', 'Where', 'son', 'We', 'will', 'found', 'King', 'Arthur', 'SCENE', 'knights', 'Camelot', 'me', 'at', 'lord', 'and', 'em', 'using', 'together', 'SOLDIER', 'two', 'coconut', 'halves', 'must', 'coconuts', 'kingdom', 'speak', 's', 'Yes', 'Mercea', 'It', 'defeator', 'court', 'got', 'land', 'clop', 'other', 'covered', 'them', 'I', 'breadth', 'from', 'You', 'empty', 'since', 'horse', 'there', 'ARTHUR', 're', 'In', 'Uther', 'servant', 'Pendragon', 'castle', 'sovereign', 'wind', 'What', 'all', 'you', 'through', 'Pull', 'one', 'in', 'Saxons', 'bangin', 'my', 'this', 'So', 'Halt', 'your', 'The', 'KING', 'd', 'have', 'master', 'ridden', 'Patsy', 'with', 'who', 'Who', 'the', 'length', 'search', 'Britons', 'get', 'on', 'trusty', 'of'}
"""
