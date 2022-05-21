import random
import pyautogui as pg
import time

x=('Aryan','Shikhar','Friends','Bros','Shreyansh','Tanmay')
time.sleep(7)
for i in range(200):
    a=random.choice(x)
    pg.write("Hello "+a)
    pg.press("enter")
    