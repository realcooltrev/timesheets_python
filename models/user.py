from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from .role import Role

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    role = Column(String)

    def __init__(self, username: str, role: Role):
        self.username = username
        self.role = role

    def __repr__(self):
        return f"<User(username={self.username}, role={self.role})>"

    def __str__(self):
        return self.username
