class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []


class Album:
    def __init__(self, title):
        self.title = title
        self.artist = None


if __name__ == '__main__':
    my_artist = Artist('Avril Lavigne')
    album = Album('Let Go')
    another_album = Album('Love Sucks')
    album.artist = my_artist
    my_artist.albums.append(album)
    my_artist.albums.append(another_album)

    for album in my_artist.albums:
        print(album.title)