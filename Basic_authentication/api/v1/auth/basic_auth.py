#!/usr/bin/env python3
"""
Auth Module
"""
from api.v1.auth.auth import Auth
from flask import request
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
        ...
        """
        if (authorization_header is None
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith("Basic ")):
            return None

        content = authorization_header.strip().split(" ")[1:]
        authorization_header = " ".join(content)

        return authorization_header
