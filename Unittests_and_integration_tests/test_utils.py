#!/usr/bin/env python3
"""
Generic utilities for GitHub org client.
"""
from parameterized import parameterized
from utils import access_nested_map, get_json

import json
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittests for access_nested_map function.
    """

    @parameterized.expand([
        [{"a": 1}, ("a",), 1],
        [{"a": {"b": 2}}, ("a",), {"b": 2}],
        [{"a": {"b": 2}}, ("a", "b"), 2],
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test successful cases.
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        [{}, ("a",)],
        [{"a": 1}, ("a", "b")],
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test exception cases.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unittests for get_json function.
    """

    @parameterized.expand([
        ["http://example.com", {"payload": True}],
        ["http://holberton.io", {"payload": False}],
    ])
    def test_get_json(self, url, payload):
        """
        Test successful cases.
        """
        with unittest.mock.patch("requests.get") as mock:
            mock.return_value.json.return_value = payload
            result = get_json(url)

        mock.assert_called_once_with(url)
        self.assertEqual(result, payload)
