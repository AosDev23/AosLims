# user
# user.py

class User:
    def __init__(self, full_name: str, username: str, password: str):
        """
        Initialize a User instance.

        Parameters:
        full_name (str): The full name of the user.
        username (str): The username of the user.
        password (str): The password of the user.
        """
        self.full_name = full_name
        self.username = username
        self.password = password
        self.active = False  # User is inactive by default

    def login(self):
        """Change the active status to True when the user logs in."""
        self.active = True
        print(f"{self.full_name} has logged in.")

    def __repr__(self):
        return (f"<User (full_name='{self.full_name}', "
                f"username='{self.username}', "
                f"active={self.active})>")

# Example usage
