"""First python file"""

def listItems( items  ):
	for item in items:
		if isinstance(item,list):
			listItems(item)
		else : print(items)

    
