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
  if len(guess) > 1 or len(guess) == 0:
    return False
  elif not guess.isalpha():
    return False
  else:
    return True
  
# check if guess is incorrect  
def IsIncorrectGuess(guess: str):
  for n in chosen_word:
    if n == guess:
      return False
  else:
    return True
    
  
# check if guess is repeated
def IsRepeatedGuess(guess: str, incorrect_list: list):
  if guess in incorrect_list:
    return True
  
game_over = False
incorrect_guesses = []
correct_guesses = []

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
    
    if IsRepeatedGuess(guessed_letter, incorrect_guesses):
      print("This letter has already been guessed.")
      continue

    if IsIncorrectGuess(guessed_letter):
      lives -= 1  # subtract life for incorrect guess
      print(HANGMANPICS[6 - lives] + '\n')
      print(*(["_"] * word_length), sep=" ")

      # add incorrect guess to list
      incorrect_guesses.append(guessed_letter)

      # print incorrect guess list
      print(*(incorrect_guesses))
      
      