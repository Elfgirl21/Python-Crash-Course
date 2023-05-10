def make_album(artist, name):
    album = {'artist name': artist, 'album name': name}
    return album

while True:
    print("Please the artist name and album.")
    print("(enter 'q' to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    b_name = input("Album name: ")
    if b_name == 'q':
        break

    name_pair = make_album(a_name, b_name)
    print(name_pair)