from app import app, babel
from app.config import LANGUAGES
from flask.ext.babel import gettext
from flask import request

@babel.localeselector
def get_locale():
	# Basic method, can be used as a fallback if a user's profile does not specify a language,
	# or a user hasn't yet registered.
	result = request.accept_languages.best_match(LANGUAGES.keys())

	# will return language code (en/es/etc).
	return 'es'
	return result

@app.route('/')
def index():
	return gettext('Please translate me, I am a message or some stuff!') + ' ' + gettext('My name is %(name)s.', name = 'Tony')
