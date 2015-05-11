"""First python file"""

def listItems( item  ):
    if isinstance(item,list):
        listItems(item)
    else : print(item)

    
