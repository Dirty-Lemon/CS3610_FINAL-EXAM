from IRegularButtonClass import IRegularButton

class Down(IRegularButton):
    def __init__(self):
        self.__name = "Down"
    def move(self):
        return f"Moving {self.__name}"