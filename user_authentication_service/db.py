#!/usr/bin/env python3
"""
db.py
DB module
"""
from sqlalchemy import create_engine, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """
    DB class.
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance.
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memorized session object.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Create and return a user.
        """
        user = User(
            email=email,
            hashed_password=hashed_password,
        )

        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user using arbitrary keyword arguments.
        """
        names = User.__table__.columns.keys()

        filters = []

        # Build filters.
        for key, value in kwargs.items():
            if key not in names:
                raise InvalidRequestError(f"Unknown field: {key}")
            filters.append(getattr(User, key) == value)

        if not len(filters):
            raise InvalidRequestError("At least one keyword is required.")

        result = select(User).where(*filters).limit(1)

        return self._session.scalars(result).one()
