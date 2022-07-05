import random
while True:
    x = ["Tanmay","Yash","Romit","Rishit","Vimoh","Aditya"]
    y = ["Tanmay","Yash","Romit","Rishit","Vimoh","Aditya"]
    x1 = random.choice(x)
    y.remove(x1)
    y1 = random.choice(y)
    print(x1,y1,sep=" - ")
    print("wanna play again(y/n) :- ")
    z=input()
    if z!="y":
        break
