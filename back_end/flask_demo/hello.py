# save this as app.py
from flask import Flask

#function definitions
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

#### Flask instance creation and root route definition decides where __main__ is ####
#create an instance of Flask
app = Flask(__name__) #__name__ == the current file where the app code is located

#root route of app
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/<name>/<int:number>") #converter:variable
def greet(name):
    return f"Hey {name}!\nYou're {number} years old!"

@app.route("/bye") #order of decorators are followed by sequence
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)