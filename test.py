import unittest
from app import app
from flask import jsonify

class StandUpComedyApiTests(unittest.TestCase):
    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):

        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

    def test_test_logging_success(self):

        response = self.app.get('/test?param=test')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test successful with param', response.json['message'])

    def test_test_logging_error(self):

        response = self.app.get('/test?param=error')
        self.assertEqual(response.status_code, 500)
        self.assertIn('Internal server error', response.json['error'])

    def test_missing_param(self):

        response = self.app.get('/test')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing \'param\' query parameter', response.json['error'])

if __name__ == '__main__':
    unittest.main()
