import MapEditor as me

app = me.ME()

app.startME()


# import MapObjectsEditorClass as moe

# app = moe.MOE()

# def loadSpriteFE(event):
	# name = app.spritePicker.get()
	# app.loadSprite(name)
	
# def loadObjectFE(event):
	# name = app.MOName.get()
	# app.loadObject(name)

# def saveObjectFE(event):
	# name = app.MOName.get()
	# app.saveObject(name)

# def addTagFE(event):
	# app.addTag()
	
# def deleteTagFE(event):
	# app.deleteTag()

# app.TtagsEntry.bind('<Return>',addTagFE)
# app.TtagsEntry.bind('<Delete>',deleteTagFE)
# app.saveObjectB.bind('<Button>',saveObjectFE)	
# app.loadObjectB.bind('<Button>',loadObjectFE)
# app.spritePicker.bind('<Return>',loadSpriteFE)
# app.start()



# img = open ('In.gif','rb')
# s=img.read()
# print (s)
######from tkinter import *
########import  PIL as pil
######root = Tk()
######root.geometry('1000x1000')
######canvas = Canvas(root,width=999,height=999)
######canvas.pack()
######rect=[]
######c=0
##########for i in range(320):
##########    for k in range (320):
##########       rect.append(canvas.create_rectangle(i,k,i+1,k+1,fill='white')) 
########pilImage = pil.Image.open("In.jpg")
############for i in range (64*64):
######image = PhotoImage(file="In.ppm")
######imagesprite = canvas.create_image(5,5,image=image)
######def mover (event):
######    global c
######    c=0
######    def stepper():
######        global c
######        canvas.move('all',1,1)
######        print(c)
######        if c<10:
######            root.after(10,stepper)
######        c+=1
######
######    stepper()
######
######root.bind('<Button-1>',mover)
######root.mainloop()
######
######
######
######
######
########################################################import os.path
##########################################################
##########################################################sp='/forestTile.asef'
##########################################################track=  os.path.normpath(os.path.relpath("res/test/"+sp, start=os.curdir))
##########################################################file = open (track)
##########################################################print (file.read())
########################################################
########################################################import tkinter as tk
########################################################
########################################################class Application(tk.Frame):
########################################################    def __init__(self, master=None):
########################################################        super().__init__(master)
########################################################        self.master = master
########################################################        self.pack()
########################################################        self.create_widgets()
########################################################
########################################################    def create_widgets(self):
########################################################        self.hi_there = tk.Button(self)
########################################################        self.hi_there["text"] = "Hello World\n(click me)"
########################################################        self.hi_there["command"] = self.say_hi
########################################################        self.hi_there.pack(side="top")
########################################################
########################################################        self.quit = tk.Button(self, text="QUIT", fg="red",
########################################################                              command=self.master.destroy)
########################################################        self.quit.pack(side="bottom")
########################################################
########################################################    def say_hi(self):
########################################################        print("hi there, everyone!")
########################################################
########################################################root = tk.Tk()
########################################################app = Application(master=root)
########################################################app.mainloop()
######################################################import os
######################################################import tkinter as tk
######################################################def play(event):
######################################################    wav_file = "./Hello.wav"
######################################################    os.system(f'aplay -i {wav_file}')
######################################################def stop(event):
######################################################    for i in range(1999):
######################################################        print ('addwdvs')
######################################################    os.system(f'^C')
######################################################
######################################################root = tk.Tk ()
######################################################root.bind('<p>',play)
######################################################root.bind('<s>',stop)
######################################################root.mainloop()
