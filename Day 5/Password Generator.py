#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

from random import choice

for i in range(nr_letters):
  password+=choice(letters)
for i in range(nr_symbols):
  password+=choice(symbols)
for i in range(nr_numbers):
  password+=choice(numbers)

print("The new Easy-Level Strong Password is: "+ password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Angela's method

from random import shuffle

password = ['']

for i in range(nr_letters):
  password.append(choice(letters))
for i in range(nr_symbols):
  password+=choice(symbols)
for i in range(nr_numbers):
  password+=choice(numbers)

shuffle(password)

password = ''.join(password)
print("The new Strong Password, hard level (Angela's method) is: " + password)

#My method
password = ""

for i in range(nr_letters+nr_numbers+nr_symbols):
  nextChar = choice([letters,numbers,symbols])
  if nr_letters==0 and nextChar==letters:
    nextChar=numbers
  if nr_numbers==0 and nextChar==numbers:
    nextChar=symbols
  if nr_symbols==0 and nextChar==symbols:
    nextChar=letters
  
  if nextChar==letters:
    password+=choice(letters)
    nr_letters-=1
  elif nextChar==numbers:
    password+=choice(numbers)
    nr_numbers-=1
  elif nextChar==symbols:
    password+=choice(symbols)
    nr_symbols-=1

print("The new Strong Password, hard level (my method) is: " + password)
