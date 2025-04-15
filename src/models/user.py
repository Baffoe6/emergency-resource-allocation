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

    def change_password(self, old_password, new_password):
        """
        Change the user's password if the old password matches.
        :param old_password: str
        :param new_password: str
        :return: bool
        """
        if self.authenticate(self.username, old_password):
            self.password = new_password
            return True
        return False

    def update_role(self, new_role):
        """
        Update the user's role.
        :param new_role: str
        """
        self.role = new_role
