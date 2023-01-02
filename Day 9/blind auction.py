from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

bidders = {}

def add_to_bidders():
  bidders[input("Your Name: ")] = float(input("Your Bid: $"))

print(logo)
moreData = "yes"
while moreData == "yes":
  add_to_bidders()
  moreData = input("Are there any more bidders? ('yes' or 'no')\n").lower()
  clear()
  if moreData=="yes":
    continue
  largest = ["",-1]
  for key in bidders:
    if bidders[key] > largest[1]:
      largest[1] = bidders[key]
      largest[0] = key
  print(f"Winner of this Bid: {largest[0]}\nBidding Amount: ${largest[1]}")
