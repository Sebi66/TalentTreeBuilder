from browser import document, html, svg
from browser.widgets.dialog import Dialog, EntryDialog, InfoDialog
from functools import partial

def createInputDialog(title, callBack,  inputs={}, *args, **kwargs):
	d = Dialog(title, ok_cancel=True)

	for item in inputs:
		if item['input_type'] is 'text':
			d.panel <= html.DIV(item['name'] + html.INPUT(id=item['id']))
		elif item['input_type'] is 'select':
			d.panel <= html.DIV(item['name']
		+ html.SELECT([html.OPTION(op) for op in item['options']], id=item['id']))
		elif item['input_type'] is 'textarea':
			d.panel <= html.DIV(item['name']
		+ html.TEXTAREA(id=item['id']) )

	d.ok_button.bind('click', lambda ev,dialog=d,args=args,kwargs=kwargs: callBack(ev, dialog=d, *args, **kwargs))