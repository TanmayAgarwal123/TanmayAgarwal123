import time

def countdown(t):
    while t:
        mins,sec =divmod(t,60)
        timer = '{:02d}:{:02d}'.format(mins,sec)
        print(timer,end="\r")
        time.sleep(1)
        t=t-1
    print("TIME UP!")

t=int(input("Enter the time in secs for alarm "))
countdown(t)
