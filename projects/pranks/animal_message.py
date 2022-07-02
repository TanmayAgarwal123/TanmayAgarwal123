import pyautogui as pg
import time
time.sleep(10)
txt=open('C:/Users/dell/OneDrive/Documents/VS Code/projects/pranks/animals.txt','r')
a="shikhar is a "
for i in txt:
    pg.write(a+" "+i)
    pg.press("Enter")
