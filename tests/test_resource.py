import unittest
from src.models.resource import Resource

class TestResource(unittest.TestCase):
    def setUp(self):
        self.resource = Resource(resource_type="Ambulance", availability=True, location="Zone 1")

    def test_initialization(self):
        self.assertEqual(self.resource.resource_type, "Ambulance")
        self.assertTrue(self.resource.availability)
        self.assertEqual(self.resource.location, "Zone 1")

    def test_update_availability(self):
        self.resource.update_availability(False)
        self.assertFalse(self.resource.availability)

    def test_update_location(self):
        self.resource.update_location("Zone 2")
        self.assertEqual(self.resource.location, "Zone 2")

    def test_repr(self):
        self.assertEqual(repr(self.resource), "Resource(type=Ambulance, available=True, location=Zone 1)")

if __name__ == "__main__":
    unittest.main()