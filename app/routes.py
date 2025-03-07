# render template is used to map a html template
# with a view function
from flask import render_template

# imports application instance from __init__.py
from app import app


# route decorators map web app urls to a view function
# this function's logic is executed when the associated
# route is visited
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

    # the render_template takes an arbitary number of arguments
    # along with a template name that serve as the outgoing
    # data to the view
    return render_template('index.html', title = "Home", user = user, posts = posts)