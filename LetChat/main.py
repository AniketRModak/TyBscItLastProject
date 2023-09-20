from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "sk-BOz0sKATZ7V69aWDsqRAT3BlbkFJi0Zn87dFb5hlWnORZqTXx"


app = Flask(__name__, template_folder='template')

app.config["MONGO_URI"] = "mongodb+srv://Aniket:Aniket86@cluster0.fewsdo9.mongodb.net/Chatgpt"
mongo = PyMongo(app)


@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)


@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"question": question, "answer": f"{chat['answer']}"}
            return jsonify(data)
        else:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            print(response)
            data = {"question": question,
                    "answer": response["choices"][0]["text"]}
            mongo.db.chats.insert_one(
                {"question": question, "answer": response["choices"][0]["text"]})
            return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}

    return jsonify(data)


@app.route('/about')
def about():
    return render_template('about.html', )


app.run(host='0.0.0.0', port=5002)
