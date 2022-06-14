##########################################################################################################################
#functions
#cleanText function processes user input and returns the input that will be used for sentiment analysis
#processText function should accept the original user input and turns it into an array to be used for video processing 
#


##########################################################################################################################
import nltk.corpus
nltk.download('stopwords')


from nltk.corpus import stopwords
import re
import shlex

def cleanText(user_input):
    #user_input_raw = "Hey Amazon - my package never arrived https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first PLEASE FIX ASAP! @"
    #print(user_input_raw)
    user_input_raw = user_input
    user_input = user_input_raw.lower()
    #print(user_input)
    user_input = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", user_input)
    #print(user_input)

    stop = stopwords.words('english')

    user_input = " ".join([word for word in user_input.split() if word not in (stop)])



    return user_input


def processText(user_input):
    phrase_database = ["hey",
    "hi",
    "hello",
    "magandang umaga",
    "ano ang pangalan mo",
    "kumusta ka",
    "okay",
    "mabuti", 
    "oo",
    "opo",
    "hindi",
    "bingi ka ba",
    "salamat",
    "i love you",
    "malungkot ako"
    ]

    user_input = user_input.lower()
    user_input = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", user_input)

    found_phrases = []
    unfound_phrases = []


    
    def words_in_string(phrase_database, user_input):
        '''return iterator of words in string as they are found'''
        word_set = set(phrase_database)
        pattern = r'\b({0})\b'.format('|'.join(phrase_database))
        for found_word in re.finditer(pattern, user_input):
            word = found_word.group(0)
            if word in word_set:
                word_set.discard(word)
                yield word
                if not word_set: # then we've found all words
                    # break out of generator, closing file
                    raise StopIteration 

    for word in words_in_string(phrase_database, user_input):
        found_phrases.append(word)

    for word in found_phrases:
        user_input = user_input.replace(word, '\"'+word+'\"')

    #print(user_input)


    
    user_input = shlex.split(user_input)

    final_input =[]

    for word in user_input:
        if word in found_phrases:
            final_input.append(word)
        else:
            for letter in word:
                final_input.append(letter)
    
    mp4_input = []
    current_element = ''
    for word in final_input:
 
        mp4_input.append(word+'.mp4')
    return mp4_input
    

#print(cleanText("Hey Amazon - my package never arrived https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first PLEASE FIX ASAP! @"))
#print(processText("Good morning!@ Hola my name is mc! hello!"))