import string
import random
from django.test import TestCase, Client


class HelloWorldTest(TestCase):
    def test_default_response(self):
        c = Client()
        response = c.get('/hello_world/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world!<br>')

    def test_msg_response(self):
        c = Client()
        response = c.get('/hello_world/?msg=abc123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world!<br>Your message was: abc123')

        response = c.get('/hello_world/?msg=%21%40%23xyz')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world!<br>Your message was: !@#xyz')

    def test_404_response(self):
        c = Client()
        response = c.get('/hello_world/1')
        self.assertEqual(response.status_code, 404)

        response = c.get('/')
        self.assertEqual(response.status_code, 404)
