from browser import svg

class Node:
	side = 80

	def __init__(self, pos):
		self.position = pos
		self.rect = svg.rect(x=self.position[0], y=self.position[1],
			width=Node.side, height=Node.side,
			stroke_width="5", stroke="black", fill='white')
		self.rect.bind("mousedown", self.mouse_down)
		self.rect.bind("mouseup", self.mouse_up)
		self.rect.bind("mousemove", self.mouse_moving)
		self.rect.bind("contextmenu", self.contextmenu_click)
		self.moving = False


	def mouse_down(self, event):
		self.moving = True

	def mouse_up(self, event):
		self.moving = False

	def mouse_moving(self, event):
		if self.moving:
			self.rect['x'] = event.x - Node.side/2
			self.rect['y'] = event.y - Node.side/2

	def contextmenu_click(self, event):
		print('in node')
		event.stopPropagation()
		event.preventDefault()
		