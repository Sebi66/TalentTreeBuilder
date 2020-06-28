from browser import document, html, svg
from browser.widgets.menu import Menu
from gui.input_dialog import createInputDialog
from gui import node

#def createInputDialog(title, callBack,  inputs={}):

talentTypes = {'Active' : True, 'Passive' : False}
panel= document['panel']

def cNode(event, dialog, *args, **kwargs):
	print(dialog.select_one("TEXTAREA#talent_descr").text)
	new_node = node.Node(panel,
		dialog.select_one('#talent_name').value,
	 	active=talentTypes[dialog.select_one("SELECT#talent_type").value],
	 	cost=dialog.select_one("INPUT#talent_cost").value)
	new_node.position = event.x,event.y
	new_node.description = dialog.select_one("TEXTAREA#talent_descr").value
	if (parentNode:=kwargs.get('parentNode', None)) is not None:
		parentNode.addChild(new_node)
	dialog.close()

def createNode(event, *args, **kwargs):
	inputs = [
		dict(
			input_type = 'text',
			name = 'Name: ',
			id   = 'talent_name'
		),
		dict(
			input_type = 'text',
			name = 'Cost: ',
			id   = 'talent_cost'
		),
		dict(
			input_type = 'select',
			name = 'Type: ',
			id   = 'talent_type',
			options = talentTypes
		),
		dict(
			input_type = 'textarea',
			name = 'Description: ',
			id   = 'talent_descr'
		)
	]
	createInputDialog('Title', cNode, inputs, *args, **kwargs)

def createSubNode(event, node):
	child_node = createNode(event, parentNode = node)

def createPostit(event):
	pass