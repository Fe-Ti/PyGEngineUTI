import MapObjectsEditorClass as moe

app = moe.MOE()

def loadSpriteFE(event):
	name = app.spritePicker.get()
	app.loadSprite(name)
	
def loadObjectFE(event):
	name = app.MOName.get()
	app.loadObject(name)

def saveObjectFE(event):
	name = app.MOName.get()
	app.saveObject(name)

def addTagFE(event):
	app.addTag()
	
def deleteTagFE(event):
	app.deleteTag()

app.TtagsEntry.bind('<Return>',addTagFE)

app.TtagsEntry.bind('<Delete>',deleteTagFE)

app.saveObjectB.bind('<Button>',saveObjectFE)	

app.loadObjectB.bind('<Button>',loadObjectFE)
app.MOName.bind('<Return>',loadObjectFE)

app.spritePicker.bind('<Return>',loadSpriteFE)
app.start()
