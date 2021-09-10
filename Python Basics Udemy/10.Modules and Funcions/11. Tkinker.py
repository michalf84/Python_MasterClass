import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow=tkinter.Tk()

mainWindow.title("Hello Worlds")
mainWindow.geometry("640x480")

label=tkinter.Label(mainWindow,text="Hello WOorld")
label.pack(side='top')

leftFrame=tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n',fill=tkinter.Y, expand=False)

canvas=tkinter.Canvas(mainWindow, relief="raised",borderwidth=5)
canvas.pack(side="left",anchor='n')

rightFrame=tkinter.Frame(mainWindow)
rightFrame.pack(side='right',anchor='n',expand=True)
# note that with x expand must be used in this set up, the same with Y does not need to hav eit, left right build other combinations too
# canvas.pack(side="left",fill=tkinter.X,expand=True)
button1=tkinter.Button(mainWindow, text="button1")
button2=tkinter.Button(mainWindow, text="button2")
button3=tkinter.Button(mainWindow, text="button3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")
mainWindow.mainloop()