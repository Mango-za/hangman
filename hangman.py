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
  
# check if guess is incorrect (or correct)  
def IsIncorrectGuess(guess: str):
  for n in chosen_word:
    if n == guess:
      return False
  else:
    return True    
  
# check if guess is repeated
def IsRepeatedGuess(guess: str, incorrect_list: list, correct_list: list):
  if guess in incorrect_list or guess in correct_list:
    return True
  
# display game board
def DisplayGameBoard(lives: int, guess_spaces: list, incorrect_guesses: list):
  print(HANGMANPICS[6 - lives])
  print(*guess_spaces, sep=' ')
  print(*incorrect_guesses, sep=', ')

while True:

  game_over = False
  incorrect_guesses = []
  correct_guesses = []

  # choose word from word_list
  chosen_word = random.choice(word_list.WORDLIST)

  # number of lives
  lives = 6

  # print game board
  word_length = len(chosen_word)
  guess_spaces = ["_"] * word_length

  DisplayGameBoard(lives, guess_spaces, incorrect_guesses)

  while not game_over:

    # display game over screen (loss)
    if lives == 0:
      play_again = input(f'''GAME OVER
                         
The word was: {chosen_word}
Would you like to play again? (Y/N)\n''')
      
      # ask if user would like to play again
      if play_again.upper() == 'Y':
        break
      elif play_again.upper() == 'N':
        game_over = True
        break

    elif not '_' in guess_spaces:
      play_again = input(f'''WELL DONE!

Would you like to play again? (Y/N)\n''')
      
      if play_again.upper() == 'Y':
        break
      elif play_again.upper() == 'N':
        game_over = True
        break

    # takes player guess
    guessed_letter = input("Enter a letter to guess\n")
    if not IsValidGuess(guessed_letter):
      print("Please make valid guess.")  # implement details on why guess is invalid
      continue
    
    if IsRepeatedGuess(guessed_letter, incorrect_guesses, correct_guesses):
      print("This letter has already been guessed.")
      continue

    if IsIncorrectGuess(guessed_letter):
      lives -= 1  # subtract life for incorrect guess

      # add incorrect guess to list
      incorrect_guesses.append(guessed_letter)

      # print incorrect guess list
      DisplayGameBoard(lives, guess_spaces, incorrect_guesses)
      continue

    if not IsIncorrectGuess(guessed_letter):
      # add correct guess to list
      correct_guesses.append(guessed_letter)

      # find all correct positions of guessed letter
      for n in range(len(chosen_word)):
        if guessed_letter == chosen_word[n]:
          # replace blank space with guessed letter
          guess_spaces[n] = guessed_letter

      DisplayGameBoard(lives, guess_spaces, incorrect_guesses)
      continue
  
  if game_over:
    break