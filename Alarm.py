from datetime import datetime
from pygame import mixer
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
while True:
    d=datetime.now()
    if d.hour<13:
        if d.minute==0 and d.second==0:
               musiconloop('water.mp3','stop')
               print('Time is',d.hour,"AM\nType'stop' to break alarm")
    else:
        if d.minute==0 and d.second==0:
               musiconloop('water.mp3','stop')
               print("Time is",d.hour-12,"PM\nType'stop' to break alarm")
