from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
import openai

openai.api_key = "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"


app = Flask(__name__, template_folder='template')

app.config["MONGO_URI"] = "mongodb+srv://Aniket:Aniket86@cluster0.fewsdo9.mongodb.net/imageGen"
mongo = PyMongo(app)


@app.route("/")
def home():
    imgs = mongo.db.imgs.find({})
    myimgs = [img for img in imgs]
    print(myimgs)
    return render_template("index.html", myimgs=myimgs)


@app.route("/api", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        img = mongo.db.imgs.find_one({"question": question})
        print(img)
        if img:
            data = {"question": question,
                    "answer": img['answer']}
            return jsonify(data)
        else:
            print("prompt:", question)
            response = openai.Image.create(
                prompt=question, n=5, size="256x256")
            print(response)
            data = {"question": question,
                    "answer": response["data"]}
            mongo.db.imgs.insert_one(
                {"question": question, "answer": response["data"]})

            return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
    return jsonify(data)


@app.route('/about')
def about():
    return render_template('about.html', )


app.run(host='0.0.0.0', port=5008)
