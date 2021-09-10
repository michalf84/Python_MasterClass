import tkinter
import os
mainWindow=tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")
mainWindow['padx']=8

label=tkinter.Label(mainWindow,text="Tkinger Grid Demo")
label.grid(row=0,column=0,columnspan=3)

mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=1)
mainWindow.columnconfigure(2,weight=3)
mainWindow.columnconfigure(3,weight=3)
mainWindow.columnconfigure(4,weight=3)
mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=10)
mainWindow.rowconfigure(2,weight=1)
mainWindow.rowconfigure(3,weight=3)
mainWindow.rowconfigure(4,weight=3)

fileList=tkinter.Listbox(mainWindow)
fileList.grid(row=1,column=0,sticky='nsew',rowspan=2)
fileList.config(border=2,relief='sunken')

for zone in os.listdir('/windows/system32'):
    fileList.insert(tkinter.END,zone)

listScroll=tkinter.Scrollbar(mainWindow,orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1,column=1,sticky='nsw',rowspan=2)
fileList["yscrollcommand"]=listScroll.set

# frame for radio buttons
optionFrame=tkinter.Label(mainWindow,text="File Detials")
optionFrame.grid(row=1,column=2,sticky='ne')

rbValue=tkinter.IntVar()
rbValue.set(3)
# radio butt
radio1=tkinter.Radiobutton(optionFrame,text='Filename',value=1,variable=rbValue)
radio2=tkinter.Radiobutton(optionFrame,text='Path',value=2,variable=rbValue)
radio3=tkinter.Radiobutton(optionFrame,text='Timestamp',value=3,variable=rbValue)
radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')
radio3.grid(row=2,column=0,sticky='w')

# widget to show results
resultLabel=tkinter.Label(mainWindow,text="result")
resultLabel=tkinter.Entry(mainWindow)
resultLabel.grid(row=2,column=2,sticky='nw')

# frame for time spinners
timeFrame=tkinter.LabelFrame(mainWindow,text="Time")
timeFrame.grid(row=3,column=0,sticky='new')
# time spinners
hourSpinner=tkinter.Spinbox(timeFrame,width=2,values=tuple(range(0,24)))
minuteSpinner=tkinter.Spinbox(timeFrame,width=2, from_=0, to_=59)
secondSpinner=tkinter.Spinbox(timeFrame,width=2,from_=0,to_=59)
hourSpinner.grid(row=0,column=0)
tkinter.Label(timeFrame,text=':').grid(row=0,column=1)
minuteSpinner.grid(row=0,column=2)
tkinter.Label(timeFrame,text=':').grid(row=0,column=3)
secondSpinner.grid(row=0,column=4)
timeFrame['padx']=36

# frame fro the dates spinners
dateFrame=tkinter.Frame(mainWindow)
dateFrame.grid(row=4,column=0,sticky='new')
# date labels
dayLabel=tkinter.Label(dateFrame,text="Day")
monthLabel=tkinter.Label(dateFrame,text="month")
yearLabel=tkinter.Label(dateFrame,text="Year")
dayLabel.grid(row=0,column=0,sticky='w')
monthLabel.grid(row=0,column=1,sticky='w')
yearLabel.grid(row=0,column=2,sticky='w')
# date spinners
daySpin=tkinter.Spinbox(dateFrame,width=5,from_=1,to_=31)
monthSpin=tkinter.Spinbox(dateFrame,width=5,values=["jan","feb","march","april","may","june","july","aug","sept","now","dec"])
yearSpin=tkinter.Spinbox(dateFrame,width=5, from_=2000,to_=2099)
daySpin.grid(row=1,column=0)
monthSpin.grid(row=1,column=1)
yearSpin.grid(row=1,column=2)

# buttons
okButton=tkinter.Button(mainWindow,text="ok")
# note in below destry there are no () as they would assign value, we remove () to run fucnion
cancelButton=tkinter.Button(mainWindow,text="Cancel",command=mainWindow.destroy)
okButton.grid(row=4,column=3, sticky='e')
cancelButton.grid(row=4,column=4, sticky='w')




mainWindow.mainloop()
print(rbValue.get())