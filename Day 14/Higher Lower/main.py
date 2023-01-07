from art import logo, vs
from replit import clear
from game_data import data
from random import choice



def screen_printer(score, lost, compareA = None, compareB = None):
  '''
    Prints all the necessary information on screen for the next question, along with next options as required. If the person has lost the game, it simply gives the required output, else, it returns the input for next scenario.
  '''
  clear()
  print(logo)
  if lost == True:
    print(f"Oops! You got it wrong!!\n\n\tScore = {score}")
  else:
    if score > 0:
      print(f"That was Correct! Score: {score}")
    print(f"Compare A:\t{compareA['name']}, {compareA['description']}, from {compareA['country']}")
    print(vs)
    print(f"Against B:\t{compareB['name']}, {compareB['description']}, from {compareB['country']}")

    return input("Who has more follower? Type 'A' or 'B': ").upper()

def check(compareA, compareB, Choice):
  '''
    Takes the number of followers in A and B as input. Returns true if the person is correct, false if wrong
  '''
  global score
  if compareA >= compareB and Choice == 'A':
    score += 1
    return True
  elif compareB >= compareA and Choice == 'B':
    score += 1
    return True
  else:
    return False
  
def assign_data():
  return choice(data)

score = 0
B = assign_data()
lost = False

while lost == False:
  A = B
  B = assign_data()
  while A == B:
    B = assign_data()
  Choice = screen_printer(score, lost, A, B)
  lost = not check(A['follower_count'], B['follower_count'], Choice)

screen_printer(score, lost)
