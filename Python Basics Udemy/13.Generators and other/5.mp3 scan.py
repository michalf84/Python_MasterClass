import os
import fnmatch
import id3reader_p3 as id3reader

def find_music(start,extension):
    for path,directories, files in os.walk(start):
        for file in fnmatch.filter(files,'*.{}'.format(extension)):
            absolute_path=os.path.abspath(path)
            yield os.path.join(absolute_path,file)

for f in find_music('music','emp3'):
    id3r=id3reader.Reader(f)
    print("artist: {}, Album{}, track: {},song:{}".format(
        id3r.get_value('performer'),
        id3r.get_value('album'),
        id3r.get_value('track'),
        id3r.get_value('title') ))