import unittest
import sys
import os

# Add the `src` directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User(username="admin", password="admin123", role="admin")

    def test_authenticate_success(self):
        self.assertTrue(self.user.authenticate("admin", "admin123"))

    def test_authenticate_failure(self):
        self.assertFalse(self.user.authenticate("admin", "wrongpassword"))
        self.assertFalse(self.user.authenticate("wronguser", "admin123"))

    def test_user_representation(self):
        self.assertEqual(repr(self.user), "User(username=admin, role=admin)")

if __name__ == "__main__":
    unittest.main()