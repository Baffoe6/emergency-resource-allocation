class ReallocationService:
    def reallocate_resources(self, incident, resources):
        """
        Reallocate resources to a high-priority incident.
        :param incident: Incident object
        :param resources: list of Resource objects
        :return: str
        """
        if incident.priority_level != "High":
            return "No reallocation needed"

        for resource in resources:
            if resource.resource_type in incident.required_resources and resource.availability:
                resource.availability = False
                return "Resource reallocated successfully"

        return "No available resources for reallocation"