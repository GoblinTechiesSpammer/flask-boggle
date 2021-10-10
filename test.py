from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont_show_debug_toolbar']

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    
    # def setUp(self):
    #     self.client = app.test_client()    
    
    def test_home_page(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<form method="GET" id="word-guess">', html)
    
    def test_guess(self):
        with app.test_client() as client:
            res = client.get("/guess", query_string={'word': 'test'})

            self.assertEqual(res.status_code, 200)