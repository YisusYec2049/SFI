# Here we will create the abstract methods to inherit logic for creating users.
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass

    @abstractmethod
    def validate_user(self):
        pass
