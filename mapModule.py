# MapModule - Apricot v.0.1-alpha
from classModule import *

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

