from flask import json
import unittest


class BqwmTestCase(unittest.TestCase):

    def setUp(self):
        from bqwm.app import create_app
        app = create_app()
        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        pass

    def test_addManager(self):
        response = self.client.post('/v2.0/addManager')
        data = json.loads(response.data)
        assert(isinstance(data, dict))
        assert(len(data) == 0)

    def test_getConfigurationCost(self):
        response = self.client.post('/v2.0/getConfigurationCost')
        data = json.loads(response.data)
        assert(len(data["Costs"]) == 0)

    def test_createReservation(self):

        response = self.client.post('/v2.0/createReservation')
        assert(response.status_code == 400)

        response = self.client.post('/v2.0/createReservation',
                                    content_type='application/json',
                                    data=json.dumps({}))
        assert(response.status_code == 200)
        data = json.loads(response.data)
        assert(isinstance(data, dict))
        assert(len(data) == 0)

    def test_checkReservation(self):
        response = self.client.get('/v2.0/checkReservation')
        data = json.loads(response.data)
        assert(not data["Ready"])

    def test_getReservationMetrics(self):
        response = self.client.get('/v2.0/getReservationMetrics')
        data = json.loads(response.data)
        assert(len(data["Reservations"]) == 0)

    def test_releaseReservation(self):
        response = self.client.delete('/v2.0/releaseReservation')
        data = json.loads(response.data)
        assert(isinstance(data, dict))
        assert(len(data) == 0)



if __name__ == '__main__':
    unittest.main()
