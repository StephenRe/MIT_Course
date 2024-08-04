from flask import Flask, request
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Practicing Cookies!</h1>"

@app.route("/addCookie")
def addCookie():
    response = make_response("<h1>Cookie added!</h1>");
    # add code to add cookie here
    response.set_cookie('myFirstCookie', 'Hello World - my first cookie!')
    return response

@app.route("/displayCookieValue")
def displayCookieValue():
    cookieValue = None
    # add code to get the cookie value (inside try block)
    try:
        cookieValue = request.cookies.get('myFirstCookie')
        return "<h1>Found the cookie: " + cookieValue + "</h1>"
    except:
        return "<h1>Cookie not found!</h1>"
    
@app.route("/removeCookie")
def removeCookie():
    res = make_response("Cookie removed!")
    # add code to remove cookie here (set max_age = 0)
    res.set_cookie('myFirstCookie', '', max_age=0)
    return res

app.run(host='0.0.0.0', port=88)