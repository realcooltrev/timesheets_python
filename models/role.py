from enum import Enum, auto


class Role(Enum):
    Employee = auto()
    Manager = auto()

    def __repr__(self):
        return f"<Role.{self.name}: {self.value}>"

    def __str__(self):
        return self.name
