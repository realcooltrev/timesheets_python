import argparse

from sqlalchemy import create_engine

from models.exceptions import LoginError
from models.role import Role
from models.user import User


def get_cli_args() -> argparse.Namespace:
    """Parse the incoming arguments passed in via the CLI"""
    parser = argparse.ArgumentParser(
        description="A CLI solution for clocking in/out that no one asked for")
    parser.add_argument(
        "-u", "--username", help="The username for user clocking in/out")
    parser.add_argument(
        "-p", "--password", help="The password for the user clocking in/out")
    return parser.parse_args()


def login(username: str, password: str) -> User:
    """Attempt to authenticate the user using their username and password"""
    # Just a placeholder until further functionality is setup
    SECRET_KEY: Final = "admin"
    MANAGER_USERNAME: Final = "trev"

    role: Role

    if password != SECRET_KEY:
        raise LoginError()

    if username == MANAGER_USERNAME:
        role = Role.Manager
    else:
        role = Role.Employee

    return User(username, role)


if __name__ == "__main__":
    args = get_cli_args()

    engine = create_engine("sqlite: // /: memory: ", echo=True)
    username = args.username
    password = args.password

    try:
        user = login(username, password)
        print(user)
    except LoginError:
        print("Error: Username/Password combination is invalid")
