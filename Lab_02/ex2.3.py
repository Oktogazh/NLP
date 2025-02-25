import re
import nltk


def extract_first_noun_phrase(sentence: str) -> str:
    # Tokenize the text into words
    tokens = nltk.word_tokenize(sentence)

    first_noun_phrase = []
    for token in nltk.pos_tag(tokens):
        if (
            len(first_noun_phrase) > 0
            and "NN" == first_noun_phrase[-1][1][:2]
            and (token[1][:2] != "NN" and token[1][:2] != "IN" and token[1][:2] != "PR")
        ):
            # end the loop if the first noun phrase has ended
            break
        elif re.match(r"^(DT|JJ|IN|NNS?|PR.*)$", token[1]):
            # extend the phrase as long as a POS tag is a valid part of a NP
            first_noun_phrase.append(token)

    return " ".join([word for word, tag in first_noun_phrase])


# testing the code with sample sentences
sample_sentences = [
    "Should all good men to come to the aid of their party?",
    "And now is the time for all good men to come to the aid of their party",
    "and for all good men to come to the aid of their party.",
    "Come to the aid of your party.",
    "Your party needs you.",
]

for sentence in sample_sentences:
    print(f"Sentence: {sentence}")
    print(f"First noun phrase: {extract_first_noun_phrase(sentence)}")
    print()

"""
Sentence: Should all good men to come to the aid of their party?
First noun phrase: all good men

Sentence: And now is the time for all good men to come to the aid of their party
First noun phrase: the time for all good men

Sentence: and for all good men to come to the aid of their party.
First noun phrase: for all good men

Sentence: Come to the aid of your party.
First noun phrase: the aid of your party

Sentence: Your party needs you.
First noun phrase: Your party needs you
"""
