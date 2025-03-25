# import libraries
import pandas as pd
import numpy as np
import nltk
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# need to download nltk corpus first (one time only)
#
# nltk.download('all')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load the amazon review dataset
# df = pd.read_csv ('https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv')
# Load a smaller sample of the amazon reviews instead
df = pd.read_csv("amazon.csv")

df = df.sample(frac=0.1, random_state=8)

print(df)


# create preprocess_text function
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())
    # Remove stop words
    filtered_tokens = [
        token for token in tokens if token not in stopwords.words("english")
    ]
    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    # Join the tokens back into a string
    processed_text = " ".join(lemmatized_tokens)
    return processed_text


# apply the function df
df["reviewText"] = df["reviewText"].apply(preprocess_text)

nltk.download("vader_lexicon")

# initialize NLTK sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# create get_sentiment function
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores["pos"] > 0 else 0
    return sentiment


print("spliting")
sets = np.split(
    df,
    [1000],
)

for set in sets:
    # apply get_sentiment function
    set["sentiment"] = set["reviewText"].apply(get_sentiment)
    print(set)

    print(confusion_matrix(set["Positive"], set["sentiment"]))

    print(classification_report(set["Positive"], set["sentiment"]))
