from flask import Flask, request, render_template, session, make_response
from flask import redirect
from functools import wraps
import os
app = Flask(__name__)
app.secret_key = "secretkey"
app.config["UPLOADED_PHOTOS_DEST"] = "static"

books = [
    {
        "id": 1,
        "author": "Hernando de Soto",
        "country": "Peru",
        "language": "English",
        "pages": 209,
        "title": "The Mystery of Capital",
        "year": 1970,
        "price":20.17
    },
    {
        "id": 2,
        "author": "Hans Christian Andersen",
        "country": "Denmark",
        "language": "Danish",
        "pages": 784,
        "title": "Fairy tales",
        "year": 1836,
        "price":35.00
    },
    {
        "id": 3,
        "author": "Dante Alighieri",
        "country": "Italy",
        "language": "Italian",
        "pages": 928,
        "title": "The Divine Comedy",
        "year": 1315,
        "price":16.00
    },
    {
        "id": 4,
        "author": "William Shakespeare",
        "country": "UK",
        "language": "English",
        "pages": 100,
        "title": "Romeo and Juliet",
        "year": 1597,
        "price":60.00
    },
    {
        "id": 5,
        "author": "William Shakespeare",
        "country": "UK",
        "language": "English",
        "pages": 100,
        "title": "Hamlet",
        "year": 1603,
        "price":30.00
    },
    {
        "id": 6,
        "author": "William Shakespeare",
        "country": "UK",
        "language": "English",
        "pages": 100,
        "title": "Macbeth",
        "year": 1623,
        "price":25.90
    },
]

users = [{"username": "testuser", "password": "testuser"}]


def loginrequired(fn):
    @wraps(fn)
    def decorator(*args, **kwargs):
        # check in session for username
        fromBrowser = session.get("username")
        # check if this is a legitimate user
        for user in users:
            if user["username"] == fromBrowser:
                return fn(*args, **kwargs)
        # otherwise send user to register
        return redirect("static/register.html")

    return decorator


def checkUser(username, password):
    for user in users:
        if username in user["username"] and password in user["password"]:
            return True
    return False


@app.route("/", methods=["GET"])
def firstRoute():
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if checkUser(username, password):
            # set session token to users name
            session["username"] = username
            return render_template(
                "index.html", username=session["username"]
            )
        else:
            return render_template("register.html")
    elif request.method == "GET":
        return render_template("register.html")


@app.route("/logout")
def logout():
    # remove the username from the session if it is there
    session.pop("username", None)
    return "Logged Out of Books"


@app.route("/books", methods=["GET"])
@loginrequired
def getBooks():
    user = session["username"]
    return render_template('books.html', username=user, books=books)

@app.route("/addbook", methods=["GET", "POST"])
@loginrequired
def addBook():
    username = session["username"]
    if request.method == "GET":
        return render_template("addBook.html")
    if request.method == "POST":
        # expects pure json with quotes everywheree
        author = request.form.get("author")
        title = request.form.get("title")
        newbook = {"author": author, "title": title}
        books.append(newbook)
        return render_template(
            "books.html", books=books, username=username, title="books"
        )
    else:
        return 400


@app.route("/addimage", methods=["GET", "POST"])
@loginrequired
def addimage():
    if request.method == "GET":
        return render_template("addimage.html")
    elif request.method == "POST":
        image = request.files["image"]
        id = request.form.get("number")  # use id to number the image
        imagename = "image" + id + ".png"
        image.save(os.path.join(app.config["UPLOADED_PHOTOS_DEST"], imagename))
        print(image.filename)
        return "image loaded"

    return "all done"

@app.route("/buybook")
def buybook():
    user = session["username"]
    bookIdParam = request.args.get("bookId")
    #to list any books already in the cookie
    bookCookie = ''
    #to house the list of books from the books list above
    booksToPurchase = []
    #if the cookie exists
    if 'booksToPurchase' in request.cookies:
        #and there are already book ids in it
        if request.cookies.get("booksToPurchase") != None:
            #add the book id string to bookCookie
            bookCookie = request.cookies.get("booksToPurchase")
    #for each book in the books list above
    for book in books:
        #if the book already exists in the cookie
        if str(book['id']) in bookCookie.split(','):
            #add the all of the book info to the booksToPurchase list
            booksToPurchase.append(book)
        #if it does not already exist in the cookie
        else:
            #if there is a matching book id to bookIdParam
            if str(book['id']) == bookIdParam:
                #add the all of the book info to the booksToPurchase list
                booksToPurchase.append(book)
                #update the bookCookie string to reset the cookie at the end
                bookCookie += ','+str(book['id'])
    #now we have a complete booksToPurchase list to pass to the buybook.html
    response = make_response(render_template('buybook.html', username = user, booksToPurchase = booksToPurchase))
    #reset cookie with new list of books, stripping off any leading or trailing commas.
    response.set_cookie('booksToPurchase', bookCookie.strip(','))
    return response



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
