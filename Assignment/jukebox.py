from test_tuplenested import albums

SONGS_LIST = 3

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][3]
    else:
        break

    print(albums[choice - 1])
    print(songs_list)
    print()
