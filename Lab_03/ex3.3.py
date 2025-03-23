import re
import json


def detect_language(texts: list[str]) -> list[str]:
    frequent_types = {
        "cy": ["yn", "yr", "yng", "i", "a", "yw", "'n", "'r", "mae", "o"],
        "en": ["the", "a", "and", "of", "be", "that", "is", "it", "for", "not", "in"],
        "br": ["an", "ar", "eo", "e", "o", "a", "ez", "ha", "da", "en"],
        "fr": ["le", "la", "de", "ne", "n'", "et", "un", "pas", "se", "les", "et"],
    }
    result = []
    for text in texts:
        counter = {}
        most_likely_language = {"name": "", "value": 0}
        for key, list in frequent_types.items():
            counter[key] = 0
            for type in list:
                counter[key] += len(re.findall(rf"{type}\b", text.lower()))
            if most_likely_language["value"] < counter[key]:
                most_likely_language = {"name": key, "value": counter[key]}
        result.append(most_likely_language["name"])
    return result


with open("../Tech Iaith/corpus_content.json") as f:
    # If your JSON has a 'text' field
    parallel_corpus = json.load(f)

fr_sentences = [sent["fr"] for sent in parallel_corpus]
br_sentences = [sent["br"] for sent in parallel_corpus]
corpus_size = len(fr_sentences)
print(
    "Accuracy in detecting French sentences:",
    f'{100
    * len([val for val in detect_language(fr_sentences) if val == "fr"])
    // corpus_size}%',
)
print(
    "Accuracy in detecting Breton sentences:",
    f'{100
    * len([val for val in detect_language(br_sentences) if val == "br"])
    // corpus_size}%',
)

# output
# Accuracy in detecting French sentences: 25%
# Accuracy in detecting Breton sentences: 97%
