from cstuff import *

initfile=open ('initGE.conf','r')
line = initfile.readline()
line=line.split('=')
#mode in the first line
mode=line[1].replace('\n','')
if mode=='0':
	mode='console'
	from cstuff import *
elif mode=='1':
	mode='graphical'
	from gstuff import *
initfile.close()
	
class GameEngineUti:
	ExitSignal=0
	UnitList=[]

	def __init__(self):
		self.LoadParams()
		self.InitStuff()
		
	def LoadParams(self):
		try:
			initfile=open ('initGE.conf','r')
			line = initfile.readline()
			while line!='':
				line=line.split('=')
				name=line[0]
				val=line[1].replace('\n','')
				if val.isdigit():
					val=int(val)
				setattr(self,name,val)
				#print (line,name,val,self.PARAMETERS)
				line = initfile.readline()
			initfile.close()
		except FileNotFoundError:
			print ('File "initGE.conf" Not Found.')
			return 1

	def InitStuff(self):
		InitScreen(self)
		self.Players=[]
		for i in range(self.PlayersCount):
			self.Players.append(csm.Player(Name='Player '+str(i)))
		self.CurPlayer=self.Players[0]
		self.CurMap=csm.Map('menu') # menu map is an flat map which 
		self.CurMap.LoadMap()

		self.UnitList=self.Players

		self.Story=csm.Story('story')
		self.Story.LoadStory()
		print(self.Story.Chapters)
#
#	End of Initialization Section 
#
########################################################################
########################################################################
#
#	Begin of Main Stuff Section
#
	def Main(self):
		if self.mode=='console':
			self.cMain()
		elif self.mode=='graphical':
			self.gMain()
 
	def cMain(self):  # Mainloop for consolemode
		UpdateScreen(self)
		while self.ExitSignal!=1:
			action=list(input('Action: ').split())
			if action!='':
				if action[0] in MiscFunc:
					self.MiscRunner(action)
				elif action[0] in GeneralFunc:
					self.GeneralRunner(action)
				elif action[0] in MoveFunc:
					self.MoveRunner(action)
				UpdateScreen(self)

	def SwitchPlayer(self,player=''):
		if player=='':
			player=self.Players.index(self.CurPlayer)+1
		if player>=len(self.Players):
			player=0
		self.CurPlayer=self.Players[player]

	def MiscRunner(self,action):
		if action[0]=='menu':
			DrawTextMenu(self,action[0])

	def GeneralRunner(self,action):
		DrawTextMenu(self,action[0])

	def MoveRunner(self,action):
		print(action)
		if action[0]=='move':
			action=list(action[1])
			print (action)
		for i in action:
			MoveVector=[0,0]
			if self.CurPlayer.Energy<=0:
				self.SwitchPlayer()
				UpdateScreen(self)
				break
			if i in list('nNсС'):
				MoveVector=[0,-1]
			elif i in list('sSюЮ'):
				MoveVector=[0,1]
			elif i in list('wWзЗ'):
				MoveVector=[-1,0]
			elif i in list('eEвВ'):
				MoveVector=[1,0]
			self.Mover(MoveVector)
			print (i,MoveVector)

	def CheckMoveAbility(self):
		if self.CurPlayer-self.NextCell.EnergyCost>=0:
			return 1
		else :
			return 0

	def ConsumeEnergy(self,CurPlayer,EnergyCost):
		CurPlayer.Energy-=EnergyCost

	def Mover(self,vector):
		NewX=self.CurPlayer.PosX+vector[0]
		NewY=self.CurPlayer.PosY+vector[1]
		self.NextCell = self.CurMap.CellsData[NewX][NewY]
		if 'crossable' in self.NextCell.Tags:
			AbleToMove = self.CheckMoveAbility()
			if AbleToMove==1:
				self.ConsumeEnergy(self.CurPlayer,self.NextCell.EnergyCost)
				self.CurPlayer.PosX= NewX
				self.CurPlayer.PosY= NewY
				if self.NextCell.Scriptstr!='':
					SIN(self,self.NextCell.Scriptstr)
		
		UpdateScreen(self)

########################################################################
#
#	Begin Subsection "SIN and related stuff"
#
#		# script example:
#		# v:var=10;tp 0 10 10;v:
#
	def SIN(self,scriptstr):
		OperationArray = scriptstr.split(';')
		while len(OperationArray)>0:
			operation=OperationArray[0].split(':')
			optype = operation[0].replace(' ','')
			operation = operation[1]
			if optype=='v':
				self.SetVariable(operation)
			elif optype=='m':
				operation = operation.split() # MAP_NAME [PLAYER PLAYER_NEWX PLAYER_NEWY]
				self.CurMap.Name=operation[0]
				self.CurMap.LoadMap() # TODO: Map pool
				self.TeleportPlayer(operation[1:])
			elif optype=='s':
				if self.StoryChecker(operation):
					self.StoryRunner(operation)
			elif optype=='tp':
				self.TeleportPlayer(operation.split())
			OperationArray=OperationArray[1:]#print('May be here we are fucking up?') YES! (I've forgotten about cutting OA)
			
	def SetVariable(self,operation):
		# Syntaxis :
		# var = expression
		# Example
		# attr.innerAttr = otherAttr + someValue
		operation = operation.replace(' ','') # normalizing expression
		operation = operation.split('=')
		variable = operation[0]
		val = self.ExpressionParser(operation[1])
		self.SetInnerAttr(variable,val)
		
	def ExpressionParser(self,exp): 
		# EP is needed to be upgraded (to set strings and other things)
		if exp.find('+')!=-1:
			op='+'
		elif exp.find('-')!=-1:
			op='-'
		elif exp.find('*')!=-1:
			op='*'
		elif exp.find('/')!=-1:
			op='/'
		exp=exp.split(op)
		if exp[0][0].isdigit():
			val0=int(exp[0])
		else :
			val0=self.GetInnerAttr(exp[0])
		if exp[1][0].isdigit():
			val1=int(exp[1])
		else :
			val1=self.GetInnerAttr(exp[1])
		cases={'+':val0+val1,'-':val0-val1,'*':val0*val1,'/':val0/val1}
		out=cases[op]
		return out
		
	def SetInnerAttr(self,attr,val):
		attr=attr.split('.')
		p=self
		lim=100
		c=0
		for i in attr[:-1]: # the last attr is used to set value
			print('IN SetATTR',p,i)
			p=getattr(p,i) # getting inner attributes
			if c>lim:
				print('too many iterations. setting',i,'in',p,'to',val)
				break
			c+=1
		setattr(p,attr[-1],val) # setting last attr to value
		
	def GetInnerAttr(self,attr):
		attr=attr.split('.')
		p=self
		for i in attr:	# going into attribute 
			#print(p,i)	# |_which in turn has another attr-s and etc.			
			p=getattr(p,i) # getting inner attribute
		return p # returning value  of the last attr-e

	def StoryChecker(self,chapter): #FIXME: there conditions should be checked
		return True 				#<----------------------------------------

	def StoryRunner(self,chapter):
		DrawTextMenu(self,chapter)
	
	def TeleportPlayer(self,operation):
		# operation format
		# PLAYER_NUM NEW_POS_X NEW_POS_Y
		if operation [0]=='cur':
			operation[0]=self.CurPlayer.Number
		self.Players[int(operation[0])].PosX=int(operation[1])
		self.Players[int(operation[0])].PosY=int(operation[2])
#
#	End Subsection SIN and related stuff
#
########################################################################
#Begin Graphical supersection 
	def gMain(self):
		null=0
#TODO: graphics
