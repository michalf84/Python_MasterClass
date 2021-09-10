# note this version has circular reference

class Song:
    """Clss to rpresent a song
    
        Attributes:
        title(str): the title of the song
        #CHANGE artist OBJECT CHANGED TO STR
        artist(str): _name of an artist creator
        duration (int): the duration of the song in seconds may be zero
        """

    def __init__(self,title,artist,duration=0):
            """Dont init method
            Args:
                ""title (str)initates the title atribute
                  artist (artist): an artist objectr representing the sont creator.
                    furation (optional (int): initial value of duration attribute. default to zero"""
            #CHANGED self title to self _name and back as we added new method get title
            self.title=title
            self.artist=artist
            self.duration=duration
# help(Song)
# help(Song.__init__)
# help(Song.__init__.__doc__)
# help(Song.__doc__)


    def get_title(self):
        return self.title

    name=property(get_title)

class Album:
    """Class to represent an Album using its track list of
        Attributes:
            name (str): _name of the album
            year(int): the year the album was released
            #CHANGED artist object to str
            artist: (str): tname of artist
            if not specified the artist will be defaulted to an artist with the nam 'various atists'
            tracks (List(Song)): a list of the songs on the album with
            
        Methods:
            addSong: used to add a new song to the album track list)
            """
    def __init__(self,name,year,artist=None):
        self.name=name
        self.year=year
        if artist is None:
            self.artist="various Artists"
        else:
            self.artist=artist

        self.tracks=[]

    def add_song(self,song, position=None):

        """Adds a as ong to the track list
#
        Args:
            song (Song): title of a song to add
            position (optional)(int) - inseriti between other songs if needed otherwise song will be added to the end of the list
            """
        song_found=find_object(song,self.tracks)
        if song_found is None:
            song_found=Song(song,self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position,song_found)

class Artist:
    """basic class to store artist detila
    Attributes:
        name(str) _name of the artintst
        albums(List(album): a list of the ablums by the artist
        the list includes only  albums in this colleeciton it is not exhaustinve list of the
        artist pulbiched songs
        Methods:
        add_album: use to add a new album to the artist album list"""

    def __init__(self,name):
        self.name=name
        self.albums=[]

    def add_album(self,album):

        """add a new album to the list
            Args:
                album (Album): album object to add to th elist
                if the album is already present if will not be added again
                """
        self.albums.append(album)

    def add_song(self,name,year,title):

        """add new son to the colleciton of album
             this method will add the song to tan album in the colection
             a new album will be created in the collection if it does not already exists
             Args:
                 name (str): the _name of album
                 year (int): the year of album produce
                 title (str): the title of song
                 """
        album_found=find_object(name,self.albums)
        if album_found is None:
            print(name+ "not found")
            #CHANGED self to self._name
            album_found=Album(name,year,self.name)
            self.add_album(album_found)
        else:
            print("found album" +name)
        album_found.add_song(title)

def find_object(field,object_list):
    """check object_list to see if an object witha  a'_name' attribute equal to 'field' exists return it if so """
    for item in object_list:
        if item._name==field:
            return item
    return None

def load_data():

    artist_list=[]

    with open("albums.txt","r") as albums:
        for line in albums:
            artist_field,album_field,year_field,song_field=tuple(line.strip('\n').split('\t'))
            year_field=int(year_field)
            print("{}:{}:{}:{}".format(artist_field,album_field,year_field,song_field))

            new_artist=find_object(artist_field,artist_list)
            if new_artist is None:
                new_artist=Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field,year_field,song_field)

    return artist_list

def create_checkfile(artist_list):
#     creat a check ifle from objct dta for comparison with original ifle
    with open("checkfile.txt","w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    #CHANGED TITLE TO NAME and then to title again as we have nowew method get_title
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist,new_album,new_song),
                          file=checkfile)


# check 236 importing techniques
if __name__=="__main__":
    artists=load_data()
    print("there are {} artists ".format(len(artists)))
    
    create_checkfile((artists))