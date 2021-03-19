from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    username: str = Column(String(30), primary_key=True)
    department: str = Column(String(2), ForeignKey="departments.code")
    department = relationship("Department", back_populates="users", cascade="all, delete, delete-orphan")

    def __init__(self, username: str, department: str):
        self.username = username
        self.department = department

    def __repr__(self):
        return f"<User(username={self.username}, department={self.department})>"

    def __str__(self):
        return self.username

    def is_manager(self) -> bool:
        pass
