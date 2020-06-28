from browser import svg
from gui import menu

LEFT = 1
RIGHT = 3

class Node:
    width,height = 100,50
    padding = 5
    active_moving = None
    active_hover = None

    def __init__(self, panel, name, active=True, cost=0):
        self.name = name
        self.active = active
        self.cost = cost

        self.description = 'Edit description'

        self.x,self.y = 0,0
        self.anchor = 0,0
        self.svg_rect = svg.rect(x=0, y=0,
            width=Node.width, height=Node.height,
            stroke_width=2, stroke="black", fill='white')
        self.svg_name = svg.text(self.name,
            x=0,y=0,
            font_size=20,text_anchor='middle',dominant_baseline="hanging")
        self.svg_active = svg.text(['Passive','Active'][self.active],
            x=0,y=0,
            font_size=15,text_anchor='start',dominant_baseline="baseline")
        self.svg_cost = svg.text(str(self.cost),
            x=0,y=0,
            font_size=15,text_anchor='end',dominant_baseline="baseline")

        self.svg_rect.bind("mousedown", self.mouse_down)
        self.svg_rect.bind("mouseup", self.mouse_up)
        self.svg_rect.bind("mousemove", self.mouse_moving)
        self.svg_rect.bind("mouseout", self.mouse_out)
        self.svg_rect.bind("mouseover",self.mouse_over)
        self.moving = False

        panel <= self.svg_rect
        panel <= self.svg_name
        panel <= self.svg_active
        panel <= self.svg_cost

        self.update()

    @property
    def position(self):
        return self.x,self.y

    @position.setter
    def position(self, value):
        self.x,self.y = value
        self.update()

    def update(self):
        x,y = self.x,self.y
        self.svg_rect['x'] = x
        self.svg_rect['y'] = y
        self.svg_name['x'] = x + self.width/2
        self.svg_name['y'] = y + Node.padding
        self.svg_active['x'] = x + Node.padding
        self.svg_active['y'] = y + self.height - Node.padding
        self.svg_cost['x'] = x + self.width - Node.padding
        self.svg_cost['y'] = y + self.height - Node.padding

        self.svg_name.text = self.name
        self.svg_active.text = ['Passive','Active'][self.active]
        self.svg_cost.text = str(self.cost)

    def mouse_down(self, event):
        button = event.which
        if button is LEFT:
            self.moving = True
            Node.active_moving = self
            self.anchor = event.x - self.x, event.y - self.y
            menu.remove()
        event.stopPropagation()

    def mouse_up(self, event):
        button = event.which
        if button is LEFT:
            self.moving = False
            Node.active_moving = None
        elif button is RIGHT:
            menu.create(event.x,event.y,self)
        event.stopPropagation()

    def mouse_moving(self, event):
        if self.moving:
            self.position = event.x - self.anchor[0], event.y - self.anchor[1]

    def mouse_out(self, event):
        self.mouse_moving(event)
        Node.active_hover = None

    def mouse_over(self, event):
        Node.active_hover = self
        event.stopPropagation()