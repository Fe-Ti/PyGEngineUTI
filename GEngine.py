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


app=GUI(640,640,'GE')
app.importSettings()


units=[]
units.append(unit(50,50,'player'))
pp = units[0].drawUnit(app.canvas,int(app.settings['pixsize']))

mapObjects=[]
#types=['grass','water','forest','mountines','snow','town']
colors=['#009933','blue','green','gray','white','#bbaaaa']





app.start()









#end of init section for global variables


# begin section of functions, which are diretly connected with event processing

##def keyProcessor(event): #processes key presses, transforming raw data into easy to read and work bits ('brother' of a buttonProcessor)
##    action=str(event.keysym)
##    print(action)
##    coordinator(settings,action)
##def buttonProcessor(event): #processes button presses, transforming raw data into easy to read and work bits ('brother' of a keyProcessor)
##    action='B'+str(event.num)
##    print(action)
##    coordinator(settings,action)
##
##def coordinator(settings,action): # coordinates movements and actions (handles MovementControls hardbinded with settings)
##    MovementControls = { 
##        settings['goS'] : [0,1], 
##        settings['goN'] : [0,-1],
##        settings['goE'] : [1,0],
##        settings['goW'] : [-1,0],
##        }
##    if action in MovementControls:
##        vec = vector(MovementControls.get(action,0)[0],MovementControls.get(action,0)[1]) # get direction coordinates for the vector
##        print (vec.x,' ',vec.y)
##        pointMover(vec)
##    elif action == settings['saveSettings']:
##        exportSettings(settings)
# end section of functions, which are diretly connected with event processing
