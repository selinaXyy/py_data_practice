from flask import Flask, render_template, request
import requests
import smtplib

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    try:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user="selinaxue2@gmail.com", password="thisIsFakeBecauseRepoIsPublic")
            connection.sendmail(
                from_addr="selinaxue2@gmail.com",
                to_addrs="yiyangxue.xyy@gmail.com",
                msg=f"Subject:Message from your website!\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
            )

        return "<em><h1>Your message has been sent! Thanks for reaching out!!</h1><em>"

    except (error):
        print(error.message)
        return f"<h1>There was a(n) {error.name} error, please try again later!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
