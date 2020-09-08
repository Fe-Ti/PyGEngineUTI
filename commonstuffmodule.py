import json
########################################################################
#
#	Begin Classes Section
#
########################################################################
########################################################################
####
####	Map Subsection
####
########################################################################
MapDirPointer='maps/'
StoryDirPointer='story/'

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
		# ~ mapfile= open (MapDirPointer+self.Name,'r')
		# ~ line=mapfile.readline()
########################################################################
####
####	End of Map Subsection
####
########################################################################
########################################################################
####
####	Story Subsection
####
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
	Name=''
	
	def __init__(self,Name='',):
		self.Name=Name
		
	def LoadStory(self):
		print("Loading Story...")
		print("Loading RawData...")
		storyfile = open(StoryDirPointer+self.Name+'.json','r')
		RawData = storyfile.read()
		storyfile.close()
		print("Loaded RawData [OK]")
		print("Processing RawData...")
		ChaptersDict = json.loads(RawData)
		self.Chapters = dict()
		print("Processed RawData [OK]")
		for i in ChaptersDict:
			print("Processing Chapter",i,"...")
			self.Chapters[i] = Chapter(ChaptersDict[i]['MainText'],ChaptersDict[i]['Options'],ChaptersDict[i]['Answers'],ChaptersDict[i]['Results'])
			print("Processed Chapter",i,"[OK]")
		print("Loaded Story [OK]")
		
		###TESTING###
		# ~ self.Chapters={
		# ~ 'menu':Chapter(['TEST menu','Input "a"'],['a) +10 Energy'],['a'],['v: CurPlayer.Energy = CurPlayer.Energy + 10;s:menu1']),
		# ~ 'menu1':Chapter(['TEST menu1','Input "b" to go back'],['a) +10 Energy','b) go to menu'],['a','b'],['v: CurPlayer.Energy = CurPlayer.Energy + 10','s:menu'])
		# ~ }
		
		
		#############
########################################################################
####
####	End of Story Subsection
####
########################################################################
########################################################################
#
#	End Classes Section
#
########################################################################

########################################################################
#	Begin General Functions Section
########################################################################

def GenerateMatrix(x,y):
	matrix=[]
	for i in range(y):
		matrix.append([])
		for j in range(x):
			matrix[i].append(' ')
			#print (len(matrix),'@@',len(matrix[i]))
	return matrix

########################################################################
#	End General Functions Section
########################################################################
