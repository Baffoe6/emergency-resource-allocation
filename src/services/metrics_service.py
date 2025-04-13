class MetricsService:
    def __init__(self):
        self.resources_in_use = 0
        self.total_resources = 0

    def update_resource_count(self, total_resources, resources_in_use):
        """
        Update the total resources and resources currently in use.
        :param total_resources: int
        :param resources_in_use: int
        """
        self.total_resources = total_resources
        self.resources_in_use = resources_in_use

    def calculate_utilization(self):
        """
        Calculate the percentage of resources currently in use.
        :return: str
        """
        # Placeholder logic for utilization calculation
        resources_in_use = 5
        total_resources = 10
        utilization = (resources_in_use / total_resources) * 100
        return f"Resource Utilization: {utilization:.2f}%"

    def predict_availability(self, resources):
        """
        Predict when resources will become available based on their ETC (Estimated Time to Completion).
        :param resources: list of resource objects with an 'etc' attribute
        :return: list of tuples (resource, time_to_availability)
        """
        predictions = []
        for resource in resources:
            if not resource.availability:
                predictions.append((resource, resource.etc))
        return predictions