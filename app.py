from queue import Empty
from flask import Flask, redirect, url_for, render_template, request
import time
from movie import processVideo
from clean import cleanText, processText
from sentiment import translate
import os

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.context_processor
def override_url_for():
    """
    Generate a new token on every request to prevent the browser from
    caching static files.
    """
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



@app.route("/", methods=["POST", "GET"])

def home():
    user_input = ''

    if request.method == "POST":
        user_input = request.form["hidden"]
        #print(user_input)
        sentimentText = cleanText(user_input)
        #print(sentimentText)
        sentiment_score = translate(sentimentText)
        if sentiment_score >= 0:
            emotion = 'happy.png'
        else:
            emotion = 'sad.png'
        videoText = processText(user_input)
        #print(videoText)
        if videoText:
            processVideo(videoText)

            #vid = 'output.mp4'
            print(user_input)
            print(videoText)
            print(sentiment_score)
            vid = 'output.mp4'
            return render_template("senyas.html", vid = vid, emotion = emotion)
        else:
             emotion = 'happy.png'
             return render_template("senyas.html", vid = 'intro.mp4', emotion = emotion)

    else:
        emotion = 'happy.png'
        return render_template("senyas.html", vid = 'intro.mp4', emotion = emotion)

if __name__ == "__main__":
    app.run()
    