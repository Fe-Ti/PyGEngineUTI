# 
# 

# standart python3 modules

# my modules
from tkAddon import * #FIXME#

from GUIclassModule import *

class ME (GUI):
	def __init__(self):
		super().__init__('ME')
		
		self.t_reso = self.INITPARAMS['t_reso']
		
		self.NLSFrame = Frame(self.controlsFrame,bg='green')
		self.NLSFrame.grid(column=0,row=0)
		
		self.newMapB = Button(self.NLSFrame, text='New map')
		self.newMapB.pack(fill=X)
		self.loadMapB = Button(self.NLSFrame, text='Load map')
		self.loadMapB.pack(fill=X)
		self.saveMapB = Button(self.NLSFrame, text='Save map')
		self.saveMapB.pack(fill=X)
		self.mapName = Entry(self.NLSFrame)
		self.mapName.pack(fill=X)
		
		
		
		self.TFrame = Frame(self.controlsFrame,bg='red')
		self.TFrame.grid(column=1,row=0)
		
		self.terrainsListBox = scrListBox(self.TFrame,self.TERRAINS)# look into tkAddon.py for details
		self.terrainsListBox.packMe(LEFT,BOTH) 						##
		
		self.terrainTagsL = Label(self.TFrame, text='Terrain tags (space to split):')
		self.terrainTagsL.pack(side=TOP)
		self.terrainTags = Entry(self.TFrame)
		self.terrainTags.pack(side=TOP)
		
		self.Tsframe = Frame(self.TFrame, bg='orange')
		self.Tsframe.pack(side=TOP)
		
		# Tsframe contents begin
		self.prevTerrain = Button (self.Tsframe,text='<')
		self.currTerrain = Label (self.Tsframe,text='')
		self.nextTerrain = Button (self.Tsframe,text='>')
		self.prevTerrain.grid(column=0,row=0)
		self.currTerrain.grid(column=1,row=0)
		self.nextTerrain.grid(column=2,row=0)
		self.addTerrainB = Button (self.Tsframe, text='+')
		self.addTerrainB.grid(column=3,row=0)
		# Tsframe contents end
		
		
		
		self.OFrame = Frame(self.controlsFrame,bg='blue')
		self.OFrame.grid(column=2,row=0)
		
		
		
		self.BFrame = Frame(self.controlsFrame,bg='purple')
		self.BFrame.grid(column=3,row=0)
		
		
		
	def startME(self):
		self.root.mainloop()
		
