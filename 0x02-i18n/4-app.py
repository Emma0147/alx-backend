#!/usr/bin/env python3
"""
Basic Flask app that serves an index page.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
"""
Instantiate the Babel object and set
the default locale and timezone
"""
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
     determine the best match with our supported languages.
    """
    """
    Check if the 'locale' parameter is
    present in the request arguments
    """
    locale = request.args.get('locale')
    """Check if the provided 'locale' is a supported locale"""
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    hello world
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
