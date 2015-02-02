from flask import Flask
from flask.ext.babel import Babel

app = Flask(__name__)
babel = Babel(app)

from app import views