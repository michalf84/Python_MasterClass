def find_object(field, object_list):
    for item in object_list:
        if item.name==field:
            return item


def load_data():
    artist_list=[]
    with open("albums.txt","r") as albums:
        for line in albums:
            artist_field,album_field,year_field,song_field=tuple(line.strip('\n').split('\t'))
            year_field=int(year_field)

            if artist_field not in artist_list:
                artist_list.append(artist_field)

            # new_artist=find_object(artist_field,artist_list)
    print(artist_list)
load_data()

class Dog:
    def __init__(self,name,objo):
        self.name=name
        self.objo=objo

class Head:
    def __init__(self,name,size):
        self.name=name
        self.size=size

glowa=Head("glowina",23)
# print("name:{} size {}".format(glowa.name,glowa.size))
# print(glowa)
pies=Dog("burek",glowa)

print(pies)
print("{}:".format(pies.objo.name))


# nowy=Dog("gowno")
# print(nowy.name)