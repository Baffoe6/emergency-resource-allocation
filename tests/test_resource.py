import unittest
from src.models.resource import Resource  # Adjust the import path as needed

class TestResource(unittest.TestCase):
    def setUp(self):
        self.resource = Resource(resource_type="Ambulance", available=True, location="Zone 1", history=[])

    def test_repr(self):
        self.assertEqual(
            repr(self.resource),
            "Resource(type=Ambulance, available=True, location=Zone 1)"
        )

if __name__ == "__main__":
    unittest.main()