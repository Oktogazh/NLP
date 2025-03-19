# Comparing Spacy and NLTK
import spacy
import nltk
import json

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# Process whole documents
text = (
    "Megan Rapinoe criticized President Donald Trump's executive order banning transgender athletes from women's sports, labeling it \"cruel and depraved.\" "
    'Rapinoe urged other athletes to speak out, stating, "Players, actually, are always the most powerful people in sports." '
    "She highlighted recent events that disprove the claim that gender battles in women's sports do not exist."
    "She expressed concerns about the implications of a Trump presidency, suggesting that the order disregards the rights of transgender individuals in sports. "
    "When Sebastian Thrun started working on self-driving cars at "
    "Google in 2007, few people outside of the company took him "
    "seriously. “I can tell you very senior CEOs of major American "
    "car companies would shake my hand and turn away because I wasn't "
    "worth talking to,” said Thrun, in an interview with Recode earlier "
    "this week. "
    "The European Union has mandated that Apple improve compatibility of its iPhone and iPad operating systems with rival technologies, the first such enforcement under the Digital Markets Act. "
    "The EU Commission stated that Google has not adequately complied with the Digital Markets Act, favoring its own services in search results. "
    "Google fails to allow app developers to inform users about cheaper options outside its Google Play Store, according to preliminary findings by the Commission. "
)
doc = nlp(text)


def parse_noun_phrases(tagged_paragraph) -> list[str]:
    np_grammar = r"""
        NP: {<POS>?(<DT>?<PRP\$>?<\#>?<CC>?<RB>?<JJS?R?>*<VBG>*<NNP?S?|(CD)>+)+}
    """
    np_parser = nltk.RegexpParser(np_grammar)
    parsed = np_parser.parse(tagged_paragraph)
    nps = [part for part in parsed if not isinstance(part, tuple)]
    np_text = [" ".join([word for word, tag in part.leaves()]) for part in nps]
    return np_text


def find_verbs(tagged_paragraph) -> list[str]:
    verbs = [token for token, tag in tagged_paragraph if tag[0] == "V"]
    return verbs


def find_entities(tagged_paragraph) -> list[str]:
    ne_parsed = nltk.ne_chunk(tagged_paragraph)
    nes = [part for part in ne_parsed if not isinstance(part, tuple)]
    ne_text = [" ".join([word for word, tag in part.leaves()]) for part in nes]
    return ne_text


tokenized_paragraph = nltk.word_tokenize(text)
tagged_paragraph = nltk.pos_tag(tokenized_paragraph)

nltk_analysis = {
    "Noun phrases": parse_noun_phrases(tagged_paragraph),
    "Verbs": find_verbs(tagged_paragraph),
    "Entities": find_entities(tagged_paragraph),
}

# Analyze syntax
spacy_analysis = {
    "Noun phrases": [chunk.text for chunk in doc.noun_chunks],
    "Verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"],
    "Entities": [entity.text for entity in doc.ents],
}

differences = {}

for key in spacy_analysis.keys():
    not_in_spacy = [
        item for item in nltk_analysis[key] if item not in spacy_analysis[key]
    ]
    not_in_nltk = [
        item for item in spacy_analysis[key] if item not in nltk_analysis[key]
    ]
    differences[key] = {"Not in SpaCy": not_in_spacy, "Not in NLTK": not_in_nltk}


print(json.dumps(differences, indent=4, ensure_ascii=True))

"""
{
    "Noun phrases": {
        "Not in SpaCy": [
            "President Donald Trump",
            "'s executive order banning transgender athletes",
            "women",
            "'s sports",
            "Rapinoe",
            "powerful people",
            "women",
            "'s sports",
            "sports.When Sebastian Thrun",
            "2007",
            "\u201d",
            "this week.The European Union",
            "the Digital Markets Act.The EU Commission",
            "search results.Google"
        ],
        "Not in NLTK": [
            "President Donald Trump's executive order",
            "transgender athletes",
            "women's sports",
            "it",
            "\"Rapinoe",
            "the most powerful people",
            "\"She",
            "that",
            "women's sports",
            "She",
            "Sebastian Thrun",
            "him",
            "I",
            "you",
            "I",
            "The European Union",
            "The EU Commission",
            "search results"
        ]
    },
    "Verbs": {
        "Not in SpaCy": [
            "criticized",
            "banning",
            "labeling",
            "depraved",
            "urged",
            "stating",
            "are",
            "highlighted",
            "do",
            "exist.She",
            "expressed",
            "suggesting",
            "disregards",
            "started",
            "working",
            "took",
            "\u201c",
            "was",
            "talking",
            "said",
            "has",
            "mandated",
            "operating",
            "stated",
            "has",
            "complied",
            "favoring",
            "fails",
            "according"
        ],
        "Not in NLTK": [
            "criticize",
            "ban",
            "label",
            "urge",
            "state",
            "highlight",
            "exist",
            "express",
            "suggest",
            "disregard",
            "start",
            "work",
            "drive",
            "take",
            "talk",
            "say",
            "mandate",
            "state",
            "comply",
            "favor",
            "fail",
            "accord"
        ]
    },
    "Entities": {
        "Not in SpaCy": [
            "Megan",
            "Rapinoe",
            "Rapinoe",
            "CEOs",
            "European Union",
            "Digital Markets",
            "Digital Markets Act"
        ],
        "Not in NLTK": [
            "Megan Rapinoe",
            "Trump",
            "2007",
            "earlier this week",
            "The European Union",
            "first",
            "the Digital Markets Act",
            "The EU Commission",
            "Google Play Store"
        ]
    }
}
"""
