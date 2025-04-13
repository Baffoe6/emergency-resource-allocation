class Resource:
    def __init__(self, resource_type, availability, location):
        """
        Initialize a resource with type, availability, and location.
        :param resource_type: str
        :param availability: bool
        :param location: str
        """
        self.resource_type = resource_type
        self.availability = availability
        self.location = location

    def update_availability(self, new_availability):
        """
        Update the availability of the resource.
        :param new_availability: bool
        """
        self.availability = new_availability

    def update_location(self, new_location):
        """
        Update the location of the resource.
        :param new_location: str
        """
        self.location = new_location

    def __repr__(self):
        return f"Resource(type={self.resource_type}, available={self.availability}, location={self.location})"