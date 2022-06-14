import translators as ts
from textblob import TextBlob

def translate(user_input):
    
    translated = ts.google(user_input)
    #print(translated)

    blob = TextBlob(translated)
    
    return blob.sentiment.polarity
