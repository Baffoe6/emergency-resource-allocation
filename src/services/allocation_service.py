class AllocationService:
    def allocate_resources(self, incidents, resources):
        for incident in incidents:
            for resource in resources:
                if resource.resource_type in incident["required_resources"] and resource.available:
                    resource.available = False
                    incident["allocated_resources"].append(resource)