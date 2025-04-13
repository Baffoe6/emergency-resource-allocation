class Incident:
    def __init__(self, location, emergency_type, priority_level, required_resources):
        """
        Initialize an incident with location, type, priority level, and required resources.
        :param location: str
        :param emergency_type: str
        :param priority_level: str (e.g., "High", "Medium", "Low")
        :param required_resources: list of str
        """
        self.location = location
        self.emergency_type = emergency_type
        self.priority_level = priority_level
        self.required_resources = required_resources

    def update_details(self, location, emergency_type, priority_level, required_resources):
        """
        Update the details of the incident.
        :param location: str
        :param emergency_type: str
        :param priority_level: str
        :param required_resources: list of str
        """
        self.location = location
        self.emergency_type = emergency_type
        self.priority_level = priority_level
        self.required_resources = required_resources

    def update_priority(self, new_priority_level):
        """
        Update the priority level of the incident.
        :param new_priority_level: str
        """
        self.priority_level = new_priority_level

    def __repr__(self):
        return f"Incident(location={self.location}, emergency_type={self.emergency_type}, priority_level={self.priority_level}, required_resources={self.required_resources})"
    
    