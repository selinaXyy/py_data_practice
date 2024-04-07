from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def get_home():
    current_year = datetime.now().year
    return render_template("index.html", year=current_year)

@app.route("/guess/<name>")
def get_guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}").json()
    age_response = requests.get(f"https://api.agify.io?name={name}").json()

    name = name.title()
    gender = gender_response["gender"]
    age = age_response["age"]

    return render_template("guess_page.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

    return render_template("blog.html", posts=blog_response)

if __name__ == "__main__":
    app.run(debug=True)