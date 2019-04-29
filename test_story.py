import unittest
from story import app
import json

class TestStory(unittest.TestCase):

        def setUp(self):
                self.app = app
                self.client = self.app.test_client()
                self.story1 = {"title": "ABC", "text": "First sentence.", "current_user": 1, "state": 1}
                self.story2 = {"title": "Greetings", "text": "Good morning.", "current_user": 1, "state": 1}

        def test_a_start_story1(self):
                resp = self.client.post(path='/story/start', data=json.dumps(self.story1), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, { "title": "ABC" })

        def test_b_list_story1(self):
                resp = self.client.get(path='/story/list', content_type='application/json')
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(resp.json, {'0': 'ABC'})

        def test_c_display_story1(self):
                resp = self.client.get(path='/story/ABC', content_type='application/json')
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(resp.json, {'title': {'0': 'ABC'}, 'text': {'0': "First sentence."}, 'current_user': {'0': 1}, "state": {'0': 1}})

        def test_d_edit_story1(self):
                data = {"title": "ABC", "new_text": " Second sentence.", "current_user": 1, "state": 1}
                resp = self.client.put(path='/story/ABC/edit', data=json.dumps(data), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, {'text': {'0': {'0': "First sentence. Second sentence."}}, 'current_user': {'0': 1}})

        def test_e_edit_story1_new_user(self):
                data = {"title": "ABC", "new_text": " Third sentence.", "current_user": 2, "state": 1}
                resp = self.client.put(path='/story/ABC/edit', data=json.dumps(data), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, {'text': {'0': {'0': {'0': "First sentence. Second sentence. Third sentence."}}}, 'current_user': {'0': 2}})
        
        def test_f_end_story1(self):
                resp = self.client.put(path='/story/ABC/end', content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, {'0': 0})

        def test_g_start_story2(self):
                resp = self.client.post(path='/story/start', data=json.dumps(self.story2), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, { "title": "Greetings" })

        def test_h_edit_story2_new_user(self):
                data = {"title": "Greetings", "new_text": " Good night.", "current_user": 3, "state": 1}
                resp = self.client.put(path='/story/Greetings/edit', data=json.dumps(data), content_type='application/json')
                self.assertEqual(resp.status_code, 201)
                self.assertEqual(resp.json, {'text': {'1': {'1': "Good morning. Good night."}}, 'current_user': {'1': 3}})

        def test_i_list_story1and2(self):
                resp = self.client.get(path='/story/list', content_type='application/json')
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(resp.json, {'0': 'ABC', '1': 'Greetings'})

        def test_j_display_story1_users(self):
                resp = self.client.get(path='/story/ABC/users', content_type='application/json')
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(resp.json, {'title': {'0': 'ABC', '1': 'ABC'}, 'user': {'0': 1, '1': 2}})

        def test_k_display_story2_users(self):
                resp = self.client.get(path='/story/Greetings/users', content_type='application/json')
                self.assertEqual(resp.status_code, 200)
                self.assertEqual(resp.json, {'title': {'2': 'Greetings', '3': 'Greetings'}, 'user': {'2': 1, '3': 3}})

                


if __name__ == '__main__':
	unnittest.main()