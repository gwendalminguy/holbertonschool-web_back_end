#!/usr/bin/env python3
"""
Auth Module
"""
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar

import base64
import hashlib


class BasicAuth(Auth):
    """
    BasicAuth Class
    """

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """
        Extract an authorization header.
        """
        if (authorization_header is None
            or not isinstance(authorization_header, str)
                or not authorization_header.startswith("Basic ")):
            return None

        content = authorization_header.strip().split(" ")[1:]
        authorization_header = " ".join(content)

        return authorization_header

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """
        Decode a Base64 encoded authorization header.
        """
        if (base64_authorization_header is None
                or not isinstance(base64_authorization_header, str)):
            return None

        try:
            b = base64.b64decode(base64_authorization_header)
            decoded = b.decode('utf-8')
        except base64.binascii.Error:
            return None

        return decoded

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extract a user credentials from authorization header.
        """
        if (decoded_base64_authorization_header is None
            or not isinstance(decoded_base64_authorization_header, str)
                or ":" not in decoded_base64_authorization_header):
            return None, None

        email, pwd = decoded_base64_authorization_header.strip().split(":")

        return email, pwd

    def user_object_from_credentials(
        self,
        user_email: str,
        user_pwd: str
    ) -> TypeVar('User'):
        """
        Retrieve a user from its credentials.
        """
        if (user_email is None
                or not isinstance(user_email, str)):
            return None
        elif (user_pwd is None
                or not isinstance(user_pwd, str)):
            return None

        results = User().search({"email": user_email})

        if len(results) != 1:
            return None

        user = results[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user
