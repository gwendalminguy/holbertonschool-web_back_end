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
        ...
        """
        if path is None or excluded_paths is None :
            return True

        # Clean trailing slashes
        clean_path = path[:-1] if path.endswith("/") else path
        clean_excluded_paths = [p[:-1] if p.endswith("/") else p for p in excluded_paths]

        if clean_path not in clean_excluded_paths:
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
