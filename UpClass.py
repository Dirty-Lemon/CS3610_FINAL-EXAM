from IRegularButtonClass import IRegularButton

class Up(IRegularButton):
    def __init__(self):
        self.__name = "Up"
    def move(self):
        return f"Moving {self.__name}"