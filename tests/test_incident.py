import unittest
from src.models.incident import Incident

class TestIncident(unittest.TestCase):

    def setUp(self):
        self.incident = Incident(location="Zone 1", emergency_type="Fire", priority_level="High", required_resources=["Fire Truck"])

    def test_incident_initialization(self):
        self.assertEqual(self.incident.location, "Zone 1")
        self.assertEqual(self.incident.emergency_type, "Fire")
        self.assertEqual(self.incident.priority_level, "High")
        self.assertEqual(self.incident.required_resources, ["Fire Truck"])

    def test_update_incident_details(self):
        self.incident.update_details(location="Zone 2", emergency_type="Medical", priority_level="Medium", required_resources=["Ambulance"])
        self.assertEqual(self.incident.location, "Zone 2")
        self.assertEqual(self.incident.emergency_type, "Medical")
        self.assertEqual(self.incident.priority_level, "Medium")
        self.assertEqual(self.incident.required_resources, ["Ambulance"])

    def test_priority_level_change(self):
        self.incident.update_priority("Low")
        self.assertEqual(self.incident.priority_level, "Low")

if __name__ == '__main__':
    unittest.main()