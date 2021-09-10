# NOTE THAT pickle loads data into memory not good option for large files

import pickle

imelda=("More Mayhem",
        "Imelda May",
        "2011",
        ((1,"pulling the rug"),
         (2,"Psycho"),
         (4,"Kentish Town Walts")))

# with open("imelda.pickle","wb") as pickle_file:
#     pickle.dump(imelda,pickle_file)

with open("imelda.pickle","rb") as imdelda_pickled:
    imelda2=pickle.load(imdelda_pickled)


print(imelda2)

album,artist,year,track_list=imelda
print(album)
print(artist)

for track in track_list:
    track_number,track_title=track
    print(track_number, track_title)
print()

