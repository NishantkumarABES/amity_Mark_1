from flask import Flask, redirect, url_for, render_template, request
import gtts
import playsound
from bot import answerMe

count = 0


def speak(text):
    global count
    sound = gtts.gTTS(str(text), lang="hi")
    sound.save("welcome" + str(count) + ".mp3")
    playsound.playsound("welcome" + str(count) + ".mp3")
    count = count + 1


app = Flask(__name__, template_folder="template", static_folder="static")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/chatbot")
def veda():
    return render_template('chatbot.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    speak(str(msg))
    Input = msg
    text = get_chat_response(Input)
    speak(text)
    return text



def get_chat_response(text):
    response_text = str(answerMe(text))
    return response_text


@app.route("/blog_page")
def blog_page():
    return render_template('blog_page.html')


# createIndex('Knowledge')
# speak("something")
app.run(debug= True)
