class User:
    def __init__(self, username, password, role):
        """
        Initialize a user with a username, password, and role.
        :param username: str
        :param password: str
        :param role: str (e.g., "admin", "coordinator", "viewer")
        """
        self.username = username
        self.password = password
        self.role = role

    def authenticate(self, username, password):
        """
        Authenticate the user by checking the username and password.
        :param username: str
        :param password: str
        :return: bool
        """
        return self.username == username and self.password == password

    def __repr__(self):
        return f"User(username={self.username}, role={self.role})"
