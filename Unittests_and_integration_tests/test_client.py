#!/usr/bin/env python3
"""
Client tests.
"""
from client import GithubOrgClient
from parameterized import parameterized

import json
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    Unittests for access_nested_map function.
    """

    @parameterized.expand([
        ["google"],
        ["abc"],
    ])
    @unittest.mock.patch("client.get_json", return_value={})
    def test_org(self, org, mock):
        """
        Test successful cases.
        """
        URL = f"https://api.github.com/orgs/{org}"

        result = GithubOrgClient(org_name=org).org

        mock.assert_called_once_with(URL)
        self.assertEqual(result, {})
        
