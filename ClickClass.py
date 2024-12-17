from UpButtonClass import UpButton
from DownButtonClass import DownButton
from LeftButtonClass import LeftButton
from RightButtonClass import RightButton

class Click():
    
    def do_move(self, objType: str):
        try:
            if (objType.lower() == 'up'): # return
                print(UpButton().move())
                return None
            
            elif (objType.lower() == 'down'): # return
                print(DownButton().move())
                return None
            
            elif (objType.lower() == 'left' ): # return
                print(LeftButton().move())
                return None
            
            elif (objType.lower() == 'right' ): # return
                print(RightButton().move())
                return None
            
            else: raise Exception("Invalid.\n")

        except Exception as _e:
            print(_e)

        return None