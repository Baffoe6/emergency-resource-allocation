import unittest
import sys
import os

# Add the `src` directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models.resource import Resource
from services.allocation_service import AllocationService

class TestAllocationService(unittest.TestCase):
    def setUp(self):
        self.allocation_service = AllocationService()
        self.resource1 = Resource(resource_type="Fire Truck", availability=True, location="Zone 1")
        self.resource2 = Resource(resource_type="Ambulance", availability=True, location="Zone 2")
        self.resources = [self.resource1, self.resource2]

    def test_allocate_high_priority_incident(self):
        incident = {"location": "Zone 1", "priority": "High", "required_resources": ["Fire Truck"]}
        self.allocation_service.allocate_resources([incident], self.resources)
        self.assertFalse(self.resource1.availability)

if __name__ == "__main__":
    unittest.main()