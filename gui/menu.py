from browser import document, html, svg
from browser.widgets.menu import Menu

menu = document['menu']

def create(x,y,node=None):
    remove()
    if node is None:
        ul = html.UL()
        ul['style'] = 'list-style-type:none;padding:0px;margin:0px;'
        menu <= ul
        for i in range(5):
            li = html.LI()
            li.style['width'] = 100
            li.style['height'] = 20
            a = html.A()
            a.href='#'
            a.text = str(i) + '_option'
            li <= a
            ul <= li


    else:
        ul = html.UL()
        ul['style'] = 'list-style-type:none;padding:0px;margin:0px;'
        menu <= ul
        for i in range(5):
            li = html.LI()
            li.style['width'] = 100
            li.style['height'] = 20
            a = html.A()
            a.href='#'
            a.text = str(i) + '_' + node.name
            li <= a
            ul <= li
    menu.style['display'] = 'block'
    menu.style['x'] = x
    menu.style['y'] = y

def remove():
    [c.remove() for c in menu.children]
    menu.style['display'] = 'none'
