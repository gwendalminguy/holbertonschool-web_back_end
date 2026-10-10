#!/usr/bin/env python3
"""
app.py
Minimal Flask Application
"""
from flask import Flask, jsonify, request, abort

from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.get("/")
def root():
    """
    Welcome route.
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.post("/users")
def users():
    """
    Create a user.
    """
    data = request.form

    email = data.get("email")
    password = data.get("password")

    if email is None:
        return jsonify({"message": "missing email"}), 400

    if password is None:
        return jsonify({"message": "missing password"}), 400

    try:
        AUTH.register_user(email=email, password=password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 200


@app.post("/sessions")
def login():
    """
    Start an authentication session.
    """
    data = request.form

    email = data.get("email")
    password = data.get("password")

    if email is None:
        return jsonify({"message": "missing email"}), 400

    if password is None:
        return jsonify({"message": "missing password"}), 400

    is_valid = AUTH.valid_login(
        email=email,
        password=password,
    )

    if not is_valid:
        abort(401)

    session_id = AUTH.create_session(email=email)

    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
