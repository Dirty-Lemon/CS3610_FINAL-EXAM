from abc import ABC, abstractmethod
class IRegularButton(ABC):

    @staticmethod
    @abstractmethod
    def move()-> None:    # "-> None means function returns"
        pass