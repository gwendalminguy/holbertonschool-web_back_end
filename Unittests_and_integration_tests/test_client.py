#!/usr/bin/env python3
"""
Client tests.
"""
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch

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
    @patch("client.get_json", return_value={})
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

        with patch("client.GithubOrgClient.org") as mock:
            mock.return_value.json.return_value = {org: "test"}

        result = GithubOrgClient(org_name=org)._public_repos_url

        self.assertEqual(URL, result)

    @patch("client.get_json", return_value=[{
        "name": "test"
    }])
    def test_public_repos(self, mock_get_json):
        """
        Test successful cases.
        """
        org = "apple"

        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=unittest.mock.PropertyMock,
        ) as mock_url:
            mock_url.return_value = f"https://api.github.com/orgs/{org}/repos"
            result = GithubOrgClient(org_name=org).public_repos()

        self.assertEqual(result, ["test"])
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}/repos"
        )
        mock_url.assert_called_once()

    @parameterized.expand([
        [{"license": {"key": "my_license"}}, "my_license", True],
        [{"license": {"key": "other_license"}}, "my_license", False],
    ])
    def test_has_license(self, repo, license_key, has_license):
        """
        Test successful cases.
        """
        result = GithubOrgClient(org_name="test").has_license(repo, license_key)

        self.assertEqual(has_license, result)
