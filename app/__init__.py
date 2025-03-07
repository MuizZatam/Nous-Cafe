# importing main flask class - Flask
from flask import Flask

# instantiates the application
app = Flask(__name__)

# imports routes module from app package
from app import routes