import unittest
from app import create_app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_greetings_page(self):
        response = self.client.get('/users/hi/John?age=30')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'JOHN', response.data)
        self.assertIn(b'30', response.data)

    def test_admin_page(self):
        response = self.client.get('/users/admin', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ADMINISTRATOR', response.data)
        self.assertIn(b'45', response.data)

if __name__ == '__main__':
    unittest.main()
