from LeftClass import Left
from IRegularButtonClass import IRegularButton

class LeftButton:

    def move(self)-> IRegularButton:
        return Left().move()