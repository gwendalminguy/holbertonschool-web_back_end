#!/usr/bin/env python3
"""
app.py
Minimal Flask Application
"""
from flask import Flask, jsonify, request, abort, redirect

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


@app.delete("/sessions")
def logout():
    """
    End an authentication session.
    """
    cookies = request.cookies

    session_id = cookies.get("session_id")

    if session_id is None:
        abort(403)

    db_user = AUTH.get_user_from_session_id(session_id=session_id)

    if db_user is None:
        abort(403)

    AUTH.destroy_session(user_id=db_user.id)

    return redirect("/")


@app.get("/profile"):
def profile():
    """
    ...
    """
    cookies = request.cookies

    session_id = cookies.get("session_id")

    if session_id is None:
        abort(403)

    db_user = AUTH.get_user_from_session_id(session_id=session_id)

    if db_user is None:
        abort(403)

    jsonify({"email": db_user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
