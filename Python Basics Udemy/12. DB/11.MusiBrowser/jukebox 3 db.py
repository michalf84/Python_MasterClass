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

def get_albums(event):
    lb=event.widget
    index=lb.curselection()[0]
    artist_name=lb.get(index),

    #get the artist id from the db row
    artist_id=conn.execute("select artists._id from artists where artists.name=?",artist_name).fetchone()
    alist=[]
    for row in conn.execute("select albums.name from albums where albums.artist=? order by albums.name",artist_id):
        alist.append(row[0])
    albumLV.set(tuple(alist))

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

artistList=Scrollbox(mainWindow)
artistList.grid(row=1,column=0, sticky='nsew', rowspan=2,padx=(30,0))
artistList.config(border=2,relief='sunken')

for artist in conn.execute("select artists.name from artists order by  artists.name"):
    artistList.insert(tkinter.END,artist[0])

artistList.bind('<<ListboxSelect>>',get_albums)

# albums listbox
albumLV=tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
#albumList=tkinter.Listbox(mainWindow,listvariable=albumLV)
albumList=Scrollbox(mainWindow,listvariable=albumLV)
albumList.grid(row=1,column=1,sticky='nsew',padx=(30,0))
albumList.config(border=2,relief='sunken')

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