import os
import bucketlist
import unittest
import tempfile


class BucketlistTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, bucketlist.app.config['DATABASE'] = tempfile.mkstemp()
        bucketlist.app.testing = True
        self.app = bucketlist.app.test_client()
        with bucketlist.app.app_context():
            bucketlist.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(bucketlist.app.config['DATABASE'])

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert b'You were logged in' in rv.data
        rv = self.logout()
        assert b'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert b'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert b'Invalid password' in rv.data

    def test_posts(self):
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
            title='<Hello>', self.login('admin', 'default')
            rv=self.app.post('/add', data=dict(
                title='<Hello>',
                text='<strong>HTML</strong> allowed here'
            ), follow_redirects=True)
            assert b'No entries here so far' not in rv.data
            assert b'&lt;Hello&gt;' in rv.data
            assert b'<strong>HTML</strong> allowed here' in rv.data

            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert b'No entries here so far' not in rv.data
        assert b'&lt;Hello&gt;' in rv.data
        assert b'<strong>HTML</strong> allowed here' in rv.data


if __name__ == '__main__':
    unittest.main()
