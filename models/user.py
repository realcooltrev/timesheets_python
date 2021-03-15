class User:
    def __init__(self, username: str):
        self.username = username

    def __repr__(self):
        return f"User(username: {self.username})"

    def __str__(self):
        return self.username
