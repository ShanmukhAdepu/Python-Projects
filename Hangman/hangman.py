def isWordGuessed(secretWord, lettersGuessed):
    
    for i in lettersGuessed:
        
        if i  not in secretWord:
            
            return False

    return True

def getGuessedWord(secretWord, lettersGuessed):

    ans = str()
    for i in secretWord:
        
        if i in lettersGuessed:
           
            ans += i
        
        else:
           
            ans += "_"
  
    return ans

import string

def getAvailableLetters(lettersGuessed):

    ans = str()
    for i in string.ascii_lowercase:
       
        if i not in lettersGuessed:
           
            ans += i
    
    return ans

def printHangman(numGuesses, secretWord, lettersGuessed):

    if numGuesses == 5:
        print("           O")
        print("Oops now there's a head! Sadly that letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
        return
    elif numGuesses == 4:
        print("           O")
        print("           |")
        print("Oh no now there's torso! Sadly that letter is not in my word either: " + str(getGuessedWord(secretWord, lettersGuessed)))
        return
    elif numGuesses == 3:
        print("           O")
        print("          /|")
        print("Watch out thats the first hand! You are getting dangerously close to losing: " + str(getGuessedWord(secretWord, lettersGuessed)))
        return
    elif numGuesses == 2:
        print("           O")
        print("          /|\\")
        print("Both arms! Be more careful!: " + str(getGuessedWord(secretWord, lettersGuessed)))
        return
    elif numGuesses == 1:
        print("           O")
        print("          /|\\")
        print("          /")
        print("A leg too! One more strike and YOU'RE OUT!: " + str(getGuessedWord(secretWord, lettersGuessed)))
        return
    elif numGuesses == 0:
        print("           O")
        print("          /|\\")
        print("          / \\")
        print("Thats the full body: " + str(getGuessedWord(secretWord, lettersGuessed)))
        return

def rprintHangman(numGuesses):

    if numGuesses == 6:
        print("nonexistant")
        return
    elif numGuesses == 5:
        print("           O")
        return
    elif numGuesses == 4:
        print("           O")
        print("           |")
        return
    elif numGuesses == 3:
        print("           O")
        print("          /|")
        return
    elif numGuesses == 2:
        print("           O")
        print("          /|\\")
        return
    elif numGuesses == 1:
        print("           O")
        print("          /|\\")
        print("          /")
        return
    elif numGuesses == 0:
        print("           O")
        print("          /|\\")
        print("          / \\")
        return

def hangman(secretWord):

    print("Loading word list from file...")
    print("55900 words loaded. ")
    print("Welcome to the game, Hangman!")

    secWordLength = len(secretWord)

    print("I am thinking of a word that is " + str(secWordLength) + " letters long.")

    print("------------")

    lettersGuessed = []
    availableLetters = string.ascii_lowercase
    availableGuesses = 6
    done = False

    while(done == False):

        print("You have " + str(availableGuesses) + " guesses left.")
        print("Available Letters: " + str(availableLetters))
        user_input = input("Please guess a letter: ")
        print("Hangman: ")

        if user_input not in getAvailableLetters(lettersGuessed):
            rprintHangman(availableGuesses)
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
        
        elif user_input not in secretWord:
            lettersGuessed += user_input
            availableLetters = getAvailableLetters(lettersGuessed)
            availableGuesses -= 1
            printHangman(availableGuesses, secretWord, lettersGuessed)
        
        elif user_input in secretWord:
            
            lettersGuessed += user_input
            availableLetters = getAvailableLetters(lettersGuessed)
            rprintHangman(availableGuesses)
            print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
        
        print("------------")

        if getGuessedWord(secretWord, lettersGuessed) == secretWord or availableGuesses == 0:
            done = True
    
    if availableGuesses == 0:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")
    
    if getGuessedWord(secretWord, lettersGuessed) == secretWord:
        print("Congratulations, you won!")
    
    print(" ")


userin = input("Would you like to begin this game of hangman?: ")
userin = userin.lower()

if "y" in userin:
    hangman('tact')
else:
    print("Very Well. See you soon!")



