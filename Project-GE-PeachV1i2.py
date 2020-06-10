# Game engine Peach version 1 idea 2
#
# standart python3 modules
from tkinter import *
from time import *

# my modules
from classModule import *
from mapModule import *

print ('start')


c=0 #reseting counter
settings=dict()

def importSettings():
    global settings
###section for debug### there should be a data loader 
    resolx=800
    resoly=800
    pixsize=2
    goN='Up'
    goS='Down'
    goE='Right'
    goW='Left'
    gamevelocity=5
    saveSettings='s'
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
    settings['saveSettings'] = saveSettings
importSettings()

#graphical
root = Tk()
canvas = Canvas (root, width=settings['resolx'], height=settings['resoly'])
canvas.grid()
player = unit(50,50,'player')
def drawUnit(canvas,unit):
    #global unit
    x1 = unit.x-0.5*settings['pixsize']
    y1 = unit.y-0.5*settings['pixsize']
    x2 = unit.x+0.5*settings['pixsize']
    y2 = unit.y+0.5*settings['pixsize']
    coords=[x1,y1,x2,y2]
    unit.picture = canvas.create_rectangle(coords, fill='red', outline='red',tag=unit.tag)

mapObjects=[]
#types=['grass','water','forest','mountines','snow','town']
colors=['#009933','blue','green','gray','white','#bbaaaa']

#end of init section for global variables


# begin section of functions, which are diretly connected with event processing
def exportSettings(settings):
    
    settsfile = open ('settings.seed','w')
    for i in settings:
        line = i+'='+str(settings[i])+'\n'
        settsfile.write(line)
    
def keyProcessor(event): #processes key presses, transforming raw data into easy to read and work bits ('brother' of a buttonProcessor)
    action=str(event.keysym)
    print(action)
    coordinator(settings,action)
def buttonProcessor(event): #processes button presses, transforming raw data into easy to read and work bits ('brother' of a keyProcessor)
    action='B'+str(event.num)
    print(action)
    coordinator(settings,action)

def coordinator(settings,action): # coordinates movements and actions (handles MovementControls hardbinded with settings)
    MovementControls = { 
        settings['goS'] : [0,1], 
        settings['goN'] : [0,-1],
        settings['goE'] : [1,0],
        settings['goW'] : [-1,0],
        }
    if action in MovementControls:
        vec = vector(MovementControls.get(action,0)[0],MovementControls.get(action,0)[1]) # get direction coordinates for the vector
        print (vec.x,' ',vec.y)
        pointMover(vec)
    elif action == settings['saveSettings']:
        exportSettings(settings)
# end section of functions, which are diretly connected with event processing


	

root.bind("<KeyRelease>",keyProcessor)
root.bind("<ButtonPress>",buttonProcessor)


MO = mapObjectsLoader('test')
refreshMap(MO)
root.mainloop()

