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


class SessionAuth(Auth):
    """
    SessionAuth Class
    """
    pass
