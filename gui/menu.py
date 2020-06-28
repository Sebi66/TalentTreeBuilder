from browser import document, html, svg
from browser.widgets.menu import Menu
from gui import options
menu = document['menu']

menuOptions = {
    'default' : {
        'Create Node' : options.createNode,
        'Create Postit' : options.createPostit,
        'Help' : options.createNode
    },
    'node' : {
        'Create Sub-Node' : options.createSubNode,
        'Delete' : options.createNode,
    }
}

def create(x,y,node=None):
    remove()
    ul = html.UL()
    ul['class'] = 'contextMenu'
    menu <= ul
    menu.style['display'] = 'block'
    menu.style['x'] = x
    menu.style['y'] = y

    if node is None:
        print('nem node')
        createMenuItem(ul)

    else:
        print('de az')
        createMenuItem(ul, 'node', node)
    
def createMenuItem(ul, options='default', node=None):
    for text, func in menuOptions[options].items():
        print(text)
        print(func)
        li = html.LI()
        li.style['width'] = 100
        li.style['height'] = 20
        a = html.P()
        a['unselectable'] = 'on'
        a.text = str(text)
        li <= a
        ul <= li
        li.bind('mousedown', lambda ev,node=node, func=func: func(ev, node=node))


def remove():
    [c.remove() for c in menu.children]
    menu.style['display'] = 'none'
