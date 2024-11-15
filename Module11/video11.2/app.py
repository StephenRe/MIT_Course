from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
books = [
    {
        "author": "Hernando de Soto",
        "country": "Peru",
        "language": "English",
        "pages": 209,
        "title": "The Mystery of Capital",
        "year": 1970,
    },
    {
        "author": "Hans Christian Andersen",
        "country": "Denmark",
        "language": "Danish",
        "pages": 784,
        "title": "Fairy tales",
        "year": 1836,
    },
    {
        "author": "Dante Alighieri",
        "country": "Italy",
        "language": "Italian",
        "pages": 928,
        "title": "The Divine Comedy",
        "year": 1315,
    },
]
username = "steve"

@app.route("/", methods=["GET"])
def firstRoute():
    return render_template("index.html", username=username)


@app.route("/books", methods=["GET"])
def getBooks():
    #return jsonify(books)
    return render_template('books.html', books=books, username=username)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
