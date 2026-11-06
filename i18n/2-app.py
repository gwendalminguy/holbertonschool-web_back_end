#!/usr/bin/env python3
"""
2-app.py
Minimal Flask Application
"""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    return request.accept_languages.best_match(config.LANGUAGES)


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """
    Basic index route.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
