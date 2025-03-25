# import libraries
import pandas as pd
import nltk

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
print(df)

nltk.download("vader_lexicon")

# initialize NLTK sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# create get_sentiment function
def get_sentiment(text):
    scores = analyzer.polarity_scores(text)
    sentiment = 1 if scores["pos"] > 0 else 0
    return sentiment


# apply get_sentiment function
df["sentiment"] = df["reviewText"].apply(get_sentiment)
print(df)

from sklearn.metrics import confusion_matrix

# Thus in binary classification, the count of true negatives is C_{0,0}, false negatives is C_{1,0}, true positives is C_{1,1} and false positives is C_{0,1}.
print(confusion_matrix(df["Positive"], df["sentiment"]))

from sklearn.metrics import classification_report

print(classification_report(df["Positive"], df["sentiment"]))
