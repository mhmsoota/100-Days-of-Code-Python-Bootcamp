from replit import clear
from art import logo

def select_the_number():
  '''
    Returns a Randomly Selected Number which will be the main number to be guessed. Does not take any inputs
  '''
  from random import randint
  return randint(1,100)

def is_it_guessed (guessedNumber, actualNumber):
  '''
    Takes the guessed number and actual number as an input and returns -100 if guessed correctly and -1 if incorrect. The returned number should be added to the number of guesses.
  '''
  if guessedNumber == actualNumber:
    return -100
  elif guessedNumber > actualNumber:
    print("It's High!")
  elif guessedNumber < actualNumber:
    print("It's Low!")
  return -1

def set_difficulty_level():
  '''
    Asks the user what difficulty level they want, and returns the number of attempts based on that. Does not take any inputs
  '''
  diff = input("Choose a Level of Difficulty. Type 'easy' or 'hard'.").lower()
  if diff == "easy":
    return 10
  else:
    return 6



def start_the_game():
  '''
    Clears the screen and plays one game repitition
  '''
  
  clear()
  print(logo)
  print("\nWelcome to Guess-the-Number Game!\nI will be thinking of number between 1 and 100.")
  attempts = set_difficulty_level()
  thenumber = select_the_number()
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess this number")
    guessedNumber = int(input("Make a Guess: "))
    attempts += is_it_guessed(guessedNumber,thenumber)

  if attempts < 0:
    print("Yippie! You guessed it right!")
  else:
    print("You have exhausted all the attempts! Let's try again, maybe?")


playAgain = "yes"
while playAgain == "yes":
  start_the_game()
  playAgain = input("Do you want to try playing all over again? \nType 'yes' or 'no'\n").lower()
