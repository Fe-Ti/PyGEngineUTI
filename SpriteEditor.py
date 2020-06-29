# Sprite editor Oak (version 1 idea 2)
# v.1.0

# standart python3 modules
from tkinter import *
from time import *
# my modules
from GUIclassModule import *
##from mapModule import * <- don't bother

app = GUI('SE')

############## FIXME:rewrite app as a class with superclass GUI #########
scale=app.INITPARAMS['scale']
t_reso = app.INITPARAMS['t_reso']
cx=app.INITPARAMS['cx']
cy=app.INITPARAMS['cy']
tg = app.INITPARAMS['tg']
#######
resx=t_reso*scale*cx
resy=t_reso*scale*cy
####################

app.t_reso = app.INITPARAMS['t_reso']

app.colorPickerL = Label (app.controlsFrame, text='Color:')
app.colorPickerL.grid(column=0,row=0)

app.colorPicker = Entry (app.controlsFrame)
app.colorPicker.grid(column=0,row=1)


app.brushSizeL = Label (app.controlsFrame, text='Size:')
app.brushSizeL.grid(column=0,row=2)

app.brushSize = Entry (app.controlsFrame)
app.brushSize.grid(column=0,row=3)
app.brushSize.insert(0,10)

app.spriteNameL = Label (app.controlsFrame,text='Sprite name:')
app.spriteNameL.grid(column=0,row=4)

app.spriteName = Entry (app.controlsFrame)
app.spriteName.grid(column=0,row=5)

app.gridToggle = Button (app.controlsFrame,text = 'Toggle grid: ON',bg='green',activebackground='green',highlightcolor='green')
app.gridToggle.grid(column=0,row=6)

app.saveSpriteB = Button (app.controlsFrame, text='Save sprite')
app.saveSpriteB.grid(column=0,row=7)

app.loadSpriteB = Button (app.controlsFrame, text='Load sprite')
app.loadSpriteB.grid(column=0,row=8)

app.exportSpriteB = Button (app.controlsFrame, text='Export sprite')
app.exportSpriteB.grid(column=0,row=9)


app.PXs = []
app.PXsData = []
# populating app.canvas

for i in range (app.t_reso):
    app.PXs.append([])
    app.PXsData.append([])
    for k in range (app.t_reso):
        x1 = i*app.INITPARAMS['scale']
        x2 = (i+1)*app.INITPARAMS['scale']
        y1 = k*app.INITPARAMS['scale']
        y2 = (k+1)*app.INITPARAMS['scale']
        coords = [x1,y1,x2,y2]
        app.PXs[i].append(app.canvas.create_rectangle(coords))
        Pixel = pixel(coords,app.canvas.itemcget(k,'fill'))
        app.PXsData[i].append(Pixel)

def refreshSprite():
    global app, tg
    
    for i in range (app.t_reso):
        for k in range (app.t_reso):
            outlineColor = (tg>0)*'black'+(tg<0)*app.PXsData[i][k].fill
            app.canvas.itemconfig(app.PXs[i][k],fill=app.PXsData[i][k].fill, outline=outlineColor)
        
def ToggleGrid(event):
    global tg
    
    tg=tg*(-1)
    if tg>0:
        app.gridToggle.config(text = 'Toggle grid: ON',bg='green',activebackground='green',highlightcolor='green')
    else:
        app.gridToggle.config(text = 'Toggle grid: OFF',bg='red',activebackground='red',highlightcolor='red')
    refreshSprite()
        
def ChangeColor(event):
    global app,tg
    
    x = int(event.x)
    y = int(event.y)
    brush_size = int(app.brushSize.get())
    items = (app.canvas.find_overlapping(x-brush_size,y-brush_size,x+brush_size,y+brush_size))
    for i in range(len(items)):
        app.canvas.itemconfig(items[i],fill = app.colorPicker.get())        
        app.canvas.itemconfig(items[i],outline = (tg>0)*'black'+(tg<0)*app.colorPicker.get())

def updatePXsData(event):
    for i in range (app.t_reso):
        for k in range (app.t_reso):
            app.PXsData[i][k].fill = app.canvas.itemcget(app.PXs[i][k],'fill')

def saveSprite(event):
    global app
    
    name = app.spriteName.get()
    sprfile = open(app.SPointer+name+'.spr','w')
    line=''
    for i in range(app.t_reso):
        for k in range(app.t_reso):
            line += app.PXsData[i][k].fill+'@'
        line=line[:-1]+'\n'
    sprfile.write(line)
    sprfile.close()
        
        
def exportSprite(event):
    global app
    name = app.spriteName.get()    
    ToggleGrid(0)
    app.canvas.postscript(file=name+".eps")
    from PIL import Image
    img = Image.open(name+".eps")
    img.thumbnail((32,32))
    img.save(name+".gif", "gif")
    ToggleGrid(0)



def loadSprite(event):
    global app
    name = app.spriteName.get()
    sprfile = open(app.SPointer+name+'.spr','r')
    line=''
    for i in range(app.t_reso):
        line = sprfile.readline().replace('\n','')
        columnColors = line.split('@')
        for k in range(app.t_reso):
            #print(i,k,columnColors[k])
            app.PXsData[i][k].fill = columnColors[k]
    refreshSprite()
    sprfile.close()

app.canvas.bind('<B1-Motion>', ChangeColor)
app.canvas.bind('<Button-1>', ChangeColor)
app.canvas.bind('<ButtonRelease>', updatePXsData)

app.gridToggle.bind('<Button>',ToggleGrid)
app.saveSpriteB.bind('<Button>',saveSprite)
app.loadSpriteB.bind('<Button>',loadSprite)
#app.exportSpriteB.bind('<Button>',exportSprite)

app.start()
