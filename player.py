import os
import time
from subprocess import PIPE, Popen, STDOUT

directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'videos')

videos = []


def getVideos():
    global videos
    videos = []
    files = [f for f in os.listdir(directory) if f.lower().endswith('.mp4')]
    files.sort()  # sort files alphabetically
    for file in files:
        videos.append(os.path.join(directory, file))


def playVideos():
    global videos
    if len(videos) == 0:
        getVideos()
        time.sleep(5)
        return
    for video in videos:
        playProcess = Popen(['omxplayer', '--no-osd', '--aspect-mode', 'letterbox', video])
        playProcess.wait()


while (True):
    playVideos()
