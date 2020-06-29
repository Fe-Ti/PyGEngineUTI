import tkinter as tk

# there are some combo widgets

class GeoMan:
	
	def packMe(self,Side,Fill):
		self.Frame.pack(side=Side,fill=Fill)

	
	def gridMe(self,c,r):
		self.Frame.grid(column=c,row=r)
		
	def placeMe(): #FIXME
		null=0

class scrListBox(GeoMan):
	
	def __init__(self, root, LIST):
		self.Frame = tk.Frame(root)
		self.ListBox = tk.Listbox(self.Frame, width=30)
		 
		for i in LIST:
		    self.ListBox.insert(tk.END, i)
		    
		self.scrollbar = tk.Scrollbar(self.Frame)
		self.ListBox.config(yscrollcommand = self.scrollbar.set)
		self.scrollbar.config(command = self.ListBox.yview)
		self.ListBox.pack(side = tk.LEFT, fill = tk.Y)
		self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
		
	def getCurrent(self):
		return self.ListBox.get(self.ListBox.curselection())
		
	
	
