from dataclasses import dataclass, field

@dataclass
class Incident:
    location: str
    emergency_type: str
    priority_level: str
    required_resources: list[str] = field(default_factory=list)

    def update_details(self, location, emergency_type, priority_level, required_resources):
        self.location = location
        self.emergency_type = emergency_type
        self.priority_level = priority_level
        self.required_resources = required_resources

    def update_priority(self, new_priority_level):
        self.priority_level = new_priority_level

