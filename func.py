def make_album(singer_name,album_name,song_num=''):
    album='Singer '+singer_name+' has an '+album_name+'.'
    '''

    if song_num:
        print('Singer '+singer_name+' has an '+album_name+',include '+str(song_num)+' songs')
    else:
        print('Singer '+singer_name+' has an '+album_name+' .')
    return album
    '''
while True:
    print('Please input your message!')
    singer_name=input('singer name:')
    if singer_name=='q':
        break
    album_name=input('album name:')
    if album_name=='q':
        break
    song_num=input('song num:')
    if song_num=='0':
        print('Singer '+singer_name+' has an '+album_name+' .')
    else:
        print('Singer ' + singer_name + ' has an ' + album_name + ',include ' + str(song_num) + ' songs')
'''album=make_album('A','B',10)
print(album)
album=make_album('C','D')
print(album)
'''

