import unittest
from story import app
import json

class TestStory(unittest.TestCase):

        def setUp(self):
                self.app = app
                self.client = self.app.test_client()
                self.story1 = {"title": "ABC", "text": "Blah", "current_user": 1, "state": 1}

        def test_a_start_story(self):
                resp = self.client.post(path='/story/start', data=json.dumps(self.story1), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, { "title": "ABC" })

        def test_b_list_story(self):
                resp = self.client.get(path='/story/list', content_type='application/json')
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(resp.json, {'0': 'ABC'})

        def test_c_display_story(self):
                resp = self.client.get(path='/story/ABC', content_type='application/json')
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(resp.json, {'title': {'0': 'ABC'}, 'text': {'0': "Blah"}, 'current_user': {'0': 1}, "state": {'0': 1}})



if __name__ == '__main__':
	unnittest.main()