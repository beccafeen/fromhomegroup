import random
import finalpro_hangman
import Number_guessing_game
import Fortune
import odds_evens
import Quizhub



def game():

    global start
    different_game = True
    while different_game == True:
        start = input('What do you want to play?\nEnter a, b, c, d, e, f, or g \n a. Hangman\n b. Odds n Evens\n c. Quizhub\n d.Fortune Telling Game\n e.Number Guessing Game\n f.Battleship\n g. Tic-Tac-Toe\n')
        print()

        if start == 'a':
            finalpro_hangman.play_hangman()
        elif start == 'b':
            odds_evens.odds_and_evens()
        elif start == 'c':
            play_another_quiz = True
            while play_another_quiz == True:
                movie = Quizhub.movie_quiz
                profession = Quizhub.profession_quiz
                makeup = Quizhub.makeup_quiz
                personality = Quizhub.personality_quiz
                age = Quizhub.age_quiz
                princess = Quizhub.disney_princess_quiz
                quarantine = Quizhub.quarantine_quiz
                random.choice([movie,profession,makeup,personality,age,princess,quarantine])()
                answer = input("Would you like to play a different quiz? ")
                if answer == "yes" or answer == "y":
                    play_another_quiz = True
                    continue
                else:
                    play_another_quiz = False
                    print("Thanks for playing!")
                    continue
                continue
        elif start == 'd':
            Fortune.fortune_telling()
        elif start == 'e':
            Number_guessing_game.number_guessing()
        elif start == 'f':
            print('You have three shots to beat me!')
            import Battleship
            Battleship.battleship()
        elif start == 'g':
            import Tic_tac_toe
        else:
            print('Ok, no game for you')
            return

        print("Would you like to play a different game?")

        response = input("> ").lower()
        if response == "yes" or response == "y":
            different_game = True

        else:
            different_game = False
            print('Ok, no game for you')
            return

game()
