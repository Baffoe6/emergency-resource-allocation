# filepath: src/models/resource.py
class Resource:
    def __init__(self, resource_type, available, location, history=None):
        self.resource_type = resource_type  # Fix attribute name
        self.available = available  # Fix attribute name
        self.location = location
        self.history = history if history is not None else []

    def __repr__(self):
        return f"Resource(type={self.resource_type}, available={self.available}, location={self.location})"
