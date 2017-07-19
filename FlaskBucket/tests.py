# tests.py

import unittest

from flask import url_for, abort

from flask_testing import TestCase

import run

import DataHandler


class TestModels(TestCase):

    def test_userdict_model(self):
        """
        Test if USER_DICT exists
        """
        self.assertEqual(DataHandler.USER_DICT == {})

    def test_bucketlist_model(self):
        """
        Test if BUCKETLIST works
        """
        ds = DataHandler.BUCKETLIST
        ds.append('Event')
        self.assertEqual(len(ds), 1)


class TestViews(TestCase):

    def test_homepage_view(self):
        """
        Test that homepage is not accessible without login
        """
        response = self.run(url_for('home.html'))
        self.assertEqual(response.status_code, 500)

    def test_signup_view(self):
        """
        Test that signup page is accessible
        """
        response = self.run(url_for('register'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_page(self):
        """
        Test that invalid page redirects to 404 page
        """
        response = self.run(url_for('invalid'))
        self.assertEqual(response.status_code, 404)


class TestErrorPages(TestCase):

    def test_403_forbidden(self):
        # create route to abort the request with the 403 Error
        @self.app.route('/403')
        def forbidden_error():
            abort(403)

        response = self.run.get('/403')
        self.assertEqual(response.status_code, 403)
        self.assertTrue("403 Error" in response.data)

    def test_404_not_found(self):
        response = self.run.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        self.assertTrue("404 Error" in response.data)

    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.run.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue("500 Error" in response.data)

if __name__ == '__main__':
    unittest.main()
