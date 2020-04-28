#Number guessing game
def number_guessing():
    import random
    play_again = True
    while play_again == True:
        while(True):
            guess = input('Guess a number between 1 to 100: ')
            ran = random.randint(1,101)
            if(guess==ran):
                print("You guessed the exact number\n")
            else:
                print("You guessed the wrong number, better luck next time")
                break
        answer = input("Would you like to play again? ")
        if answer == "yes" or answer == "y":
            play_again = True
        else:
            play_again = False
            print("Thanks for playing!")
            return

#number_guessing()
