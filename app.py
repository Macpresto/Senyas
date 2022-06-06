from flask import Flask, redirect, url_for, render_template, request
import time
from movie import processVideo
from clean import cleanText, processText
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route("/home", methods=["POST", "GET"])


def home():

    user_input = ''
    if request.method == "POST":
        user_input = request.form["hidden"]
        #print(user_input)
        sentimentText = cleanText(user_input)
        #print(sentimentText)
        videoText = processText(user_input)
        #print(videoText)
        processVideo(videoText)
        #vid = 'output.mp4'
        print(user_input)
        print(videoText)
        vid = 'output.mp4'
        emotion = 'sad.png'
        return render_template("senyas.html", vid = vid, emotion = emotion)
    else:
        emotion = 'happy.png'
        return render_template("senyas.html", vid = 'intro.mp4', emotion = emotion)

if __name__ == "__main__":
    app.run()
    