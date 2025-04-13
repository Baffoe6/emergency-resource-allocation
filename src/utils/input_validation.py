def validate_location(location):
    if isinstance(location, str) and location.strip():
        return True
    return False

def validate_priority(priority):
    valid_priorities = ['high', 'medium', 'low']
    return priority in valid_priorities

def validate_resources(resources):
    if isinstance(resources, list) and all(isinstance(resource, str) for resource in resources):
        return True
    return False

def validate_incident_data(location, emergency_type, priority, resources):
    if not validate_location(location):
        raise ValueError("Invalid location. It must be a non-empty string.")
    if not validate_priority(priority):
        raise ValueError("Invalid priority. It must be one of: high, medium, low.")
    if not validate_resources(resources):
        raise ValueError("Invalid resources. It must be a list of resource names.")
    return True

def validate_resource_data(resource_type, availability, location):
    if not isinstance(resource_type, str) or not resource_type.strip():
        raise ValueError("Invalid resource type. It must be a non-empty string.")
    if not isinstance(availability, bool):
        raise ValueError("Invalid availability. It must be a boolean value.")
    if not validate_location(location):
        raise ValueError("Invalid location. It must be a non-empty string.")
    return True