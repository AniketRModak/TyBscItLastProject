from flask import Flask, render_template, jsonify, request

import openai

openai.api_key = "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"


app = Flask(__name__, template_folder='template')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/api", methods=["GET", "POST"])
def qa():

    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        print(question)
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
        return jsonify(data)
    return jsonify(data)


app.run(host='0.0.0.0', port=5003)
