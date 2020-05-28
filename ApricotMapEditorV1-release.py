# one of the simplest vector graphics editor

from tkinter import *

# P.S. maybe it will be a map editor for Peach game engine, who knows

class vertex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class mapObject: # describes single object on the map
    def __init__(self,vertexes,Fill,tags):
        self.Fill=Fill
        self.vertexes=vertexes
        self.tags=tags
        

types=['grass','water','forest','mountines','snow','town']
colors={
    'grass' :'#009933',
    'water':'blue',
    'forest': 'green',
    'mountines':'gray',
    'snow':'white',
    'town':'#bbaaaa'
    }
mapObjects=[]
vertexes=[]
visualrepresentation=[]
vv=[]
Fill=''
root = Tk()
width = 512
height = 512
pixsize = 10


canvas = Canvas (root, scrollregion=(0,0,width,height), bg='#dddddd')#describe canvas
canvas.grid (column=0,row=0)
scrolly = Scrollbar(root, orient=VERTICAL,command=canvas.yview)
scrollx = Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
canvas.config(yscrollcommand=scrolly.set)
canvas.config(xscrollcommand=scrollx.set)
scrolly.grid (column=1,row=0, sticky=(N,S))
scrollx.grid (column=0,row=1, sticky=(W,E))

controls = Frame(root) #frame where controls are placed, which are described below 
controls.grid (column=0,row=2)

createMap = Button(controls, text='create new map')
createMap.grid (column=0,row=0)

save = Button(controls, text='save')
save.grid (column=10,row=1)

load = Button(controls,text='load')
load.grid(column=10,row=2)
Fill = Listbox(controls, height=len(types))
for i in types:
    Fill.insert(END,i)
Fill.grid (column=2,row=3)

apply = Button (controls, text='apply object')
apply.grid(column=3,row=0)

tagsForm = Entry (controls)
tagsForm.grid (column=9, row=0)

name = Entry (controls)
name.grid (column=9, row=1)

def createVertex(event): # creates 1 vertex
    x=canvas.canvasx(event.x)
    y=canvas.canvasy(event.y)
    print (canvas.canvasx(event.x), '  ', canvas.canvasy(event.y))
    vv.append(canvas.create_rectangle ([x-0.5,y-0.5,x+0.5,y-0.5], outline = 'yellow', tag= "vertex")) #(actual size of this is 2x2 pixels)
    vertexes.append(vertex(x,y))
    
def createNewMap(event): # deletes all objects
    global vertexes
    vertexes=[]
    canvas.delete("all")
    mapObjects=[]

def applyNewObj(event):
    global mapObjects, vertexes, Fill, visualrepresentation
    fillment=str(types[Fill.curselection()[0]])
    print (fillment)
    tags = tagsForm.get()
    tags = tags.split()
    current=mapObject(vertexes,fillment,tags) # add object to the object-propeties index

    v=[] 
    for i in range (len(vertexes)):
        v.append(vertexes[i].x)
        v.append(vertexes[i].y)
    visualrepresentation.append(canvas.create_polygon(v, fill=colors[fillment], tag=tags)) #draw objects in canvas

    mapObjects.append(current) # add cur. obj. to list of all mapObjects
    vertexes=[] # reset vertexes
    canvas.delete('vertex')
    print (mapObjects[-1].vertexes)
    
def saveMap (event): #saves object-properties index to file in .amef format 
    global name,mapObjects
    print (name.get())

    mapFile = open (name.get()+'.amef','w')
    for i in range(len(mapObjects)):
        mapFile.write ('#/\n')
        mapFile.write ('vertex/\n')
        vertexes=""
        for j in range(len(mapObjects[i].vertexes)):
            vertexes+=str(mapObjects[i].vertexes[j].x)+' '+str(mapObjects[i].vertexes[j].y)+" "
        mapFile.write (vertexes+'\n')
        mapFile.write ('/vertex\n')
        mapFile.write ('Fill/\n')
        mapFile.write(str(mapObjects[i].Fill)+'\n')
        mapFile.write ('/Fill\n')
        mapFile.write ('tags/\n')
        tags=''
        for j in mapObjects[i].tags:
            tags += (j+' ')
        mapFile.write(tags+'\n')
        mapFile.write ('/tags\n')        
        mapFile.write ('/#\n')


def mapObjectsLoader(name): # linearly loads the index from file (this is quite slow due to reading line by line and several cycles)
    global mapObjects

    mapObjects=[] # resetting (defining) variables
    vertexes=[]
    Fill=''
    tags=[]
    counter=0

    mapfile = open (name+'.amef','r')
    line = mapfile.readline()
    while line!='':

        if line=="#/\n": # if there is an object prefix
            counter+=1
            line = mapfile.readline()
            while line!='/#\n': # do before object postfix

                if line=='vertex/\n': # if there is an vertex prefix
                    vertexes=[]
                    line = mapfile.readline()
                    while line!='/vertex\n': # do before facing in vertex postfix (the same can be achieved without 'while' cycle, but I want unification) 
                        line = line.replace('\n','')
                        
                        coords=line.split()
                        for i in range(len(coords)//2):
                            x=coords[i*2]
                            y=coords[i*2+1]
                            vertexes.append(vertex(x,y))

                        
                        print('loaded vertexes','in object #',counter)
                        line = mapfile.readline()
                if line=='Fill/\n': # same with fill property
                    line = mapfile.readline()
                    while line!='/Fill\n':
                        Fill=line.replace('\n','')
                        print('filled with',Fill)
                        line = mapfile.readline()
                if line=='tags/\n': # same with tags
                    line = mapfile.readline()
                    while line!='/tags\n':
                        line = line.replace('\n','')
                        tags = line.split()
                        print('tagged with',tags)
                        line = mapfile.readline()
                line = mapfile.readline()

        mapObjects.append(mapObject(vertexes,Fill,tags))
        line = mapfile.readline()

def refreshMap(): # deletes everything and draws new objects on canvas from index
    global mapObjects
    canvas.delete('all')
    
    for i in range(len(mapObjects)):
        vertexes=[]
        for j in range(len(mapObjects[i].vertexes)):
            vertexes.append(mapObjects[i].vertexes[j].x)
            vertexes.append(mapObjects[i].vertexes[j].y)
        Fill = mapObjects[i].Fill
        color = colors[Fill]
        tags = mapObjects[i].tags

        canvas.create_polygon(vertexes,fill=color,tag=tags)

def loadMap(event): # calls object loader and then refresh function (which draws new objects from index)
    global name
    mapname = (name.get())
    mapObjectsLoader(mapname)
    refreshMap()

canvas.bind ('<Button-1>',createVertex) # binding things with functions
createMap.bind('<Button>',createNewMap)
apply.bind('<Button>',applyNewObj)
save.bind ('<Button>',saveMap)
load.bind ('<Button>',loadMap)
root.mainloop() # starting application
