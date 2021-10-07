print('''
                             \
                              \
                               \\
                                \\
                                 >\/7
                             _.-(6'  \
                            (=___._/` \
                                 )  \ |
                                /   / |
                               /    > /
                              j    < _\
                          _.-' :      ``.
                          \ r=._\        `.
                         <`\\_  \         .`-.
                          \ r-7  `-. ._  ' .  `\
                           \`,      `-.`7  7)   )
                            \/         \|  \'  / `-._
                                       ||    .'
                                        \\  (
                                         >\  >
                                     ,.-' >.'
                                    <.'_.''
                                      <'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'").lower()

if choice == "left":
  #Continue in the game
  choice = input("You've come to a lake. There's an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim accross").lower()
  
  
  if choice=="wait":
    choice = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
    
    if choice == "red":
      print("It's a room full of fire. Game Over")
    elif choice == "yellow":
      print("You found the treasure, It's all yours! You win!")
    elif choice == "blue":
      print("The door closes behind you. No escape! Game Escape")
    else:
      print("You failed to make proper decision, so you were killed by the protectorm of the treasure")
  
  else:
    print("You got attacked by an angry trout. Game Over.")


else:
  print("You fell into a hole. Game Over.")