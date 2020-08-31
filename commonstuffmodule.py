########################################################################
#
#	Begin Classes Section
#
########################################################################
##
##	Map Subsection
##
########################################################################

class Unit:
	PosX=0
	PosY=0
	Name=''
	Symbol=''
	HP=100
	Energy=100
	def __init__(self,PosX=0,PosY=0,Name='',Symbol='',HP=100,Energy=100):
		self.PosX=PosX
		self.PosY=PosY
		self.Name=Name
		self.Symbol=Symbol
		self.HP=HP
		self.Energy=Energy

class Player(Unit):#TODO
	Number=''
	pass

class CellObject:
	Name=''
	Tags=[]
	Symbol=''
	#Image=''
	def __init__(self, Name='', Tags=[], Symbol=''):
		self.Name=Name
		self.Tags=Tags[:]
		self.Symbol=Symbol

class Cell:
	CellName='' # 
	Symbol='' # is used if there is no image for terrain 
	Object='' 
	Tags=[]
	EnergyCost=0
	Scriptstr=''
	
	def __init__(self,CellName='',Symbol='',Object='',Tags=[],Scriptstr='',EnergyCost=0):
		self.CellName=CellName
		self.Symbol=Symbol # is used if there is no image for terrain 
		self.Object=Object
		self.Tags=Tags[:]
		self.Scriptstr=Scriptstr
		self.EnergyCost=EnergyCost

class Map:
	Name=''
	CellsData=[]
	ObjectList=[]
	
	def __init__(self,Name=''):
		self.Name=Name
		for i in range(80):
			self.CellsData.append([])
			for l in range(21):
				self.CellsData[i].append(Cell(Symbol="M"))
		
	def LoadMap(self):
		print ("LOADING MAP...")
########################################################################
##
##	End of Map Subsection
##
########################################################################
########################################################################
##
##	Story Subsection
##
########################################################################
class Chapter:#TODO
	MainText=[]
	Answers=[]
	Options=[]
	Results=[]
	def __init__(self,MainText=[],Options=[],Answers=[],Results=[]):
		self.MainText=MainText[:]
		self.Answers=Answers[:]
		self.Options=Options[:]
		self.Results=Results[:]
	

class Story:
	Chapters=dict()
	
	def __init__(self,Name=''):
		self.Name=Name
		
	def LoadStory(self):
		print ("LOADING STORY...")
		###TESTING###
		self.Chapters={'menu':Chapter(['TEST TEST','TEST TEST'],['a) +10 Energy'],['a'],['v: CurPlayer.Energy = CurPlayer.Energy + 10'])}
		
		
		#############
########################################################################
##
##	End of Story Subsection
##
########################################################################
########################################################################
#
#	End Classes Section
#
########################################################################
########################################################################
#	Begin General Functions
########################################################################
def GenerateMatrix(x,y):
	matrix=[]
	for i in range(y):
		matrix.append([])
		for j in range(x):
			matrix[i].append(' ')
			print (len(matrix),'@@',len(matrix[i]))
	return matrix
########################################################################
#	End General
########################################################################
