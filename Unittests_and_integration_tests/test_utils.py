#!/usr/bin/env python3
"""
Generic utilities for GitHub org client.
"""
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

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


class TestMemoize(unittest.TestCase):
    """
    Unittests for memoize function.
    """

    def test_memoize(self):
        """
        Test successful cases.
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with unittest.mock.patch.object(
            TestClass,
            "a_method",
            return_value=42
        ) as mock:
            instance = TestClass()

            result_a = instance.a_property
            result_b = instance.a_property

        mock.assert_called_once()
        self.assertEqual(result_a, 42)
        self.assertEqual(result_b, 42)
