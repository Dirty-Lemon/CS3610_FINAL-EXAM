from ClickClass import Click

# class Client:
def get_move_type()-> str:
    print('In what would you like to move?')
    
    moveType = input()
    documentCreator = Click()
    return documentCreator.do_move(moveType)

get_move_type()