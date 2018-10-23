"""
Python --> MySQL using pymysql
"""
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# save the comments
def insert_comments(music_id, comments, detail, connection0):
    with connection0.cursor() as cursor:
        sql = "INSERT INTO `comments` (`MUSIC_ID`, `COMMENTS`, `DETAILS`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, comments, detail))
    connection0.commit()


# save the music
def insert_music(music_id, music_name, album_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `musics` (`MUSIC_ID`, `MUSIC_NAME`, `ALBUM_ID`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, music_name, album_id))
    connection.commit()


# save the album
def insert_album(album_id, artist_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `albums` (`ALBUM_ID`, `ARTIST_ID`) VALUES (%s, %s)"
        cursor.execute(sql, (album_id, artist_id))
    connection.commit()


# save the artist
def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()


# Get the ID of all artists
def get_all_artist():
    with connection.cursor() as cursor:
        sql = "SELECT `ARTIST_ID` FROM `artists` ORDER BY ARTIST_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# get the ID of all albums
def get_all_album():
    with connection.cursor() as cursor:
        sql = "SELECT `ALBUM_ID` FROM `albums` ORDER BY ALBUM_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# get the ID of all music
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# previous half of music
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 0, 800000"
        cursor.execute(sql, ())
        return cursor.fetchall()


# later half of music
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 800000, 1197429"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()
