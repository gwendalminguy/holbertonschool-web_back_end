#!/usr/bin/env python3
"""
Client tests.
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, call

import json
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    Unittests for GitHubOrgClient class.
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
            result = GithubOrgClient(org).public_repos()

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
        result = GithubOrgClient("test").has_license(repo, license_key)

        self.assertEqual(has_license, result)


@parameterized_class(
    (
        "org_payload",
        "repos_payload",
        "expected_repos",
        "apache2_repos",
    ),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GitHubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch("requests.get")
        cls.mock = cls.get_patcher.start()

        response_1 = Mock()
        response_2 = Mock()

        response_1.json.return_value = cls.org_payload
        response_2.json.return_value = cls.repos_payload

        cls.mock.side_effect = [
            response_1,
            response_2,
        ]

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        ...
        """
        org_name = "google"
        client = GithubOrgClient(org_name)

        self.assertEqual(
            client.public_repos(),
            self.expected_repos
        )

        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )

        self.assertEqual(self.mock.call_count, 2)
        self.mock.assert_has_calls([
            call(f"https://api.github.com/orgs/{org_name}"),
            call(self.org_payload["repos_url"]),
        ])
