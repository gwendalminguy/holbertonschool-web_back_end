#!/usr/bin/env python3
"""
1-app.py
Minimal Flask Application
"""
from flask import Flask, render_template
from flask_babel import Babel

class Config():
    """
    Configuration class.
    """
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)

config = Config()

babel = Babel(
    app,
    locale_selector=config.LANGUAGES[0],
    timezone_selector="UTC",
)


@app.route("/")
def home():
    """
    Basic index route.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
