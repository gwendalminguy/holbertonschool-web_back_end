#!/usr/bin/env python3
"""
Auth Module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar

import hashlib


class BasicAuth(Auth):
    """
    BasicAuth Class
    """
    pass
