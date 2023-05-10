def make_album(artist, name):
    album = {'artist name': artist, 'album name': name}
    return album

music = make_album('back street boys', 'the black', '20')
print(music)

def make_album(artist, name, songs = None):
    album = {'artist name': artist, 'album name': name}
    if songs:
        album['songs'] = songs
    return album

music = make_album('back street boys', 'the black', '20')
print(music)