from flask import Flask, render_template
from Post import Post
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    id = post["id"]
    title = post["title"]
    subtitle = post["subtitle"]
    body = post["body"]

    post_object = Post(id, title, subtitle, body)
    post_objects.append(post_object)

@app.route('/')
def home():
    return render_template("index.html", my_posts=post_objects)

@app.route('/blog/<int:blog_id>')
def get_blog(blog_id):
    for obj in post_objects:
        if obj.id == blog_id:
            blog = obj
            return render_template("post.html", post=blog)

if __name__ == "__main__":
    app.run(debug=True)
