from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    code: str = Column(String(30), primary_key=True)
    name: str = Column(String(2))
    director: str = Column(String(30), ForeignKey("users.username"))
    user = relationship("User", back_populates="department")

    def __init__(self, code: str, name: str, director: str):
        self.code = code
        self.name = name
        self.director = director

    def __repr__(self):
        return f"<Department(code={self.code}, name={self.name}, director={self.director})>"

    def __str__(self):
        return self.name
