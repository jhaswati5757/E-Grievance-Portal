import unittest
from app import app

class EGrievanceTestCase(unittest.TestCase):
    def setUp(self):
        # Setup testing client for our Flask application
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # 1. Test if home page loads successfully (HTTP 200)
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome to', result.data)

    def test_login_page_loads(self):
        # 2. Test if login page loads text
        result = self.app.get('/login')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Student Login', result.data)

    def test_register_page_loads(self):
        # 3. Test if register page loads
        result = self.app.get('/register')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Student Registration', result.data)

    def test_admin_login_page_loads(self):
        # 4. Test admin login page
        result = self.app.get('/admin_login')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Admin', result.data)

    def test_dashboard_access_without_login(self):
        # 5. Accessing dashboard without login should redirect (HTTP 302 Redirection)
        result = self.app.get('/dashboard')
        self.assertEqual(result.status_code, 302)

if __name__ == '__main__':
    unittest.main()
