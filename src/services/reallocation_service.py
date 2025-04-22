class ReallocationService:
    def reallocate_resources(self, incident, resources):
        for resource in resources:
            # Access incident as a dictionary
            if resource.resource_type in incident["required_resources"] and resource.available:
                resource.available = False
                return resource
        return None