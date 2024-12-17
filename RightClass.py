from IRegularButtonClass import IRegularButton

class Right(IRegularButton):
    def __init__(self):
        self.__name = "Right"
    def move(self):
        return f"Moving {self.__name}"