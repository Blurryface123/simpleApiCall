import unittest
from mySumApi import get_sum, app


class Testsum(unittest.TestCase):

    def test_sum(self):
        data = [1,2,3]
        result = get_sum(data)
        self.assertEqual(result,6, "this test should return 6 because it sums every number in the list")

    def test_get_request(self):
        api = app.test_client()
        response = api.get('/total', content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()