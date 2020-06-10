# Apricot sprite editor

# std lib-s
from tkinter import *

# custom lib-s
from classModule import *



colors=['#009933','blue','green','gray','white','#bbaaaa','brown',]
spriteElements=[]
vertexes=[]
vv=[]
visualrepresentation=[]


Fill=''
root = Tk()
##width = 128
##height = 128
pixsize = 10
reso=128

canvas = Canvas (root, width=reso,height=reso, bg='#dddddd')#describe canvas
canvas.grid (column=0,row=0)
##scrolly = Scrollbar(root, orient=VERTICAL,command=canvas.yview)
##scrollx = Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)
##canvas.config(yscrollcommand=scrolly.set)
##canvas.config(xscrollcommand=scrollx.set)
##scrolly.grid (column=1,row=0, sticky=(N,S))
##scrollx.grid (column=0,row=1, sticky=(W,E))

controls = Frame(root) #frame where controls are placed, which are described below 
controls.grid (column=0,row=2)

createsprite = Button(controls, text='create new sprite')
createsprite.grid (column=0,row=0)

save = Button(controls, text='save')
save.grid (column=10,row=1)

load = Button(controls,text='load')
load.grid(column=10,row=2)
Fill = Listbox(controls, height=len(colors))
for i in colors:
    Fill.insert(END,i)
Fill.grid (column=2,row=3)

apply = Button (controls, text='apply object')
apply.grid(column=3,row=0)

qForm = Entry (controls)
qForm.grid (column=9, row=0)

name = Entry (controls)
name.grid (column=9, row=1)

prex=-1
prey=-1
#q=

def createVertex(event): # creates 1 vertex
    global prex, prey, qForm
    x=canvas.canvasx(event.x)
    y=canvas.canvasy(event.y)
    print (canvas.canvasx(event.x), '  ', canvas.canvasy(event.y))
    vv.append(canvas.create_rectangle ([x-0.5,y-0.5,x+0.5,y-0.5], outline = 'yellow', tag= "vertex")) #(actual size of this is 2x2 pixels)
    vertexes.append(vertex(x,y))
    prex=x
    prey=y
        
def createVertexs(event): # creates several vertexes, while cursor is moving
    global prex, prey
    q=int(qForm.get())
    x=canvas.canvasx(event.x)
    y=canvas.canvasy(event.y)
    if (x-prex)**2+(y-prey)**2>=q : # do not clone vertexes
        print (canvas.canvasx(event.x), '  ', canvas.canvasy(event.y))
        vv.append(canvas.create_rectangle ([x-0.5,y-0.5,x+0.5,y-0.5], outline = 'yellow', tag= "vertex")) #(actual size of this is 2x2 pixels)
        vertexes.append(vertex(x,y))
        prex=x
        prey=y
    
def createNewsprite(event): # deletes all objects
    global vertexes
    vertexes=[]
    canvas.delete("all")
    spriteElements=[]

def applyNewObj(event):
    global spriteElements, vertexes, Fill, visualrepresentation
    fillment=str(colors[Fill.curselection()[0]])
    print (fillment)
##    tags = tagsForm.get()
##    tags = tags.split()
    current=spriteElement(vertexes,fillment) # add object to the object-propeties index

    v=[] 
    for i in range (len(vertexes)):
        v.append(vertexes[i].x)
        v.append(vertexes[i].y)
    visualrepresentation.append(canvas.create_polygon(v, fill=fillment)) #, tag=tags)) #draw objects in canvas

    spriteElements.append(current) # add cur. obj. to list of all spriteElements
    vertexes=[] # reset vertexes
    canvas.delete('vertex')
    print (spriteElements[-1].vertexes)
    
def savesprite (event): #saves object-properties index to file in .amef format 
    global name,spriteElements
    print (name.get())

    spriteFile = open (name.get()+'.asef','w')
    for i in range(len(spriteElements)):
        spriteFile.write ('#/\n')
        spriteFile.write ('vertex/\n')
        vertexes=""
        for j in range(len(spriteElements[i].vertexes)):
            vertexes+=str(spriteElements[i].vertexes[j].x)+' '+str(spriteElements[i].vertexes[j].y)+" "
            if j%32 == 0:
                spriteFile.write (vertexes+'\n')
                vertexes=''
        spriteFile.write (vertexes+'\n')
        spriteFile.write ('/vertex\n')
        spriteFile.write ('Fill/\n')
        spriteFile.write(str(spriteElements[i].Fill)+'\n')
        spriteFile.write ('/Fill\n')
##        spriteFile.write ('tags/\n')
##        tags=''
##        for j in spriteElements[i].tags:
##            tags += (j+' ')
##        spriteFile.write(tags+'\n')
##        spriteFile.write ('/tags\n')        
        spriteFile.write ('/#\n')


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

        spriteElements.append(spriteElement(vertexes,Fill)) #,tags))
        line = spritefile.readline()
        
    return spriteElements

def refreshsprite(spriteElements): # deletes everything and draws new objects on canvas from index
    
    canvas.delete('all')
    
    for i in range(len(spriteElements)):
        vertexes=[]
        for j in range(len(spriteElements[i].vertexes)):
            vertexes.append(spriteElements[i].vertexes[j].x)
            vertexes.append(spriteElements[i].vertexes[j].y)
        color = spriteElements[i].Fill
        #tags = spriteElements[i].tags

        canvas.create_polygon(vertexes,fill=color)#,tag=tags)

def loadsprite(event): # calls object loader and then refresh function (which draws new objects from index)
    global name
    spritename = (name.get())
    SE = spriteLoader(spritename)
    refreshsprite(SE)

canvas.bind ('<B1-Motion>',createVertexs) # binding things with functions
canvas.bind ('<Button-1>',createVertex)

createsprite.bind('<Button>',createNewsprite)
apply.bind('<Button>',applyNewObj)
save.bind ('<Button>',savesprite)
load.bind ('<Button>',loadsprite)
root.mainloop() # starting application
