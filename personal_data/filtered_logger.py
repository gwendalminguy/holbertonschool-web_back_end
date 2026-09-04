#!/usr/bin/env python3
"""
filtered_logger.py
Module containing the function filter_datum.
"""
from typing import List

import logging
import mysql.connector
import os
import re

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscate data using a given redation.

    Parameters:
    - fields: list of keys whose values must be obfuscated
    - redaction: string to use for obfuscation
    - message: concatenated string of key-value pairs with a separator
    - separator: string indicating the delimiter used

    Return: the result as a concatenated string obfuscated
    """
    p = r"=.*?(?=" + re.escape(separator) + r")"

    for item in fields:
        message = re.sub(re.escape(item) + p, f"{item}={redaction}", message)

    return message


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format and filter a given record to return it redacted.
        """
        f = super().format(record)

        return filter_datum(self.fields, self.REDACTION, f, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Configure a named logger at INFO level with a redacting formatter.

    Return: a configured Logger object
    """
    # Creation and configuration of the logger
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Creation of the handler and formatter
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Configure a connection to a database.

    Return: a MySQLConnection object
    """
    DB_HOST = os.getenv("PERSONAL_DATA_DB_HOST", "")
    DB_NAME = os.getenv("PERSONAL_DATA_DB_NAME", "")
    DB_USERNAME = os.getenv("PERSONAL_DATA_DB_USERNAME", "")
    DB_PASSWORD = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")

    connection = mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
    )

    return connection


def main():
    """
    Read users from a database and log informations with obfuscated PII fields.
    """
    logger = get_logger()

    db = get_db()

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    columns = [item[0] for item in cursor.description]

    for row in cursor:
        data = "".join([f"{col}={row[i]}; " for i, col in enumerate(columns)])
        logger.info(data)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
