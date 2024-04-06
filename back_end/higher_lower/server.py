from flask import Flask

#decorator function
def make_italic(function):
    def wrapper_func():
        return "<em>" + function() + "</em>"
    return wrapper_func

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9!</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='A gif that shows numbers 0 to 9' />" 

@app.route("/0")
def num0():
    return "<h1>WAY TOO LOW! This is not the correct number.</h1><img src='https://media.giphy.com/media/ulQ9ljaDmiGR4SSEsB/giphy.gif?cid=790b7611cfmnetctt7b16r5ob250chgpof2z97yxuc6mxtd3&ep=v1_gifs_search&rid=giphy.gif&ct=g' alt='gif of number 0'/>"

@app.route("/1")
def num1():
    return "<h1>TOO LOW!! Guess another number.</h1>"

@app.route("/2")
def num2():
    return "<h1>STILL LOW! Guess another number.</h1>"

@app.route("/3")
def num3():
    return "<h1>Come on... HIGHER!!!</h1>"

@app.route("/4")
def num4():
    return "<h1>Guess a higher number!</h1>"

@app.route("/5")
def num5():
    return "<h1>You are getting there!!!</h1>"

@app.route("/6")
def num6():
    return "<h1>Almost there!!!!!</h1>"

@app.route("/7")
@make_italic
def num7():
    return "<h1>You got me!!! 7 is my favorite number!!</h1><img src='https://media.giphy.com/media/xT9IgxiUfXHycuUkRW/giphy.gif?cid=790b7611z9bujpyhwn72ep0dwg0008nox6vcneklicq3tukd&ep=v1_gifs_search&rid=giphy.gif&ct=g' alt='a gif of number 7'"

@app.route("/8")
def num8():
    return "<h1>A little too high. Can you guess the right number?</h1>"

@app.route("/9")
def num9():
    return "<h1>High. Bye.</h1>"

if __name__ == "__main__":
    app.run(debug=True)