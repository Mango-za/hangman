# dictionary of words and images of hangman
import word_list, random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# check if guess is valid
def IsValidGuess(guess: str):
  if len(guess) > 1:
    return False
  
  elif not guess.isalpha():
    return False
     
  else:
    return True
  
game_over = False

while True:
    # choose word from word_list
    chosen_word = random.choice(word_list.WORDLIST)

    # number of lives
    lives = 6

    # print game board
    print(HANGMANPICS[0] + '\n')

    word_length = len(chosen_word)
    print(*(["_"] * word_length), sep=" ")

    while not game_over:
      # takes player guess
      guessed_letter = input("Enter a letter to guess\n")
      if not IsValidGuess(guessed_letter):
        print("Please make valid guess.")  # implement details on why guess is invalid
      
      break