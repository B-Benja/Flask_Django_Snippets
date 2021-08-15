# basic blog with flask

from flask import Flask, render_template
from post import Post
import requests

# get example posts in json format
post_data = requests.get("https://api.npoint.io/4af156202f984d3464c3").json()
blog_data = []
for post in post_data:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    blog_data.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=blog_data)


@app.route("/post/<int:index>")
def individual_post(index):
    chosen_post = None
    for blog_post in blog_data:
        if blog_post.id == index:
            chosen_post = blog_post
    return render_template("post.html", post=chosen_post)


if __name__ == "__main__":
    app.run(debug=True)
