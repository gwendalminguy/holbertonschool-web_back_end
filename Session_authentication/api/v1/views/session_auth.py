#!/usr/bin/env python3
"""
SessionAuth Views Module
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User

import os

SESSION_NAME = os.getenv("SESSION_NAME")


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Initiate an authentication session with credentials.

    Return:
        - the User object with the session ID in a cookie
    """
    from api.v1.app import auth

    email = request.form.get("email")
    pwd = request.form.get("password")

    if email is None or len(email) == 0:
        return jsonify({"error": "email missing"}), 400

    if pwd is None or len(pwd) == 0:
        return jsonify({"error": "password missing"}), 400

    results = User().search({"email": email})

    if len(results) != 1:
        return jsonify({"error": "no user found for this email"}), 404

    user = results[0]

    if not user.is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user_id=user.id)

    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)

    return response
