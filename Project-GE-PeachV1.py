# Game engine Peach version 1
#
from tkinter import *
from time import *
print ('start')
###short reference what do what
###
###classes
### vector - class which describes a 2D vector
###
###variables
### c -counter
### i - iteration variable (same for j, k)
###
### settings - list, which contains:
###       resolx (resoly) - resolution in X axis
###       pixsize - size of one pixel (side of pixel square)
###
### canvas - canvas , where action is going)
### PxMass - 2D list of all squares of pixsize*pixsize pixels^2, they are objects of canvas
###
###
###functions
### (key-) buttonProcessor - processes (key) button presses into some human readable data (which is easy to work with)
###
###
#begin init section for global variables#

# classes:

# for game logic
class vector:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        
# for graphics
class unit:
    def __init__ (self,x,y,tag): 
        self.x=x
        self.y=y
        self.tag=tag
    pass

class vertex:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class mapObject: # describes single object on the map
    def __init__(self,vertexes,Fill,tags):
        self.Fill=Fill
        self.vertexes=vertexes
        self.tags=tags
        
c=0 #reseting counter
settings=dict()
def importSettings():
    global settings
###section for debug### there should be a data loader 
    resolx=512
    resoly=512
    pixsize=5
    goN='Up'
    goS='Down'
    goE='Right'
    goW='Left'
    gamevelocity=5#pixsize
#######################
    settings = dict()
    settings['resolx'] = resolx
    settings['resoly'] = resoly
    settings['pixsize'] = pixsize
    settings['goN'] = goN
    settings['goS'] = goS
    settings['goE'] = goE
    settings['goW'] = goW
    settings['gamevelocity'] = gamevelocity
importSettings()

#graphical
root = Tk()
canvas = Canvas (root, width=settings['resolx'], height=settings['resoly'])
canvas.grid()
player = unit(50,50,'player')
def drawPlayer():
    global player
    x1 = player.x-0.5*settings['pixsize']
    y1 = player.y-0.5*settings['pixsize']
    x2 = player.x+0.5*settings['pixsize']
    y2 = player.y+0.5*settings['pixsize']
    coords=[x1,y1,x2,y2]
    player.picture = canvas.create_rectangle(coords, fill='red', outline='red',tag=player.tag)

mapObjects=[]
types=['grass','water','forest','mountines','snow','town']
colors={
    'grass' :'#009933',
    'water':'blue',
    'forest': 'green',
    'mountines':'gray',
    'snow':'white',
    'town':'#bbaaaa'
    }
### the list below is for only testing
##PxMass = []
##PxMass.append(canvas.create_rectangle([settings['pixsize']*0,settings['pixsize']*0,settings['pixsize']*settings['resolx'],settings['pixsize']*settings['resoly']], fill='white', outline='blue',tag=('crossable','pixel')))
##PxMass.append(canvas.create_rectangle([settings['pixsize']*8,settings['pixsize']*8,settings['pixsize']*(8+1),settings['pixsize']*(8+1)], fill='black', outline='red',tag=('pixel','noncross')))
##
#############

#drawPlayer()

#end of init section for global variables
        
def exportSettings():
    global settings
    null=0

def mapObjectsLoader(name): # linearly loads the index from file (this is quite slow due to reading line by line and several cycles)
    
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
        
    return mapObjects
        
def refreshMap(mapObjects): # deletes everything and draws new objects on canvas from index

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

    drawPlayer()

    
def keyProcessor(event): #processes key presses, transforming raw data into easy to read and work bits ('brother' of a buttonProcessor)
    action=str(event.keysym)
    print(action)
    coordinator(action)
def buttonProcessor(event): #processes button presses, transforming raw data into easy to read and work bits ('brother' of a keyProcessor)
    action='B'+str(event.num)
    print(action)
    coordinator(action)


def pointMover(vec): #moves rectangles ("pixels") along vector\
    global c
    c=0
    def stepper():
        global c, settings
        x1 = player.x-0.5*settings['pixsize']+2*vec.x
        y1 = player.y-0.5*settings['pixsize']+2*vec.y
        x2 = player.x+0.5*settings['pixsize']+2*vec.x
        y2 = player.y+0.5*settings['pixsize']+2*vec.y
        
        if 'crossable' in canvas.itemcget(canvas.find_overlapping(x1,y1,x2,y2)[-2],"tag"):
            player.x+=vec.x
            player.y+=vec.y
            canvas.move('player', vec.x, vec.y)
            if c<=settings['gamevelocity']:
                root.after(10,stepper)
                c+=1
    stepper()
    
def coordinator(action): # coordinates movements and actions (handles controls hardbinded with settings)
    CONTROLS = { 
        settings['goS'] : [0,1], 
        settings['goN'] : [0,-1],
        settings['goE'] : [1,0],
        settings['goW'] : [-1,0],
        }
    if action in CONTROLS:
        vec = vector(CONTROLS.get(action,0)[0],CONTROLS.get(action,0)[1]) # get direction coordinates for the vector
        print (vec.x,' ',vec.y)
        pointMover(vec)

	

root.bind("<KeyRelease>",keyProcessor)
root.bind("<ButtonPress>",buttonProcessor)

MO = mapObjectsLoader('test')
refreshMap(MO)
root.mainloop()

