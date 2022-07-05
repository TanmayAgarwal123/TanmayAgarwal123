from pytube import YouTube
import pyautogui as p
from tkinter import *
import sqlite3
a = p.confirm('Enter the YouTube link of the video',title="YouTube Downloader",buttons=['Download','Cancel'])
def add_link():
    global links
    link = links.get()
link="https://www.youtube.com/watch?v=sP7A-RgNxkY"
video= YouTube(link)
videos=video.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("enter : "))
videos[strm].download()
print("Successfully Done")

