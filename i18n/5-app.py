#!/usr/bin/env python3
"""
5-app.py
Minimal Flask Application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """
    Configuration class.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


config = Config()


def get_locale():
    """
    Locale selector.
    """
    locale = request.args.get('locale')

    if locale in config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(config.LANGUAGES)


def get_user():
    """
    User selector.
    """
    user_id = request.args.get('login_as', type=int)

    return users.get(user_id)


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.before_request
def before_request():
    """
    Before request instructions.
    """
    g.user = get_user()


@app.route("/")
def home():
    """
    Basic index route.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
