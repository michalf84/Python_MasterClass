from Nested_data_structures import albums

# to create constant value
SONGS_LIST_INDEX=3
SONG_TITLE_INDEX=1

while True:
    print("please choose your alboum (invalid choice exists):")
    # note bracket to iterate via tuple 2 verisons of code
    # for index,value in enumerate(albums):
    #     title,artist,year,songs=value
    #     print(index,title,artist,year,songs)

    # for index,(title,artist,year,songs) in enumerate(albums):
    #     print(f"{index+1}:{title}:{artist}:{year}:{songs}")
    # break

    for index,(title,artist,year,songs) in enumerate(albums):
        print(f"{index+1}:{title}")
    choice=int(input())
    if 1<=choice<=len(albums):
        songs_list=albums[choice-1][SONGS_LIST_INDEX]
    else:
        break
    # print(albums[choice-1])
    # print(songs_list)
    # print()
    print("please choose your song:")
    for index,(track_number,song) in enumerate(songs_list):
        print(f"{index+1}:{song}")

    song_choice=int(input())
    if 1<=song_choice<=len(songs_list):
        title=songs_list[song_choice-1][SONG_TITLE_INDEX]
        print(f"Playing{title}")
    print("="*40)
