def city_country(name,country):
    return print(f' "{name},{country}" ')

city_country('Denver', "USA")
city_country('Palmetto', "USA")
city_country('London', "Britain")

def make_album(artist_name,album_title, num_songs = None):
    if num_songs:
        album = {'Artist Name' : artist_name , 'Album' : album_title, 'Number of Songs': num_songs}

    else:
        album = {'Artist Name' : artist_name , 'Album' : album_title}
    return album

print(make_album('Mac Miller', 'Blue Slide Park', 4))
print(make_album('Jeff Buckley', 'Grace'))
print(make_album('Yeasayer', 'Odd Blood',9))

while True:
    print("Lets add you favorite artist and album to the dictionary")

    user_artist = input("\n Which Artist")
    user_album = input("\n Which Album")

    mk_al= make_album(user_artist,user_album)
    print(mk_al)
    break