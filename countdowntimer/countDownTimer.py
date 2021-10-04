# creating a basic countdown timer
import time

def countdown(t):
    while t:
        mins,secs=divmod(t,60)
        timer='{0:2d}:{0:2d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1

    print("Aaag lagi basti mai aur meh idhar python ke sath masti mai")

t=input("Enter the time in seconds:_")

countdown(int(t))