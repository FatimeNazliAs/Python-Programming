import random
def play():

    user_point=0
    computer_point=0
    for i in range(3):
        user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            continue
        if is_win(user, computer):
            user_point += 1


        else:
            computer_point += 1

        print(f"computer choice is {computer}")



    if user_point>computer_point:
        print(f'You won! user: {user_point} computer {computer_point}')

    elif user_point<computer_point:
        print(f'You lost! user: {user_point} computer {computer_point}')

    else:
        print("It is a tie.")


def is_win(player,opponent):
    # r>s, s>p,p>r
    if (player=='r'and opponent=='s') or(player=='s' and opponent=='p')\
        or (player=='p' and opponent=='r'):
        return True
play()