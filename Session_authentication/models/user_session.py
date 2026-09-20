#!/usr/bin/env python3
"""
UserSession Module
"""
from models.base import Base

import hashlib


class UserSession(Base):
    """
    UserSession Class
    """

    def __init__(self, *args: list, **kwargs: dict):
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
