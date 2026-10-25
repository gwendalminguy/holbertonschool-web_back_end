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

    def test_public_repos_url(self):
        """
        Test successful cases.
        """
        org = "apple"
        URL = f"https://api.github.com/orgs/{org}/repos"

        with unittest.mock.patch("client.GithubOrgClient.org") as mock:
            mock.return_value.json.return_value = {org: "test"}

        result = GithubOrgClient(org_name=org)._public_repos_url

        self.assertEqual(URL, result)
