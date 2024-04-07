from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", text="It works!")

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["name"]
    password = request.form["password"]
    return render_template("info.html", name=name, password=password)

if __name__ == "__main__":
    app.run(debug=True)