from browser import document, svg, timer, html
from gui.node import Node

panel = document['panel']
tooltip = document['tooltip']
tooltip.parent.style['display'] = 'none'

def contextmenu_click(event):
    button = event.which
    print('panel')
    if button is 1:
        if Node.active_moving is not None:
            Node.active_moving.mouse_up(event)
    elif button is 3:
       cNode = Node(panel,'Unnamed')
       cNode.position = event.x,event.y

def panel_move(event):
    if Node.active_moving is not None:
        Node.active_moving.mouse_moving(event)
        tooltip.parent.style['display'] = 'none'
    elif Node.active_hover is not None:
        node = Node.active_hover
        tooltip.parent['x'] = node.x + node.width
        tooltip.parent['y'] = node.y
        tooltip.text = node.description
        tooltip.parent.style['display'] = 'block'
    else:
        tooltip.parent.style['display'] = 'none'

panel.parent.bind("mouseup", contextmenu_click)
panel.parent.bind("mousemove", panel_move)

node = Node(panel,'Skill1',active=False,cost=2)
node2 = Node(panel,'Skill2',cost=3)
node.position = 300,100
node.description = 'Scroll of Wisdom'
node2.position = 400,200
node2.description = 'Mirror of Kalandra'



