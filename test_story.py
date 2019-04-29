import unittest
from story import app
import json

class TestStory(unittest.TestCase):

        def setUp(self):
                self.app = app
                self.client = self.app.test_client()
                self.story1 = {"title": "ABC", "text": "First sentence.", "current_user": 1, "state": 1}

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
                self.assertEqual(resp.json, {'title': {'0': 'ABC'}, 'text': {'0': "First sentence."}, 'current_user': {'0': 1}, "state": {'0': 1}})

        def test_d_edit_story(self):
                data = {"title": "ABC", "new_text": " Second sentence.", "current_user": 1, "state": 1}
                resp = self.client.put(path='/story/ABC/edit', data=json.dumps(data), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, {'text': {'0': {'0': "First sentence. Second sentence."}}, 'current_user': {'0': 1}})

        def test_e_edit_story_new_user(self):
                data = {"title": "ABC", "new_text": " Third sentence.", "current_user": 2, "state": 1}
                resp = self.client.put(path='/story/ABC/edit', data=json.dumps(data), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, {'text': {'0': {'0': {'0': "First sentence. Second sentence. Third sentence."}}}, 'current_user': {'0': 2}})
        
        def test_f_end_story(self):
                resp = self.client.put(path='/story/ABC/end', content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, {'0': 0})
                


if __name__ == '__main__':
	unnittest.main()