from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():

    user = {"username": "Muiz"}

    posts = [

        {
            "author": {"username": "Samuel"},
            "body": "Technofeudalism is a bane for society"
        },
        {
            "author": {"username": "Ahmed"},
            "body": "Islam as a Philosophy to Life"
        }
    ]

    return render_template('index.html', title = "Home", user = user, posts = posts)