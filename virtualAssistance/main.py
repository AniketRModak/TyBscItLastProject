from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "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"


app = Flask(__name__, template_folder='template')

app.config["MONGO_URI"] = "mongodb+srv://Aniket:Aniket86@cluster0.fewsdo9.mongodb.net/virtualA"
mongo = PyMongo(app)


@app.route("/")
def home():
    ques = mongo.db.ques.find({})
    myques = [que for que in ques]
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        que = mongo.db.ques.find_one({"question": question})
        print(que)
        if que:
            data = {"question": question, "answer": f"{que['answer']}"}
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
            mongo.db.ques.insert_one(
                {"question": question, "answer": response["choices"][0]["text"]})
            return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}

    return jsonify(data)


app.run(host='0.0.0.0', port=5003)
