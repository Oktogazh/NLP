import json
import spacy
from spacy import displacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


with open("./corpus_content.json") as f:
    # If your JSON has a 'text' field
    parallel_corpus = json.load(f)

fr_core = spacy.load("fr_core_news_sm")
xx_ent = spacy.load("xx_ent_wiki_sm")

fr_sentences = " ".join([sent["fr"] for sent in parallel_corpus])
br_sentences = " ".join([sent["br"] for sent in parallel_corpus])

fr = fr_core(fr_sentences)


s = [sent for sent in fr.sents][2:3]
""" displacy.serve(
    s,
    style="dep",
    auto_select_port=True,
)
 """
print("Sentence analisys:")
for t in list(fr.sents)[2]:
    print(t.text, t.pos_, t.is_stop)

print()
print("50 most common alphabetic tokens:")
token_counter = Counter()
for token in fr:
    if token.is_stop is False and token.is_alpha:
        token_counter[token.lemma_] += 1


br_token_counter = Counter()
for token in (
    br_sentences.replace(".", "").replace(",", "").replace(";", " ").split(" ")
):
    if (
        (len(token) > 4 or token == "enez" or token == "Doue")
        and token[-4:] != "zhañ"
        and token[-4:] != "ezho"
        and token != "gantañ"
        and token != "outañ"
        and token != "ennañ"
        and token != "emezañ"
        and token[0] != "v"
        and token[0] != "z"
        and token[0] != "w"
        and token[0:2] != "e-"
        and token[0:2] != "a-"
        and token[0:3] != "er-"
        and token[0:4] != "war-"
    ):
        token = token if token[1:] != "leet" else "dleout"
        token = token if token != "gaout" else "kaout"
        token = token if token[-3:] != "aet" else token[:-3] + "aat"
        token = token if token != "gristen" else "kristen"
        token = token if token != "Goude" else "goude"
        token = token if token != "barrez" else "parrez"
        token = token if token != "ouelañ" else "gouelañ"
        token = token if token != "maouezed" else "maouez"
        token = token if token != "c'helle" and token != "gellet" else "gallout"
        br_token_counter[token] += 1

print("In the French examples:")
print(token_counter.most_common(50))
print()
print("In the Breton examples:")
print(br_token_counter.most_common(50))

# Create the word cloud object
wordcloud = WordCloud(
    width=800, height=400, background_color="white", min_font_size=10
).generate(" ".join([token for (token, count) in br_token_counter.most_common(50)]))

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")  # Remove the axis
plt.tight_layout(pad=0)
plt.show()

# You can also save the image to a file
wordcloud.to_file("wordcloud.png")
