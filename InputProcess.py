import speech_recognition as sr
from textblob import TextBlob

recognizer = sr.Recognizer()
mic = sr.Microphone()

#voice_input for video inputs
#translated_phrase for sentiment analysis

class Input(object):
    voice_input = ""

    #function that starts voice recognition and saves into voice_input variable
    def mic_loop():
    
        #sr.Microphone.list_microphone_names()

        with mic as source:
            print('say something')
            try:
                audio = recognizer.listen(source,10,3)
                voice_input = recognizer.recognize_google(audio, language="fil-PH")
                return voice_input
                #print(voice_input)
            except sr.UnknownValueError:
                voice_input = 'could not understand'
            except sr.RequestError as e:
                voice_input = "error: {0}".format(e)

    voice_input = mic_loop()
    print(voice_input)


    def translate_input(phrase): 
        print(TextBlob.detect_language(phrase))
        blob = TextBlob(phrase)
        translated_phrase = blob.translate(to='en')
        print(translated_phrase)
        return translated_phrase

    translated_phrase = translate_input(voice_input)








