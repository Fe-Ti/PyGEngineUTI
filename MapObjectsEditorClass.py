# MOEclassModule 
# Pine v.1.0

# standart python3 modules
from tkinter import *
from time import *

# my modules
from GUIclassModule import *


class MOE(GUI):
	def __init__(self):
		super().__init__('MOE')
		
		self.t_reso = self.INITPARAMS['t_reso']
	
		self.spritePickerL = Label (self.controlsFrame, text='Sprite(press Return to load):')
		self.spritePickerL.pack()
	
		self.spritePicker = Entry (self.controlsFrame)
		self.spritePicker.pack()
	
		self.TtagsL = Label (self.controlsFrame, text='Tags for MO type(press Return to add or Delete to remove):')
		self.TtagsL.pack()
	
		self.TtagsEntry = Entry (self.controlsFrame)
		self.TtagsEntry.pack()
		
		self.Ttags = dict()
	
		self.MONameL = Label (self.controlsFrame,text='Map object name:')
		self.MONameL.pack()
	
		self.MOName = Entry (self.controlsFrame)
		self.MOName.pack()
		
		##self.gridToggle = Button (self.controlsFrame, text='')
		##self.gridToggle.pack()
	
		self.saveObjectB = Button (self.controlsFrame, text='Save object')
		self.saveObjectB.pack()
		
		self.loadObjectB = Button (self.controlsFrame, text='Load object')
		self.loadObjectB.pack()
	
		self.sprites['current'] = spriteObject('',[],[])
		# populating self.canvas
		name = self.spritePicker.get()
		self.sprites['current'].name = name
		for i in range (self.INITPARAMS['t_reso']):
			self.sprites['current'].spriteElements.append([])
			self.sprites['current'].spriteElementsData.append([])
			for k in range (self.INITPARAMS['t_reso']):
				x1 = i*self.INITPARAMS['scale']
				x2 = (i+1)*self.INITPARAMS['scale']
				y1 = k*self.INITPARAMS['scale']
				y2 = (k+1)*self.INITPARAMS['scale']
				coords = [x1,y1,x2,y2]
				self.sprites['current'].spriteElements[i].append(self.canvas.create_rectangle(coords))
				Pixel = pixel(coords,self.canvas.itemcget(k,'fill'))
				self.sprites['current'].spriteElementsData[i].append(Pixel)

	
	
	def refreshSprite(self):
		
		name = self.spritePicker.get()
		self.sprites['current'].name = name
		    
		for i in range (self.INITPARAMS['t_reso']):
			for k in range (self.INITPARAMS['t_reso']):
				outlineColor = (self.INITPARAMS['tg']>0)*'black'+(self.INITPARAMS['tg']<0)*self.sprites['current'].spriteElementsData[i][k].fill
				self.canvas.itemconfig(self.sprites['current'].spriteElements[i][k],fill=self.sprites['current'].spriteElementsData[i][k].fill, outline=outlineColor)
	
	def loadSprite(self,name):
		#self.canvas.delete('all')
		
		self.sprites['current'].name = name
		sprfile = open(name+'.spr','r')
		line=''
		for i in range(self.t_reso):
			line = sprfile.readline().replace('\n','')
			columnColors = line.split('@')
			for k in range(self.t_reso):
				#print(i,k,columnColors[k])
				self.sprites['current'].spriteElementsData[i][k].fill = columnColors[k]
		self.refreshSprite()
		sprfile.close()


	def updateTextOut(self):
		textOut=''
		for i in self.Ttags:
			textOut += self.Ttags[i] + '<>'
		self.textOut.config(text=textOut)
		
	def addTag(self):
		tag = self.TtagsEntry.get()
		self.Ttags[tag] = tag
		textOut=''
		self.updateTextOut()
	
	def deleteTag(self):
		tag = self.TtagsEntry.get()
		try:
			del self.Ttags[tag]
		except KeyError:
			pass 
		self.updateTextOut()
		
	def saveObject(self,name):
		objfile = open (name+'.mo','w')
		sprite = self.sprites['current'].name
		typeTags = ''
		for i in self.Ttags:
			typeTags+= self.Ttags[i]
		text = sprite + '\n' + typeTags
		objfile.write(text)
		objfile.close()
		
	def loadObject(self,name):
		objfile = open (name+'.mo','r')
		
		self.sprites['current'].name = objfile.readline().replace('\n','')
		self.spritePicker.delete(0, END)
		self.spritePicker.insert(0,self.sprites['current'].name)
		self.loadSprite(self.sprites['current'].name)
		
		Ttags = objfile.readline()
		Ttags = Ttags.split('<>')
		self.Ttags = dict()
		for i in Ttags:
			self.Ttags[i.replace('\n','')] = i 
		self.updateTextOut()
		
		objfile.close()
