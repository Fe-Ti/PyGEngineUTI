# adding GUI class to classes module ==> GUIclassModule

from tkinter import *
from classModule import *

class GUI: # common GUI for games and editors
	
	IPointer='res/misc/'
	SPointer='res/sprites/'
	OPointer='res/objects/'
	MPOinter='res/maps/'

	def __init__ (self,apptype):
		# begin reading init file
		self.INITFILE = open (self.IPointer+apptype+'.init','r')
		self.INITPARAMS = dict()
		line = self.INITFILE.readline()
		while line!="":
			values=line.split('=')
			self.INITPARAMS[values[0]] = int(values[1].replace('\n',''))
			line = self.INITFILE.readline()
		self.INITPARAMS['resx']= self.INITPARAMS['t_reso']*self.INITPARAMS['scale']*self.INITPARAMS['cx']
		self.INITPARAMS['resy']= self.INITPARAMS['t_reso']*self.INITPARAMS['scale']*self.INITPARAMS['cy']
		
		self.INITFILE.close()
		# end reading init file
		
		# basical constants and variables V
		self.type = apptype
		
		self.TERRAINS = ['plain','stones','sand','water','sea','ocean']
		self.COLORS = ['#50aa50','#808080','#efed50','#8080ff','#6060ff','#101080']#,'','','','']
		self.TERRA2COLOR = dict(zip(self.TERRAINS, self.COLORS))

		self.sprites = dict() # here all sprites are placed
		
		# graphical constants V
		
		self.root = Tk()

		self.screenFrame = Frame(self.root)
		self.canvas = Canvas(self.screenFrame,width = self.INITPARAMS['resx'], height = self.INITPARAMS['resy'])
		self.textOut = Label(self.screenFrame)

		self.screenFrame.grid(column=0,row=0)


		self.canvas.grid(column = 0,row = 0)
		self.textOut.grid(column = 0,row = 1)
		
		self.controlsFrame = Frame(self.root)
		self.controlsFrame.grid(column=0,row=1)

			
	def start(self):
		self.root.mainloop()

	def importSettings(self):
		setsfile = open (self.IPointer+self.type+'.settings','r')
		settings = dict()
		line = setsfile.readline()
		while line!="":
			values=line.split('=')
			settings[values[0]] = values[1].replace('\n','')
			line = setsfile.readline()
		self.settings = settings

	def exportSettings(self,name):
		settsfile = open (self.IPointer+self.type+'.settings','w')
		for i in self.settings:
			line = i+'='+str(self.settings[i])+'\n'
			settsfile.write(line)

	def regenerate(self,apptype):
		self.root.destroy()
		# begin reading init file
		self.INITFILE = open (self.IPointer+apptype+'.init','r')
		self.INITPARAMS = dict()
		line = self.INITFILE.readline()
		while line!="":
			values=line.split('=')
			self.INITPARAMS[values[0]] = int(values[1].replace('\n',''))
			line = self.INITFILE.readline()
		self.INITPARAMS['resx']= self.INITPARAMS['t_reso']*self.INITPARAMS['scale']*self.INITPARAMS['cx']
		self.INITPARAMS['resy']= self.INITPARAMS['t_reso']*self.INITPARAMS['scale']*self.INITPARAMS['cy']
		
		self.INITFILE.close()
		# end reading init file
		
		# basical constants and variables V
		self.type = apptype
		
		self.TERRAINS = ['plain','stones','sand','water','sea','ocean']
		self.COLORS = ['#50aa50','#808080','#efed50','#8080ff','#6060ff','#101080']#,'','','','']
		self.TERRA2COLOR = dict(zip(self.TERRAINS, self.COLORS))

		self.sprites = dict() # here all sprites are placed
		
		# graphical constants V
		
		self.root = Tk()

		self.screenFrame = Frame(self.root)
		self.canvas = Canvas(self.screenFrame,width = self.INITPARAMS['resx'], height = self.INITPARAMS['resy'])
		self.textOut = Label(self.screenFrame)

		self.screenFrame.grid(column=0,row=0)


		self.canvas.grid(column = 0,row = 0)
		self.textOut.grid(column = 0,row = 1)
		
		self.controlsFrame = Frame(self.root)
		self.controlsFrame.grid(column=0,row=1)

					
	pass

