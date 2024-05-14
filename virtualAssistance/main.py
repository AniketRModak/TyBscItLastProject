from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__, template_folder='template')

app.config["MONGO_URI"] = "mongodb+srv://Aniket:Aniket86@cluster0.fewsdo9.mongodb.net/virtualA"
mongo = PyMongo(app)


@app.route("/")
def home():
    ques = mongo.db.ques.find({})
    myques = [que for que in ques]
    print(myques)
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
            print(data)
            return jsonify(data)
        else:
            data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}

    return jsonify(data)


app.run(host='0.0.0.0', port=5003)
