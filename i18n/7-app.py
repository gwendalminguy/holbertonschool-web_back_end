#!/usr/bin/env python3
"""
3-app.py
Minimal Flask Application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, utc
from pytz.exceptions import UnknownTimeZoneError


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
    locale = request.args.get("locale")
    user_locale = g.user.get("locale") if g.user else None

    if locale in config.LANGUAGES:
        return locale
    elif user_locale in config.LANGUAGES:
        return user_locale

    return request.accept_languages.best_match(config.LANGUAGES)


def get_timezone():
    """
    Timezone selector.
    """
    tz = request.args.get("timezone")
    user_tz = g.user.get("timezone") if g.user else None

    if tz is not None:
        try:
            tz = timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass
    elif user_tz is not None:
        try:
            user_tz = timezone(user_tz)
            return user_tz
        except UnknownTimeZoneError:
            pass

    return utc


def get_user():
    """
    User selector.
    """
    user_id = request.args.get("login_as", type=int)

    return users.get(user_id)


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel()
babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)


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
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
