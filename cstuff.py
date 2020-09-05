import commonstuffmodule as csm
from ccmodule import *
########################################################################
# Comments:
# ooc_<CLASS NAME> is equal to "object of <CLASS NAME> class"
# ScreenData is a 80x23 matrix (STD terminal (80x24) minus 1 line)  
#
#
########################################################################

def PrintScreen(screen): 
	# screen is ooc_GameEngineUti.ScreenData matrix 80x23
	s=''
	for i in range(len(screen)):
		for j in range(len(screen[i])):
			s+=screen[i][j]
		s+='\n'
	print(s[:-2])

def GenerateScreen(): # generates ScreenData matrix 80x23
	ScreenData = []
	for i in range(23): # "Y axis" in standard terminal 
		ScreenData.append([])
		for j in range(80): # X axis ...
			ScreenData[i].append(' ')
	return ScreenData

def InitScreen(ooc_GameEngineUti):
	ooc_GameEngineUti.ScreenData = GenerateScreen()
	PrintScreen(ooc_GameEngineUti.ScreenData)
	
########################################################################
# Composer Stuff Section	|
#							V
def InsertString(InString,BeginPos,ListForOut):
	c=0 #counter
	print('inserting ', InString)
	for i in InString:
		ListForOut[BeginPos+c]=i
		#print(ListForOut,'\n\n',i,BeginPos)
		c+=1
	return ListForOut
	
def Placer(InString,ListForOut, Where='left'): # InString - string, 
# Where - value of {'left', 'center', 'right'}
# ListForOut - a list which is returned (a part of ScreenData)
	if Where == 'right':
		BeginPos = len(ListForOut)-(1+len(InString))
	elif Where == 'center':
		BeginPos = (len(ListForOut)-len(InString))//2 
	else: # if Where not in ['right','center'] falling back to 'left'
		BeginPos=0
	ListForOut = InsertString(InString,BeginPos,ListForOut)
	return ListForOut

def Composer(ooc_GameEngineUti,Map):
	NewSD = GenerateScreen() # New ScreenData Array
	for i in UpperTopBar:
		InString= i.split('.')[-1]+': '+str(ooc_GameEngineUti.GetInnerAttr(i))
		Where= UpperTopBar[i]
		NewSD[0]= Placer(InString,NewSD[0],Where)
	for i in LowerTopBar:
		InString= i.split('.')[-1]+': '+str(ooc_GameEngineUti.GetInnerAttr(i))
		Where= LowerTopBar[i]
		NewSD[1]= Placer(InString,NewSD[1],Where)
	NewSD[2:23]=Map[:]
	#print("in Composer",len(NewSD))
	ooc_GameEngineUti.ScreenData=NewSD[:] # returning ScreenData

def UpdateScreen(ooc_GameEngineUti): #TODO
	CurMapText = csm.GenerateMatrix(80,21)
	for i in range(21):
		for j in range(80):
			#print("in UpdateScreen",i,j)
			CurMapText[i][j]=ooc_GameEngineUti.CurMap.CellsData[j][i].Symbol
	Composer(ooc_GameEngineUti,CurMapText)
	PrintScreen(ooc_GameEngineUti.ScreenData)

def DrawTextMenu(ooc_GameEngineUti,menu):
	action=""
	MainText=ooc_GameEngineUti.Story.Chapters[menu].MainText
	Answers=ooc_GameEngineUti.Story.Chapters[menu].Answers
	Options=ooc_GameEngineUti.Story.Chapters[menu].Options
	Results=ooc_GameEngineUti.Story.Chapters[menu].Results
	TextToDisplay=MainText+[' '*80]+Options # empty string in between 
	#print("in DrawTextMenu",TextToDisplay)
	TextMap=csm.GenerateMatrix(80,21) # generating "map"
	PrintScreen(TextMap)
	for i in range(len(TextToDisplay)):
		#print('before',TextMap[i],TextToDisplay[i])
		#PrintScreen(TextMap)
		TextMap[i]=Placer(TextToDisplay[i],TextMap[i])
		#print('after',TextMap[i],TextToDisplay[i],'\noutputing ---->')
		#PrintScreen(TextMap)
	#PrintScreen(TextMap)
	Composer(ooc_GameEngineUti,TextMap)
	while action not in Answers:
		PrintScreen(ooc_GameEngineUti.ScreenData)
		action = input ('Action: ')
	scriptstr=Results[Answers.index(action)]
	ooc_GameEngineUti.SIN(scriptstr) # 
	# Use "s:MENU_NAME" in results to make menus
