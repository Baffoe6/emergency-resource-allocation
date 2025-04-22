import unittest
from src.models.resource import Resource
from src.services.reallocation_service import ReallocationService

class TestReallocationService(unittest.TestCase):
    def setUp(self):
        self.resource1 = Resource(resource_type="Fire Truck", available=True, location="Zone 1")
        self.resource2 = Resource(resource_type="Ambulance", available=False, location="Zone 2")
        self.resources = [self.resource1, self.resource2]
        self.incident1 = {"required_resources": ["Fire Truck"], "allocated_resources": []}
        self.reallocation_service = ReallocationService()

    def test_reallocate_resource_to_high_priority_incident(self):
        result = self.reallocation_service.reallocate_resources(self.incident1, self.resources)
        self.assertFalse(self.resource1.available)
        self.assertEqual(result, self.resource1)

    def test_reallocation_with_unavailable_resource(self):
        self.resource1.available = False
        result = self.reallocation_service.reallocate_resources(self.incident1, self.resources)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()