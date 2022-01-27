from textblob import TextBlob


#translated_phrase for sentiment analysis

class Input(object):
    
    #substitute post data
    user_input=''
    #Code for translating filipino input to english input
    def translate_input(phrase): 
        print(TextBlob.detect_language(phrase))
        blob = TextBlob(phrase)
        translated_phrase = blob.translate(to='en')
        print(translated_phrase)
        return translated_phrase
    #translate filipino to english to be used for rnn
    translated_phrase = translate_input(user_input)
    








