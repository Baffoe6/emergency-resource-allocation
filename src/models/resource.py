class Resource:
    def __init__(self, resource_type: str, availability: bool, location: str):
        """
        Initialize a resource with type, availability, and location.
        :param resource_type: str
        :param availability: bool
        :param location: str
        """
        self.resource_type = resource_type
        self.availability = availability
        self.location = location
        self.history = []  # Added a history attribute to track changes

    def update_availability(self, new_availability: bool):
        """
        Update the availability of the resource.
        :param new_availability: bool
        """
        self.availability = new_availability
        self.history.append(f"Availability updated to {new_availability}")

    def update_location(self, new_location: str):
        """
        Update the location of the resource.
        :param new_location: str
        """
        self.location = new_location
        self.history.append(f"Location updated to {new_location}")

    def add_to_history(self, action: str):
        """
        Add an action to the resource's history.
        :param action: str
        """
        self.history.append(action)

    def get_history(self):
        """
        Get the history of changes made to the resource.
        :return: list[str]
        """
        return self.history

    def __repr__(self):
        return (f"Resource(type={self.resource_type}, available={self.availability}, "
                f"location={self.location}, history={self.history})")
