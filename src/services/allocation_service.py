class AllocationService:
    def allocate_resources(self, incidents, resources):
        """
        Allocate resources to incidents based on priority and availability.
        :param incidents: list of dict
        :param resources: list of Resource objects
        """
        for incident in incidents:
            for resource in resources:
                if resource.resource_type in incident["required_resources"] and resource.availability:
                    resource.availability = False
                    break