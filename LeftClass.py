from IRegularButtonClass import IRegularButton

class Left(IRegularButton):
    def __init__(self):
        self.__name = "Left"
    def move(self):
        return f"Moving {self.__name}"