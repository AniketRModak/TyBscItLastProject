from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route("/")
def main():
    return render_template('index.html')


app.run(host='0.0.0.0', port=5006)
