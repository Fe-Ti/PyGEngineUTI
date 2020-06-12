# Pinapple map editor

# std lib-s
from tkinter import *

# custom lib-s
from classModule import *

sprites=[]
vertexes=[]
visualrepresentation=[]
vv=[]
Fill=''
root = Tk()
width = 128
height = 128
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
Fill = Listbox(controls, height=len(colors))
for i in sprites:
    Fill.insert(END,i)
Fill.grid (column=2,row=3)

apply = Button (controls, text='apply object')
apply.grid(column=3,row=0)

tagsForm = Entry (controls)
tagsForm.grid (column=9, row=0)

name = Entry (controls)
name.grid (column=9, row=1)

    
def createNewMap(event): # deletes all objects
    global vertexes
    vertexes=[]
    canvas.delete("all")
    mapObjects=[]

def applyNewObj(event):
    
def saveMap (event): #saves object-properties index to file in .amef format 
    global name,mapObjects
    print (name.get())

    mapFile = open (name.get()+'.amef','w')
    for i in range(len(mapObjects)):
        mapFile.write ('#/\n')
        
        
        mapFile.write ('/#\n')


def spriteLoader(name): # linearly loads the index from file (this is quite slow due to reading line by line and several cycles)
    
    spriteElements=[] # resetting (defining) variables
    vertexes=[]
    Fill=''
    tags=[]
    counter=0

    spritefile = open (name+'.asef','r')
    line = spritefile.readline()
    while line!='':

        if line=="#/\n": # if there is an object prefix
            counter+=1
            line = spritefile.readline()
            while line!='/#\n': # do before object postfix
                
                if line=='vertex/\n': # if there is an vertex prefix
                    vertexes=[]
                    line = spritefile.readline()
                    while line!='/vertex\n': # do before facing in vertex postfix (the same can be achieved without 'while' cycle, but I want unification) 
                        line = line.replace('\n','')
                        
                        coords=line.split()
                        for i in range(len(coords)//2):
                            x=coords[i*2]
                            y=coords[i*2+1]
                            vertexes.append(vertex(x,y))

                        
                        print('loaded vertexes','in object #',counter)
                        line = spritefile.readline()
                if line=='Fill/\n': # same with fill property
                    line = spritefile.readline()
                    while line!='/Fill\n':
                        Fill=line.replace('\n','')
                        print('filled with',Fill)
                        line = spritefile.readline()
                if line=='tags/\n': # same with tags
                    line = spritefile.readline()
                    while line!='/tags\n':
                        line = line.replace('\n','')
                        tags = line.split()
                        print('tagged with',tags)
                        line = spritefile.readline()
                line = spritefile.readline()

        spriteElements.append(spriteElement(vertexes,Fill,tags))
        line = spritefile.readline()
        
    return spriteElements

def refreshMap(): # deletes everything and draws new objects on canvas from index
    global sprites
    canvas.delete('all')
    
    for i in range(len(sprites)):
        vertexes=[]
        for j in range(len(sprites[i].vertexes)):
            vertexes.append(sprites[i].vertexes[j].x)
            vertexes.append(sprites[i].vertexes[j].y)
        color = sprites[i].Fill
        tags = sprites[i].tags

        canvas.create_polygon(vertexes,fill=color,tag=tags)

def loadMap(event): # calls object loader and then refresh function (which draws new objects from index)
    global name
    mapname = (name.get())
    spritesLoader(mapname)
    refreshMap()

canvas.bind ('<Button-1>',createVertex) # binding things with functions
createMap.bind('<Button>',createNewMap)
apply.bind('<Button>',applyNewObj)
save.bind ('<Button>',saveMap)
load.bind ('<Button>',loadMap)
root.mainloop() # starting application
