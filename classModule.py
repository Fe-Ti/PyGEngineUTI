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

class spriteElement: # describes single color object in the sprite
    def __init__(self,vertexes,Fill):
        self.Fill=Fill
        self.vertexes=vertexes
        

class spriteObject: # describes single sprite
    def __init__(self,spriteElements):
        self.spriteElements=spriteElements
        

class mapObject:
    def __init__(self,sprite,x,y,tags):
        self.sprite=sprite
        self.x=x
        self.y=y
        self.tags=tags
