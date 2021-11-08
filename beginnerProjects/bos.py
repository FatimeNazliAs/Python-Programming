import random
word_list=['elma','armut','portakal','mandalina','kavun']

def get_word():
    word=random.choice(word_list)
    return word.upper()

def play(word):
    word_display="_"*len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=6

    print(f"lets start. You have {tries} rights.  ")
    print(word_display)
    print("\n")

    while not guessed and tries>0:
        guess=input("Please, make a gues: ").upper()

        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You made a guess with {guess}")
            elif guess not in word:
                tries-=1
                print(f"{guess} is not in word. You have {tries} rigths.")
                guessed_letters.append(guess)
            else:
                print(f"{guess} is in word")
                guessed_letters.append(guess)
                word_as_array=list(word_display)
                indices=[i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_array[index]=guess
                word_display="".join(word_as_array)
                if "_" not in word_display:
                    guessed=True







        elif len(guess)==len(word) and guess.isalpha():
            if guess==word:
                guessed=True
                word_display=word
            elif guess in guessed_words:
                print(f"You tried {guess}")

            else:
                print("Wrong answer")
                guessed_words.append(guess)
                tries-=1


        else:
            print("Invalid gues...")

        print(word_display)
        print("\n")






    if guessed:
        print("You won")


    else:
        print(f"You lost. Correct answer is {word}")


def main():
    word=get_word()
    play(word)
    while input("would like to do it again? (Y/N): ").upper()=="Y":
        word = get_word()
        play(word)
main()