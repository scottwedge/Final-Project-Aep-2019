import unittest
from story import app
import json

class TestStory(unittest.TestCase):

        def setUp(self):
                self.app = app
                self.client = self.app.test_client()
                self.data = {"title": "ABC", "text": "Blah", "ip": 1, "state": 1}

        def test_start_story(self):
                resp = self.client.post(path='/story/start', data=json.dumps(self.data), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, { "title": "ABC" })



if __name__ == '__main__':
	unnittest.main()