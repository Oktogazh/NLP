# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
import nltk
import json

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = (
    "When Sebastian Thrun started working on self-driving cars at "
    "Google in 2007, few people outside of the company took him "
    "seriously. “I can tell you very senior CEOs of major American "
    "car companies would shake my hand and turn away because I wasn’t "
    "worth talking to,” said Thrun, in an interview with Recode earlier "
    "this week."
)
doc = nlp(text)


def parse_noun_phrases(text: str) -> list[str]:
    tokenized_paragraph = nltk.word_tokenize(text)
    tagged_paragraph = nltk.pos_tag(tokenized_paragraph)
    np_grammar = r"""
        NP: {<POS>?(<DT>?<PRP\$>?<\#>?<CC>?<JJS?R?>*<VBG>*<NNP?S?|(CD)>+)+}
    """
    np_parser = nltk.RegexpParser(np_grammar)
    parsed = np_parser.parse(tagged_paragraph)
    nps = [part for part in parsed if not isinstance(part, tuple)]
    np_text = [" ".join([word for word, tag in part.leaves()]) for part in nps]
    print([chunk.text for chunk in doc.noun_chunks])
    return np_text


# Analyze syntax
spacy_analysis = {
    "Noun phrases": [chunk.text for chunk in doc.noun_chunks],
    "Verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"],
    "Entities": [", ".join((entity.text, entity.label_)) for entity in doc.ents],
}

nltk_analysis = {
    "Noun phrases": parse_noun_phrases(text),
    "Verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"],
    "Entities": [", ".join((entity.text, entity.label_)) for entity in doc.ents],
}

print(json.dumps(nltk_analysis, indent=4))
