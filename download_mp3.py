#根据txt文件里的url地址链接，下载链接里的mp3资源

import requests
import os

with open('DoubanMusicLinks.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()
    data1 = [x.strip() for x in data]
    f.close()
    #print(data)
    #print(data1)

with open('musicList.txt', 'r', encoding='utf-8') as f1:
    song = f1.readlines()
    song_name = [x.strip() for x in song]
    f1.close()


def download_music(songlink, songname):
    res = requests.get(songlink)
    music = res.content
    #songname1 = songname.strip('\t')

   # with open(r'‪H:/Python学习实践/url_download_mp3/'+songname+'.mp3', 'ab')as file:
    with open(os.getcwd() + '\\' + songname.replace('\t', '').replace('/', '').replace('?', '') + '.mp3', 'ab')as file:
        file.write(music)
        file.flush()
"""
for songlink,songname in data1,song_name:
    download_music(songlink, songname)
"""

for (songlink, songname) in zip(data1, song_name):
    download_music(songlink, songname)

"""
for url in data1:
    res = requests.get(url)
    music = res.content
    with open(r'‪H:/Python学习实践/url_download_mp3/.mp3', 'ab')as file:
        file.write(res.content)
        file.flush()
"""
"""   
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')

music = res.content

with open(r'c:/Users/Administrator/Desktop/ceshi.mp3', 'ab') as file: #保存到本地的文件名
    file.write(res.content)
    file.flush()
"""