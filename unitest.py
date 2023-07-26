import unittest
import json
from time import time
from app import app
from data_test import QUERIES, URLS


class TestAPIEndpoints(unittest.TestCase):
    # Call before each test
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    # Call after each test
    def tearDown(self):
        pass

    def test_get_count_y(self):
        response = self.app.get('/1/queries/count/2015')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['count'], QUERIES[0][1]['count'])

    def test_get_count_ym(self):
        response = self.app.get('/1/queries/count/2015-08')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['count'], QUERIES[1][1]['count'])

    def test_get_count_ymd(self):
        response = self.app.get('/1/queries/count/2015-08-03')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['count'], QUERIES[2][1]['count'])

    def test_get_count_ymdh(self):
        response = self.app.get('/1/queries/count/2015-08-01T00:04')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['count'], QUERIES[3][1]['count'])

    def test_get_popular_ymd(self):
        expected = QUERIES[4][1]['queries']
        response = self.app.get('/1/queries/popular/2015?size=3')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['queries'], expected)

    def test_get_popular_y(self):
        expected = QUERIES[5][1]['queries']
        response = self.app.get('/1/queries/popular/2015-08-02?size=5')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['queries'], expected)

    def test_count_break_links(self):
        res_info = []
        expected = (343, 5)
        for url in URLS:
            start = time()
            response = self.app.post(
                '/break_links', json={"url": url})
            
            elapsed = time() - start
            
            data = json.loads(response.get_data(as_text=True))
            p = {
                'elapsed': elapsed,
                'count': data['count_links'], 
                'status': response.status_code
            }
            res_info.append(p)
        
        self.assertEqual(res_info[0]['status'], 200)
        self.assertEqual(res_info[1]['status'], 200)
        self.assertEqual(res_info[0]['count'], expected[0])
        self.assertEqual(res_info[1]['count'], expected[1])
        self.assertLess(round(res_info[0]['elapsed'], 1), 60)
        self.assertLess(round(res_info[1]['elapsed'], 1), 30)


if __name__ == '__main__':
    unittest.main()
