from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def firstRoute():
    return render_template("index.html", message="Hello Earthling")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
