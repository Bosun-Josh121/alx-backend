#!/usr/bin/env python3
"""
a simple flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext


app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config(object):
    """
    class used  to configure languages
    """
    LANGUAGES = ['en', 'fr']
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello_world():
    """
    parametersize
    """
    title = _("home_title")
    header = _("home_header")
    return render_template("3-index.html", title=title, header=header)


@babel.localeselector
def get_locale():
    """
    get locale
    """
    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    return locale


if __name__ == '__main__':
    app.run(debug=True)
