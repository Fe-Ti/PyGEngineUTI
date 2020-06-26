# classes:

from tkinter import *


class vector: # defines a vector
    def __init__ (self,x,y):
        self.x=x
        self.y=y

class mapObject: # defines a single mapobject
    def __init__(self,spriteName,position,tags):
        self.spriteName=spriteName # name of the sprite
        self.x=position[0]
        self.y=position[1]
        self.tags=tags

class unit: # defines a unit
    def __init__ (self,x,y,tag): 
        self.x=x
        self.y=y
        self.tag=tag
    def drawUnit(self,canvas,pixsize):
        x1 = self.x-0.5*pixsize
        y1 = self.y-0.5*pixsize
        x2 = self.x+0.5*pixsize
        y2 = self.y+0.5*pixsize
        coords=[x1,y1,x2,y2]
        picture = canvas.create_rectangle(coords, fill='red', outline='red',tag=self.tag)
        return picture
    pass

class vertex: # defines a vertex
    def __init__(self,x,y):
        self.x=x
        self.y=y

class pixel: # defines a square with x1,y1,x2,y2 coordinates and its fill
    def __init__(self,coords,fill):
        self.coords = coords
        self.fill = fill
    
        
class spriteObject: # defines single sprite
    def __init__(self,name,spriteElements,spriteElementsData):
        self.name = name
        self.spriteElements = spriteElements # here are "pixels", only their ID on the canvas
        self.spriteElementsData = spriteElementsData #here is their data i.e.
        # ['coords']==[x1..y2] and ['fill']=='color'



##class GUI:
##
##    def __init__ (self,resx,resy,apptype):
##        
##        # basical constants and variables V
##        self.type = apptype
##        
##        self.TERRAINS = ['plain','stones','sand','water','sea','ocean']
##        self.COLORS = ['#50aa50','#808080','#efed50','#8080ff','#6060ff','#101080']#,'','','','']
##        self.TERRA2COLOR = dict(zip(self.TERRAINS, self.COLORS))
##
##        self.sprites = [] # here all sprites are placed
##        
##        # graphical constants V
##        
##        self.root = Tk()
##
##        self.screenFrame = Frame(self.root)
##        self.canvas = Canvas(self.screenFrame,width = resx, height = resy)
##        self.textOut = Label(self.screenFrame)
##
##        self.screenFrame.grid(column=0,row=0)
##
##
##        self.canvas.grid(column = 0,row = 0)
##        self.textOut.grid(column = 0,row = 1)
##        
##        self.controlsFrame = Frame(self.root)
##        self.controlsFrame.grid(column=0,row=1)
##
##            
##    def start(self):
##        self.root.mainloop()
##
##    def importSettings(self):
##        setsfile = open (self.type+'.settings','r')
##        settings = dict()
##        line = setsfile.readline()
##        while line!="":
##            values=line.split('=')
##            settings[values[0]] = values[1].replace('\n','')
##            line = setsfile.readline()
##        self.settings = settings
##
##    def exportSettings(self,name):
##        settsfile = open (self.type+'.settings','w')
##        for i in self.settings:
##            line = i+'='+str(self.settings[i])+'\n'
##            settsfile.write(line)
##                    
##    pass
##
##
##
