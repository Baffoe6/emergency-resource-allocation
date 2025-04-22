import unittest
import sys
import os

# Add the `src` directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.models.resource import Resource
from src.services.allocation_service import AllocationService

class TestAllocationService(unittest.TestCase):
    def setUp(self):
        self.resource1 = Resource(resource_type="Fire Truck", available=True, location="Zone 1")
        self.resource2 = Resource(resource_type="Ambulance", available=False, location="Zone 2")
        self.resources = [self.resource1, self.resource2]
        self.incident = {"required_resources": ["Fire Truck"], "allocated_resources": []}
        self.allocation_service = AllocationService()

    def test_allocate_high_priority_incident(self):
        self.allocation_service.allocate_resources([self.incident], self.resources)
        self.assertFalse(self.resource1.available)
        self.assertIn(self.resource1, self.incident["allocated_resources"])

if __name__ == "__main__":
    unittest.main()