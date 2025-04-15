from dataclasses import dataclass, field

@dataclass
class Incident:
    location: str
    emergency_type: str
    priority_level: str
    required_resources: list[str] = field(default_factory=list)
    status: str = "Open"  # Added a default status field

    def update_details(self, location: str, emergency_type: str, priority_level: str, required_resources: list[str]):
        """
        Update the details of the incident.
        :param location: str
        :param emergency_type: str
        :param priority_level: str
        :param required_resources: list[str]
        """
        self.location = location
        self.emergency_type = emergency_type
        self.priority_level = priority_level
        self.required_resources = required_resources

    def update_priority(self, new_priority_level: str):
        """
        Update the priority level of the incident.
        :param new_priority_level: str
        """
        self.priority_level = new_priority_level

    def add_resource(self, resource: str):
        """
        Add a resource to the required resources list.
        :param resource: str
        """
        if resource not in self.required_resources:
            self.required_resources.append(resource)

    def remove_resource(self, resource: str):
        """
        Remove a resource from the required resources list.
        :param resource: str
        """
        if resource in self.required_resources:
            self.required_resources.remove(resource)

    def close_incident(self):
        """
        Close the incident by updating its status.
        """
        self.status = "Closed"

    def __repr__(self):
        return (f"Incident(location={self.location}, emergency_type={self.emergency_type}, "
                f"priority_level={self.priority_level}, required_resources={self.required_resources}, "
                f"status={self.status})")
