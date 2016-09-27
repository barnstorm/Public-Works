import os
import youtube_dl

def mv(path, extenstion):
    ls = os.listdir(path)
    filenames = (os.path.join(path, filename) for filename in ls)
    for original_file in filenames:
        if os.path.isfile(original_file) == True:
            new_file = original_file + extenstion
            os.rename(original_file, new_file)

def getaudio(url):
    mp3savedir = '/home/barmstrong/homebot/mp3'
    os.chdir(mp3savedir)
    options = {
        'format': 'bestaudio/best', # choice of quality
        'extractaudio' : True,      # only keep the audio
        'audioformat' : "mp3",      # convert to mp3
        'outtmpl': '%(title)s',        # name the file the ID of the video
        'noplaylist' : True,}       # only download single song, not playlist
    with youtube_dl.YoutubeDL(options) as ydl:
        r = ydl.extract_info(url, download=False)
        title = r['title']
        ydl.download([url])
        mv(mp3savedir, '.mp3')
        if title in os.listdir( mp3savedir ):
            os.system("sh /opt/homebot/rclone move " +  mp3savedir + ' ' + title +" remote:")
    return title

def getvideo(url):
    vidssavedir = '/home/barmstrong/homebot/video'
    os.chdir(vidssavedir)
    options = {
        'format': 'bestaudio/best', # choice of quality
        'outtmpl': '%(title)s',        # name the file the ID of the video
        'noplaylist' : True,}       # only download single song, not playlist
    with youtube_dl.YoutubeDL(options) as ydl:
        r = ydl.extract_info(url, download=False)
        title = r['title']
        ydl.download([url])
        mv(mp3savedir, '.mp3')
        if title in os.listdir( vidssavedir ):
            os.system("sh /opt/homebot/rclone move " +  vidssavedir + ' ' + title +" remote:")
    return title



