from flair.models import TextClassifier
from flair.data import Sentence

classifier = TextClassifier.load('en-sentiment')

def createSentence(msg):
    return Sentence(msg)

def predict_sentence_sentiment(msg):
    sentence = createSentence(msg)
    return classifier.predict(sentence)


