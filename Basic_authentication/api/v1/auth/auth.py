#!/usr/bin/env python3
"""
Auth Module
"""
from flask import request
from typing import List, TypeVar

import hashlib


class Auth():
    """
    Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check wether the given path requires authentication or not.
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        # Clean trailing slashes
        path = path[:-1] if path.endswith("/") else path
        excluded_paths = [
            p[:-1] if p.endswith("/") else p for p in excluded_paths
        ]

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        ...
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        ...
        """
        return None
