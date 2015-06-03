from flask import json
import unittest
from bqwm import api


class BqwmTestCase(unittest.TestCase):

    def setUp(self):
        app = api.create_app()
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_true(self):
        assert(True)

    def test_checkReservation(self):
        rv = self.app.get('/v2.0/checkReservation')
        data = json.loads(rv.data)
        assert(not data["Ready"])

if __name__ == '__main__':
    unittest.main()
