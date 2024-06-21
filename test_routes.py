import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')

    def test_add(self):
        response = self.app.get('/add/5/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'result': 8})

        # Test for bad request (non-numeric input)
        response = self.app.get('/add/hello/world')
        self.assertEqual(response.status_code, 404)  # Bad request


if __name__ == '__main__':
    unittest.main()
