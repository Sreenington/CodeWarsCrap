def song_decoder(song):
    song = (song.replace('WUB', ' ')).split()
    return print(' '.join(song))


s1 = "AWUBBWUBC"
s2 = "AWUBWUBWUBBWUBWUBWUBC"
s3 = "WUBAWUBBWUBCWUB"
song_decoder(s2)