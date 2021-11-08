print("Welcome to my computer quiz! ")

playing=input("Do you want to play? ")
score=0
if playing.lower()!="yes":
    quit()

answer=input("what does cpu stand for? ")
if answer.lower()=="central processing unit":
    print("correct!")
    score+=1

else:
    print("Incorrect!")