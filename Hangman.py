import random

HANGMAN_PICS = [                                                ### CHANGE - Used my hangman figures instead and reformatted to make it neat
    "   +---+\n       |\n       |\n       |\n      ===",
    "   +---+\n   O   |\n       |\n       |\n      ===",
    "   +---+\n   O   |\n   |   |\n       |\n      ===",
    "   +---+\n   O   |\n  /|   |\n       |\n      ===",
    "   +---+\n   O   |\n  /|\  |\n       |\n      ===",
    "   +---+\n   O   |\n  /|\  |\n  /    |\n      ===",
    "   +---+\n   O   |\n  /|\  |    [GAME OVER! x_X] \n  / \  |\n      ==="
    ]
words = "ant baboon badger bat bear beaver camel cat clam cobra".split()
 
def getRandomWord(wordList):
      # This function returns a random string from the passed list strings.
      wordIndex = random.randint(0, len(wordList) - 1)
      return wordList[wordIndex]
 
def displayBoard(missedLetters, correctLetters, secretWord):
      print(HANGMAN_PICS[len(missedLetters)])
      print()
 
      print('Missed letters:', end=' ')
      for letter in missedLetters:
          print(letter, end=' ')
      print()
 
      blanks = '_' * len(secretWord)
 
      for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
         if secretWord[i] in correctLetters:
              blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
 
      for letter in blanks: # Show the secret word with spaces in between each letter.
          print(letter, end=' ')
      print()
 
def getGuess(alreadyGuessed):
      # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
      while True:
          print('Guess a letter.')
          guess = input()
          guess = guess.lower()
          if len(guess) != 1:
             print('Please enter a single letter.')
          elif guess in alreadyGuessed:
             print('You have already guessed that letter. Choose again.')
          elif guess not in 'abcdefghijklmnopqrstuvwxyz':
              print('Please enter a LETTER.')
          else:
              return guess
 
def playAgain():
      # This function returns True if the player wants to play again; otherwise, it returns False.
      print('Do you want to play again? (yes or no)')
      return input().lower().startswith('y')
 
 
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)

gameIsDone = False
 
while gameIsDone is False:
    displayBoard(missedLetters, correctLetters, secretWord)
 
      # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)
 
    if guess in secretWord:
        correctLetters = correctLetters + guess
         # Check if the player has won.
        foundAllLetters = True

        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
        
        if foundAllLetters:
            print("_____________________\n   Y O U   W O N !\n")            ### CHANGE - Design addition to counteract extra scoreboard print
            displayBoard(missedLetters, correctLetters, secretWord)         ### CHANGE - extra display & Stat section added - correct missing last word
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            print('________________\nYOUR STATS\nTotal Guesses: ' + str(len(missedLetters) + len(correctLetters)) + 
            '\nWrong Guesses: ' + str(len(missedLetters)))
            gameIsDone = True
    else:                                                                   ### CHANGE - Moved the else condition in line with the first 'If'. Problem: Game wasn't ending; It was nested incorrectly
        missedLetters = missedLetters + guess
      
        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
         
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' +
            str(len(correctLetters)) + ' correct guesses,the word was "' + secretWord + '"')
            gameIsDone = True
  
            # Ask the player if they want to play again (but only if the game is done).
            if gameIsDone:
                if playAgain():

                    missedLetters = ''
                    correctLetters = ''
                    gameIsDone = False
                    secretWord = getRandomWord(words)
                else:
                    break
