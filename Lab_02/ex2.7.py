import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
import re
import requests
from bs4 import BeautifulSoup

# Extract the History section of the Artificial_intelligence" Wikipedia page
# Get Wikipedia page
url = "https://en.wikipedia.org/wiki/Bell_labs"
print("Loading the page content")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print("Parsing the page content")
# Find history section (starts after heading "History")
page = soup.find("div", {"id": "bodyContent"})

text_content = []

# Get all paragraphs
paragraphs = page.find_all("p")

# Extract text from each paragraph
for p in paragraphs:
    # Skip empty paragraphs and footnotes
    if p.text.strip() and not p.find_parent(class_="reference"):
        text_content.append(p.text)


# Join paragraphs and clean text
text = " ".join(text_content)
text = text.replace("\n", " ").replace("[edit]", "").strip()
# Remove citations [1], [2], etc.
text = (
    re.sub(r"\[\d+\]", "", text) + " The Bell Labs was located in New Jersey in 1970."
)

print("tokenizing, tagging and chunking")
sequences = [
    ne_chunk(pos_tag(word_tokenize(sentence + ". "))) for sentence in text.split(". ")
]

print("Start ectracting the relations")
rels = []
for sequence in sequences:
    new_relation = {"ORG": None, "isIn": False, "LOC": None}
    for chunk in sequence:
        if type(chunk) != tuple:
            if chunk.label() == "ORGANIZATION":
                new_relation["ORG"] = " ".join([leaf[0] for leaf in chunk])
            elif (
                (chunk.label() == "GPE" or chunk.label() == "LOCATION")
                and new_relation["ORG"] != None
                and new_relation["isIn"]
            ):
                new_relation["LOC"] = " ".join([leaf[0] for leaf in chunk])
                rels.append(new_relation)
                new_relation = {"ORG": None, "isIn": False, "LOC": None}

        elif new_relation["ORG"] is not None and chunk[1] == "IN" and chunk[0] == "in":
            new_relation["isIn"] = True
for rel in rels:
    print(f"[ORG: '{rel["ORG"]}'] 'in' [LOC: '{rel["LOC"]}'] ")

"""
Loading the page content
Parsing the page content
tokenizing, tagging and chunking
Start ectracting the relations
[ORG: 'Bell Telephone Laboratories'] 'in' [LOC: 'Western Electric'] 
[ORG: 'Volta Laboratory'] 'in' [LOC: 'Washington'] 
[ORG: 'Bell'] 'in' [LOC: 'Western Electric'] 
[ORG: 'Bell Laboratories'] 'in' [LOC: 'New Jersey'] 
[ORG: 'Bell Laboratories'] 'in' [LOC: 'New Jersey'] 
[ORG: 'Bell Lab'] 'in' [LOC: 'United States'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Physics'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Physics'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Physics'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Physics'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Physics'] 
[ORG: 'Bell Labs'] 'in' [LOC: 'Freehold'] 
[ORG: 'Bell Laboratories Fellow'] 'in' [LOC: 'United States'] 
[ORG: 'National Medal'] 'in' [LOC: 'Technology'] 
[ORG: 'Yokosuka Research Park'] 'in' [LOC: 'Yokosuka'] 
[ORG: 'Bell Labs Fellow Award'] 'in' [LOC: 'Network Architecture'] 
[ORG: 'Professional Services'] 'in' [LOC: 'Cable'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Physics'] 
[ORG: 'Bell Labs Fellow'] 'in' [LOC: 'North'] 
[ORG: 'Bell Labs'] 'in' [LOC: 'Information'] 
[ORG: 'Bell Labs'] 'in' [LOC: 'Tel Aviv'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Chemistry'] 
[ORG: 'Nobel Prize'] 'in' [LOC: 'Physics'] 
[ORG: 'Bell Labs'] 'in' [LOC: 'New Jersey'] 
[ORG: 'Bell Labs'] 'in' [LOC: 'New Jersey'] 
"""
