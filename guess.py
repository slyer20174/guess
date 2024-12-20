import random
number=random.randint(1,100)
def intro():
    print("lets play a game, guess the number between 1 to 100 ")
    if number %2==0:
        print("its an even number")
    else:
        print("its an odd number")
    print("guess the number")

def pick():
    Guess_Taken=0
    while Guess_Taken<6:
        try:
            guess=int(input("guess the number"))
            if guess<=100 and guess>=1:
                Guess_Taken=Guess_Taken+1
                if Guess_Taken<6:
                    if guess<number:
                        print("the guess is too less")
                    if guess>number:
                        print("the guess is too high")
                    if guess!=number:
                        print("try again")
                    if guess==number:
                        print("your correct yayayyayayayayayyayayayayayayayayayayayayay")
                        break
        except:
            print(" i dont think the number is in my range")

play_again="yes"
while play_again=="yes":
    intro()
    pick()
    print("do you want to play again")
    play_again=input()