import unittest

from Application import app

from flask import sessions


class BasicTests(unittest.TestCase):
    # Executed prior to each test
    def setUp(seldf):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # helper methods

    def register(self, email, username, password, confirm):
        return self.app.post('/register',
                             data=(email=email, username=username, password=password, confirm=confirm),
                             follow_redirects=True
                             )

    def login(self, email, password):
        return self.app.post(
            '/login',
            data=dict(email=email, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get('/login', follow redirects=True)

    def test_valid_user_registration(self):
        response = self.register(
            'tonyk@gmail.com', 'Toni', 'Password', 'Password')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thanks for registering!', response.data)

    def test_invalid_user_registration_different_passwords(self):
        response = self.register('antonyK@gmail.com',
                                 'Password', 'NotPassword')
        self.assertIn(b'Field must be equal to password.', response.data)

    def test_invalid_user_registration_duplicate_email(self):
        response = self.register('antonyK@gmail.com', 'Password', 'Password')
        self.assertEqual(response.status_code, 200)
        response = self.register('antonyK@gmail.com', 'Password', 'Password')
        self.assertIn(
            b'ERROR! Email (antonyK@gmail.com) already exists.', response.data)


if __name__ == "__main__":
    unittest.main()
