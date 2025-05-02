import re
import string

with open("Breton_text.txt", "r", encoding="utf-8-sig") as file1:
    breton = file1.read().replace("\n", " ")

with open("French_text.txt", "r", encoding="utf-8-sig") as file2:
    french = file2.read().replace("\n", " ")

# print length for each vairable
print("Breton text length:", len(breton))
print("French text length:", len(french))
# Breton text length: 391498
# French text length: 342861

# Split anywhere a punctuation followed by a space and a capital letter
breton_segments = re.split(r"(?<=[.!?\"\'])\s+(?=[A-Z])", breton)
french_segments = re.split(r"(?<=[.!?\"\'])\s+(?=[A-Z])", french)

print("Breton segments count:", len(breton_segments))
print("French segments count:", len(french_segments))
# Breton segments count: 4737
# French segments count: 3814

print("Breton segments example:", breton_segments[:3])
print("French segments example:", french_segments[:3])
# Breton segments example: ['Paol, emañ ho koan war an daol.', 'Deuit da zebriñ ho koan !"', 'Kleier Karmez o doa sonet an anjeluz.']
# French segments example: ['- Paol, votre dîner est sur la table.', "Les cloches des Carmes avaient sonné l'angélus.", "La paix du soir s'épandait sur la ville."]


# Reuse the function from the last lab
def clean_text(text):
    # Cleans the given text using regular expressions to split and lower-cased versions to create
    # a list of tokens for each text.

    # lower case
    tokens = re.split(r"[\s\n.–]+", text.replace("—", " ").replace("c'h", "cvvh"))
    tokens = [t.lower() for t in tokens]

    # remove punctuation using regular expressions
    # this line of code locates the punctuation within the given text and compiles that punctuation into a single variable
    re_punc = re.compile("[%s]" % re.escape(string.punctuation))
    # this line of code substitutes the punctuation we just compiled with nothing ''
    tokens = [re_punc.sub("", token) for token in tokens]

    # only include tokens that aren't numbers
    tokens = [token.replace("cvvh", "c'h") for token in tokens if token]
    return tokens


clean_breton_segments = []
for x in breton_segments:
    clean_breton_segments.append(clean_text(x))

clean_french_segments = []
for x in french_segments:
    clean_french_segments.append(clean_text(x))

print(clean_breton_segments[:3])
print(clean_french_segments[:3])
# [['paol', 'emañ', 'ho', 'koan', 'war', 'an', 'daol'], ['deuit', 'da', 'zebriñ', 'ho', 'koan'], ['kleier', 'karmez', 'o', 'doa', 'sonet', 'an', 'anjeluz']]
# [['paol', 'votre', 'dîner', 'est', 'sur', 'la', 'table'], ['les', 'cloches', 'des', 'carmes', 'avaient', 'sonné', 'langélus'], ['la', 'paix', 'du', 'soir', 'sépandait', 'sur', 'la', 'ville']]
