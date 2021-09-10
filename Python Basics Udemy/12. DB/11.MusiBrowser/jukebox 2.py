#after scrooll back and grid fundioncs

import sqlite3
import tkinter

conn=sqlite3.connect('music.sqlite')

class Scrollbox(tkinter.Listbox):

    def __init__(self,window,**kwargs):
        super().__init__(window,**kwargs)

        self.scrollbar=tkinter.Scrollbar(window,orient=tkinter.VERTICAL,command=self.yview)

    def grid(self,row,column,sticky='nsw',rowspan=1,columnspan=1,**kwargs):
        super().grid(row=row,column=column,sticky=sticky,rowspan=rowspan,columnspan=columnspan,**kwargs)
        self.scrollbar.grid(row=row,column=column,sticky='nse',rowspan=rowspan)
        self['yscrollcommand']=self.scrollbar.set

mainWindow=tkinter.Tk()
mainWindow.title=("Musiv DB Browser")
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0,weight=2)
mainWindow.columnconfigure(1,weight=2)
mainWindow.columnconfigure(2,weight=2)
mainWindow.columnconfigure(3,weight=1)

mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=5)
mainWindow.rowconfigure(2,weight=5)
mainWindow.rowconfigure(3,weight=1)


# labels
tkinter.Label(mainWindow,text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow,text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow,text="Songs").grid(row=0, column=2)

# artists listbox
#artistList=tkinter.Listbox(mainWindow)
artistList=Scrollbox(mainWindow)
artistList.grid(row=1,column=0, sticky='nsew', rowspan=2,padx=(30,0))
artistList.config(border=2,relief='sunken')

# artistScroll=tkinter.Scrollbar(mainWindow,orient=tkinter.VERTICAL,command=artistList.yview)
# artistScroll.grid(row=1,column=0,sticky='nse',rowspan=2)
# artistList['yscrollcommand']=artistScroll.set

# albums listbox
albumLV=tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
#albumList=tkinter.Listbox(mainWindow,listvariable=albumLV)
albumList=Scrollbox(mainWindow,listvariable=albumLV)
albumList.grid(row=1,column=1,sticky='nsew',padx=(30,0))
albumList.config(border=2,relief='sunken')

# albumScroll=tkinter.Scrollbar(mainWindow,orient=tkinter.VERTICAL,command=artistList.yview)
# albumScroll.grid(row=1,column=1,sticky='nse',rowspan=2)
# albumList['yscrollcommand']=artistScroll.set


# songs listbox
songLV=tkinter.Variable(mainWindow)
songLV.set(("Choose album",))
#songList=tkinter.Listbox(mainWindow,listvariable=songLV)
songList=Scrollbox(mainWindow,listvariable=songLV)
songList.grid(row=1,column=2,sticky='nsew',padx=(30,0))
songList.config(border=2,relief='sunken')

# main loop
testList=range(0,100)

albumLV.set(tuple(testList))
mainWindow.mainloop()
print("closing db conneciton")
conn.close()