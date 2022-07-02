# importing YouTube from pytube
from pytube import YouTube
# asking user to enter link
link = input("Enter the link ")
# showing user that the process has started
print("Downloding...")
# main code to download Video
YouTube(link).streams.get_highest_resolution()
# showing user that the video has downloaded
print("Video downloaded successfully")