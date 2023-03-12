from moviepy import editor
from time import time
from threading import Thread

videos = {"Dualar Eder Insan" : editor.VideoFileClip('Dualar Eder Insan.mp4'),
          "Haydi Soyle" : editor.VideoFileClip('Haydi Soyle.mp4'),
          "Hello" : editor.VideoFileClip('Hello.mp4'),
          "Muallem" : editor.VideoFileClip('Muallem.mp4'),
          "Sky Fall" : editor.VideoFileClip('Sky Fall.mp4')}

def Convert(name,video):
    filename = f'{name}.mp3'
    video.audio.write_audiofile(filename)

start1 = time()
for name,video in videos.items():
    Convert(name,video)
end1 = time()
print("Time without Thread" , end1-start1)

###############################################

start2 = time()
for name,video in videos.items():
    thred = Thread(target=Convert,args=[name,video])
    thred.start()
    thred.join()
    
end2 = time()
print("Time With Thread",end2-start2)