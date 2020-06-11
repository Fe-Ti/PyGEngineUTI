# classes:

# for game logic
class vector:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
        
# for graphics

from tkinter import *

class GUI:

    def __init__ (self,resx,resy):
        
        # basical constants
        
        self.TERRAINS = ['plain','stones','sand','water','sea','ocean']
        self.COLORS = ['#50aa50','#808080','#efed50','#8080ff','#6060ff','#101080']#,'','','','']
        self.TERRA2COLOR = dict(zip(self.TERRAINS, self.COLORS))
        
        # graphical constants
        
        self.root = Tk()

        self.screenFrame = Frame(root)
        self.canvas = Canvas(self.screenFrame,width = resx, heigth = resy)
        self.textOut = Label(self.screenFrame)

        self.canvas.grid(column = 0,row = 0)
        self.textOut.grid(column = 0,row = 1)
        
        self.contolsFrame = Frame(root)

        self.conrolsFrame.
    pass

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

class spriteElement: # describes single color object in the sprite
    def __init__(self,vertexes,Fill):
        self.Fill=Fill
        self.vertexes=vertexes
        

class spriteObject: # describes single sprite
    def __init__(self,spriteElements):
        self.spriteElements=spriteElements
        

class mapObject:
    def __init__(self,sprite,square,tags):
        self.sprite=sprite
        self.x=square[0]
        self.y=y
        self.tags=tags
