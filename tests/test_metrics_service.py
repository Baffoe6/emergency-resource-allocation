import unittest
from src.services.metrics_service import MetricsService

class TestMetricsService(unittest.TestCase):
    def setUp(self):
        self.metrics_service = MetricsService()

    def test_calculate_utilization(self):
        # Example test for resource utilization
        utilization = self.metrics_service.calculate_utilization()
        self.assertIn("Resource Utilization", utilization)

if __name__ == "__main__":
    unittest.main()