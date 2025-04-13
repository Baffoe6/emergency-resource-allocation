import unittest
from src.models.incident import Incident
from src.models.resource import Resource
from src.services.reallocation_service import ReallocationService

class TestReallocationService(unittest.TestCase):
    def setUp(self):
        self.reallocation_service = ReallocationService()
        self.incident1 = Incident(location="Zone 1", emergency_type="Fire", priority_level="High", required_resources=["Fire Truck"])
        self.incident2 = Incident(location="Zone 2", emergency_type="Medical", priority_level="Low", required_resources=["Ambulance"])
        self.resource1 = Resource(resource_type="Fire Truck", availability=True, location="Zone 1")
        self.resource2 = Resource(resource_type="Ambulance", availability=True, location="Zone 2")
        self.resources = [self.resource1, self.resource2]

    def test_no_reallocation_when_no_high_priority_incident(self):
        result = self.reallocation_service.reallocate_resources(self.incident2, self.resources)
        self.assertEqual(result, "No reallocation needed")

    def test_reallocate_resource_to_high_priority_incident(self):
        result = self.reallocation_service.reallocate_resources(self.incident1, self.resources)
        self.assertEqual(result, "Resource reallocated successfully")
        self.assertFalse(self.resource1.availability)

    def test_reallocation_with_unavailable_resource(self):
        self.resource1.availability = False
        result = self.reallocation_service.reallocate_resources(self.incident1, self.resources)
        self.assertEqual(result, "No available resources for reallocation")

if __name__ == "__main__":
    unittest.main()