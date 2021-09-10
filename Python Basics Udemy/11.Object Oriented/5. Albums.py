# note this version has circular reference

class Song:
    """Clss to rpresent a song
    
        Attributes:
        title(str): the title of the song
        artist(Artist): an artist objectg reprsenting the song creator
        duration (int): the duration of the song in seconds may be zero
        """
    
    def __init__(self,title,artist,duration=0):
            """Dont init method
            Args:
                ""title (str)initates the title atribute
                  artist (artist): an artist objectr representing the sont creator.
                    furation (optional (int): initial value of duration attribute. default to zero"""
            self.title=title
            self.artist=artist
            self.duration=duration
# help(Song)
# help(Song.__init__)
# help(Song.__init__.__doc__)
# help(Song.__doc__)

class Album:
    """Class to represent an Album using its track list of
        Attributes:
            name (str): _name of the album
            year(int): the year the album was released
            artist: (Artist): the artist responsible for song
            if not specified the artist will be defaulted to an artist with the nam 'various atists'
            tracks (List(Song)): a list of the songs on the album with
            
        Methods:
            addSong: used to add a new song to the album track list)
            """
    def __init__(self,name,year,artist=None):
        self._name=name
        self.year=year
        if artist is None:
            self.artist=Artist("various Artists")
        else:
            self.artist=artist

        self.tracks=[]

    def add_song(self,song, position=None):

        """Adds a as ong to the track list

        Args:
            song (SOng): a song to add
            position (optional)(int) - inseriti between other songs if needed otherwise song will be added to the end of the list
            """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position,song)

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
        self._name=name
        self.albums=[]

    def add_album(self,album):

        """add a new album to the list
            Args:
                album (Album): album object to add to th elist
                if the album is already present if will not be added again
                """
        self.albums.append(album)

def find_object(field,object_list):
    """check object_list to see if an object witha  a'_name' attribute equal to 'field' exists return it if so """
    for item in object_list:
        if item._name==field:
            return item
    return None

def load_data():
    new_artist=None
    new_album=None
    artist_list=[]

    with open("albums.txt","r") as albums:
        for line in albums:
            artist_field,album_field,year_field,song_field=tuple(line.strip('\n').split('\t'))
            year_field=int(year_field)
            print("{}:{}:{}:{}".format(artist_field,album_field,year_field,song_field))

            if new_artist is None:
                new_artist=Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist._name != artist_field:
#                 we have just read details for a new artist
#                  CHANGED terrie the artist obejct if there is
#                  one otherwise create a new artist object and add it to the artist list

                new_album=find_object(artist_field,artist_list)
                if new_artist is None:
                    new_artist=Artist(artist_field)
                    artist_list.append(new_artist)
                new_album=None

            if new_album is None:
                new_album=Album(album_field,year_field,new_artist)
                new_artist.add_album(new_album)
            elif new_album._name!=album_field:
#                 we just read a new album for the current artist
#                  CHANGED retrieve the album object if thre is one
#                   else create a new album objectg and store it in the atists colelction
                new_album=find_object(album_field,new_artist.albums)
                if new_album is None:
                    new_album=Album(album_field,year_field,new_artist)
                new_artist.add_album(new_album)
                new_album=Album(album_field,year_field,new_artist)
            #crea a new song oabject and add it to curent album colleciton
            new_song=Song(song_field,new_artist)
            new_album.add_song(new_song)
#REMOVED SECTION

    return artist_list

def create_checkfile(artist_list):
#     creat a check ifle from objct dta for comparison with original ifle
    with open("checkfile.txt","w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0._name}\t{1._name}\t{1.year}\t{2.title}".format(new_artist,new_album,new_song),
                          file=checkfile)


# check 236 importing techniques
if __name__=="__main__":
    artists=load_data()
    print("there are {} artists ".format(len(artists)))
    
    create_checkfile((artists))