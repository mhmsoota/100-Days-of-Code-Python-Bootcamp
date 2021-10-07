rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]
playerChoice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors")
playerChoice = list[int(playerChoice)]
print(playerChoice)

from random import choice
computerChoice = choice(list)
print("Computer Chose:\n" + computerChoice)

if playerChoice == computerChoice:
  print("It's a draw")
elif (playerChoice==rock and computerChoice==paper) or (playerChoice==paper and computerChoice==scissors) or (playerChoice==scissors and computerChoice==rock):
  print("You lose")
else:
  print("You win")

