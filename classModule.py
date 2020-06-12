# classes:

# for game logic
class vector:
    def __init__ (self,x,y):
        self.x=x
        self.y=y

# for graphics

from tkinter import *

class GUI:

    def __init__ (self,resx,resy,apptype):
        
        # basical constants
        self.type = apptype
        
        self.TERRAINS = ['plain','stones','sand','water','sea','ocean']
        self.COLORS = ['#50aa50','#808080','#efed50','#8080ff','#6060ff','#101080']#,'','','','']
        self.TERRA2COLOR = dict(zip(self.TERRAINS, self.COLORS))
        
        # graphical constants
        
        self.root = Tk()

        self.screenFrame = Frame(self.root)
        self.canvas = Canvas(self.screenFrame,width = resx, height = resy)
        self.textOut = Label(self.screenFrame)

        self.screenFrame.grid(column=0,row=0)


        self.canvas.grid(column = 0,row = 0)
        self.textOut.grid(column = 0,row = 1)
        
        self.controlsFrame = Frame(self.root)

        self.controlsFrame.grid(column=0,row=1)
        
        
        def keyProcessor(event): #processes key presses, transforming raw data into easy to read and work bits ('brother' of a buttonProcessor)
            print(event)
            action=str(event.keysym)
            print(action)
            coordinator(self.settings,action)
            
        def buttonProcessor(event): #processes button presses, transforming raw data into easy to read and work bits ('brother' of a keyProcessor)
            print(event)
            action='B'+str(event.num)
            print(action)
            coordinator(self.settings,action)
        self.root.bind("<KeyRelease>",keyProcessor)
        self.root.bind("<ButtonPress>",buttonProcessor)
            
        def coordinator(settings,action):
            null=0
            
    def start(self):
        self.root.mainloop()

    def importSettings(self):
        setsfile = open (self.type+'.settings','r')
        settings = dict()
        line = setsfile.readline()
        while line!="":
            values=line.split('=')
            settings[values[0]] = values[1].replace('\n','')
            line = setsfile.readline()
        self.settings = settings

    def exportSettings(self,name):
        settsfile = open (self.type+'.settings','w')
        for i in self.settings:
            line = i+'='+str(self.settings[i])+'\n'
            settsfile.write(line)
                    
    pass

class unit:
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

class vertex:
    def __init__(self,x,y):
        self.x=x
        self.y=y


class spriteObject: # describes single sprite
    def __init__(self,spriteElements):
        self.spriteElements=spriteElements
        

class mapObject:
    def __init__(self,sprite,position,tags):
        self.sprite=sprite
        self.x=position[0]
        self.y=position[1]
        self.tags=tags
