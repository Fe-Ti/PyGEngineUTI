# 
# 

# standart python3 modules

# my modules
from tkAddon import * #FIXME#

import objectLists as OL

from GUIclassModule import *

class ME (GUI):
	def __init__(self):
		super().__init__('ME')
		
		self.t_reso = self.INITPARAMS['t_reso']
		
		# BEGIN New,Load,Save frame
		def initializeNLSFrame(self):	
			
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
			# END New,Load,Save frame	
		initializeNLSFrame(self)
		
		# BEGIN terrain manipulation frame 
		def initializeTFrame(self):
			self.TFrame = Frame(self.controlsFrame,bg='red')
			self.TFrame.grid(column=1,row=0)
			
			self.terrainsListBox = scrListBox(self.TFrame,self.TERRAINS)# look into tkAddon.py for details
			self.terrainsListBox.packMe(LEFT,BOTH) 						##
			
			self.terrainTagsL = Label(self.TFrame, text='Terrain tags (space to split):')
			self.terrainTagsL.pack(side=TOP,fill=X)
			self.terrainTags = Entry(self.TFrame)
			self.terrainTags.pack(side=TOP,fill=X)
			
			def initializeTerrainSelectorF(self):
				self.TerrainSelectorFL = Label(self.TFrame, text='Terrain node:')
				self.TerrainSelectorFL.pack(side=TOP,fill=X)
				self.TerrainSelectorF = Frame(self.TFrame, bg='orange')
				self.TerrainSelectorF.pack(side=TOP)
				
				# TerrainSelectorF contents begin
				self.prevTerrain = Button (self.TerrainSelectorF,text='<')
				self.currTerrain = Label (self.TerrainSelectorF,text='')
				self.nextTerrain = Button (self.TerrainSelectorF,text='>')
				self.prevTerrain.grid(column=0,row=0)
				self.currTerrain.grid(column=1,row=0)
				self.nextTerrain.grid(column=2,row=0)
				self.addTerrainB = Button (self.TerrainSelectorF, text='+')
				self.addTerrainB.grid(column=3,row=0)
				# TerrainSelectorF contents end
			initializeTerrainSelectorF(self)
			
			self.CurrentTerrainTagsL = Label(self.TFrame)
			self.CurrentTerrainTagsL.pack()
			# END terrain manipulation frame
		initializeTFrame(self)
		
		# BEGIN object manipulation frame
		def initializeOFrame(self):
			self.OFrame = Frame(self.controlsFrame,bg='blue')
			self.OFrame.grid(column=2,row=0)
			
			self.objectPickerL = Label(self.OFrame,text='Object:')
			self.objectPickerL.pack(side=TOP,fill=X) 
			self.objectPickerE = Entry(self.OFrame)
			self.objectPickerE.pack(side=TOP,fill=X)
			self.objectPickerLB = scrListBox(self.OFrame, OL.AOL_t)
			self.objectPickerLB.packMe(LEFT,Y)
			
			def initializeCurrentObjectPropertiesF(self):
				self.CurrentObjectPropertiesF=Frame(self.OFrame)
				self.CurrentObjectPropertiesF.pack()
				
				self.COPnameL = Label (self.CurrentObjectPropertiesF, text='OBJECT name:') 
				self.COPname = Entry (self.CurrentObjectPropertiesF)
				self.COPtagsL = Label (self.CurrentObjectPropertiesF, text='OBJECT tags:')
				self.COPtags = Entry (self.CurrentObjectPropertiesF)
				self.COPstoryChaptersL = Label (self.CurrentObjectPropertiesF, text='Story chapters\nconnected to OBJECT:')
				self.COPstoryChapters = Entry (self.CurrentObjectPropertiesF)
				
				self.COPnameL.pack()
				self.COPname.pack()
				self.COPtagsL.pack()
				self.COPtags.pack()
				self.COPstoryChaptersL.pack()
				self.COPstoryChapters.pack()
				
			initializeCurrentObjectPropertiesF(self)
			# END object manipulation frame
		initializeOFrame(self)
		
		# BEGIN brush & layers manipulation frame
		def initializeBFrame(self):	
			self.BFrame = Frame(self.controlsFrame,bg='purple')
			self.BFrame.grid(column=3,row=0)
			
			self.BRUSHES = ['selector','object','terrain vertex']
			#self.brushListBox = Listbox(self.BFrame)
			self.brushRB=dict()
			self.brushNumber = IntVar()
			c=0
			def select():
				self.currentBrush = self.BRUSHES[brushNumber]
			for i in self.BRUSHES:
				#self.brushListBox.insert(END,i)
				self.brushRB[i] = Radiobutton(self.BFrame, text=i,value=c, variable=self.brushNumber)
				self.brushRB[i].pack(fill=X)
				c+=1
			
			# END brush & layers manipulation frame
		initializeBFrame(self)
		
	def startME(self):
		self.root.mainloop()
