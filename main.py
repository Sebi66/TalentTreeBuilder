from browser import document, svg, timer
from gui.node import Node



panel = document['panel']

def contextmenu_click(event):
	print('panel')
	cNode = Node((event.x, event.y))
	panel<=cNode.rect

panel.parent.bind("contextmenu", contextmenu_click)



node = Node((500,100))
node2 = Node((300,200))

panel<=node.rect
panel<=node2.rect