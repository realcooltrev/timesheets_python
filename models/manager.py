from .user import User


class Manager(User):
    def __init__(self, username: str):
        User.__init__(self, username)
