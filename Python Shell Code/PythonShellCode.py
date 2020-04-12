import random
def generate_random_word():
    filename = "words.txt"
    file = open(filename,"r")  # the "r" specifies we will be reading from it, not writing to it
    text = file.read()
    words = text.split()
    return random.choice(words)
generate_random_word()

word = generate_random_word()
letters = [i for i in word]
#print(word)
#print(letters)

def print_word(word,guessed_letter):  
    for i in word:
        if i != guessed_letter:
            word = word.replace(i,"-")
        elif i == guessed_letter:
            word = word.replace(i, guessed_letter)
    print(word)
print_word(word,"e")    

guessed_letters = []
def guessed_letters_str(guessed_letters):  
    
    # initialize an empty string 
    str_guessed_letters = '' 
    
    # return string   
    return (str_guessed_letters.join(guessed_letters)) 
guessed_letters_str(guessed_letters)
        
def play_hangman():

    
    HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /   \ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /   \ 
|   | 
|    
|
|
|
--------
""",
"""
-----
|   |
|   0
| /   \ 
|   |  
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /   \ 
|   |  
|  | |
|
--------
""")
    want_to_play = True
    play = input('Do you want to play hangman?'.lower())

    if play not in ("yes","y"):
        want_to_play = False
        print('Goodbye')
        
        
    
    while want_to_play == True:
        print(HANGMAN[0])
        word = generate_random_word()
        #print(word)
        word_guessed = []
        for letter in word:
            word_guessed.append("-")
        #joined_word = None # joins the words in the list word_guessed
        attempts = (len(HANGMAN) - 1)  
        
        
        letter = input('Please choose a letter') #"ask the user for a letter"
        done = False
        while not done:
            
            while (attempts != 0 and set(word) != set(guessed_letters_str(guessed_letters))):
                if letter in word:
                    print(("\nYou have {} attempts remaining\n\n").format(attempts))
                else:
                    print(("\nYou have {} attempts remaining\n\n").format(attempts-1))
                

                if not letter.isalpha(): # check the input is a letter. Also checks an input has been made.
                    attempts -= 1
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])
                    print("That is not a letter. Please try again.")
                    
                elif len(letter) > 1: # check the input is only one letter
                    attempts -= 1
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])
                    print("That is more than one letter. Please try again.")
                    
                elif letter in guessed_letters:
                    attempts -= 1
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts]) #subtract one from guesses_left
                    print('Sorry, you have already guessed that letter') #and tell them they already guessed that letter

                elif letter not in word:
                    attempts -= 1
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])
                    guessed_letters.append(letter) #add letter to guessed letters
                    print("\nLetters guessed:",guessed_letters)#prints list of guessed letters
                    print('Sorry, that letter is not in this word')#tell user the letter is not in the word

                elif letter in word:
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])
                    guessed_letters.append(letter) #add letter to guessed letters
                    print("\nLetters guessed:",guessed_letters)#prints list of guessed letters               
                    print('Good job! That letter is in the word') #tell user the letter is in the word

                if set(word) <= set(guessed_letters_str(guessed_letters)):
                    print(HANGMAN[(len(HANGMAN) - 1) - attempts])
                    done = True 
                    print('Good job! You won. The word was ' +  word ) #set done to be true and tell the user they won!

                elif attempts <= 0:#the number of guesses left is zero
                    print('Sorry, you lost')#set done to be true and tell the user they lost!"
                    return
                    

                else:
                    print_word(word,letter)#print the word with a dash for each letter not in guessed_letters
                    #there is a bug here as it does not print the full word with the correct letters but instead prints a spearate line for each correct letter. Hard to explain but you can test it and see what I mean
                    letter = input('Please choose another letter') #ask the user for another letter"
         
        print("Would you like to play again?")

        response = input("> ").lower()
        if response not in ("yes","y"):
            want_to_play = False
            print('Goodbye')
            
if __name__ == "__main__":
    play_hangman()
