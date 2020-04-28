def fortune_telling():
    play_again = True
    while play_again == True:
        #fortune Telling Game
        reading = ["You will become rich in coming years","Your smile will tell you what makes you feel good.","You will become PM or president of your country","You will become poor in coming years","You will marry soon"]
        n=int(input("Enter number from 1 to "+str(len(reading))))
        print(reading[n-1])
        answer = input("Would you like to play again? ")
        if answer == "yes" or answer == "y":
            play_again = True
        else:
            play_again = False
            print("Thanks for playing!")
            return
#fortune_telling()
