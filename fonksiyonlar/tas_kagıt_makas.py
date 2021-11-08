import time
import random


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")


begin = input("Are you ready? ")
countdown(2)




def rock_paper_scissors():
    gamer_point = 0
    computer_point = 0
    value = ["rock", "paper", "scissors"]



    #gamer_pick = input("paper,rock,scissors?  ")
    for i in range(3):

        computer_pick = random.choice(value)

        gamer_pick = input("paper,rock,scissors?  ")
        print(computer_pick)
        if computer_pick=="rock" and gamer_pick=="scissors":
            computer_point += 1
        if computer_pick == "rock" and gamer_pick == "paper":
            gamer_point += 1

        if computer_pick == "paper" and gamer_pick == "rock":
            computer_point += 1
        if computer_pick == "paper" and gamer_pick == "scissors":
            gamer_point += 1

        if computer_pick == "scissors" and gamer_pick == "paper":
            computer_point += 1

        if computer_pick == "scissors" and gamer_pick == "rock":
            gamer_point += 1



        if computer_pick=="paper" and gamer_pick=="paper":
            continue
        if computer_pick=="rock" and gamer_pick=="rock":
            continue
        if computer_pick=="scissors" and gamer_pick=="scissors":
            continue

    if (gamer_point == 1 and computer_point == 2) or (gamer_point == 0 and computer_point == 2) or (
            gamer_point == 0 and computer_point == 3) or (gamer_point == 0 and computer_point == 1):
        print(' {} computer_point kazandı {} gamer_point yenildi'.format(computer_point, gamer_point))

    elif (gamer_point == 2 and computer_point == 1) or (gamer_point == 2 and computer_point == 0) or (
            gamer_point == 3 and computer_point == 0) or (gamer_point == 1 and computer_point == 0):
        print(' {} computer_point yenildi {} gamer_point kazandı'.format(computer_point, gamer_point))

    else:
        # if (gamer_point == 1 and computer_point == 1) or (gamer_point == 0 and computer_point == 0):
        print(' {} computer_point  {} gamer_point berabere kaldı'.format(computer_point, gamer_point))



rock_paper_scissors()














    
      
      
