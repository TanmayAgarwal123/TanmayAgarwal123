from tkinter import *
from unicodedata import name
from click import command
from pytube import YouTube
import pyautogui as p
root=Tk()
root.geometry("300x100")
name_var=StringVar()
video=StringVar()
def download():
	name=name_var.get()
	print("downloaded :- " + name)
	name_var.set("")
name_label = Label(root, text = 'Link')
name_entry = Entry(root,textvariable = name_var)
sub_btn=Button(root,text = 'Download', command = download)
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
sub_btn.grid(row=2,column=1)
root.mainloop()
video= YouTube(name)
videos=video.streams.get_highest_resolution()
videos.download()
print("Successfully done")


"""videos=video.streams.all()
vid=list(enumerate(videos))
for i in vid:
    print(i)
print()
strm=int(input("enter : "))
videos[strm].download()
print("Successfully Done")"""