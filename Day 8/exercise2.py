#Write your code below this line 👇
from math import floor

def prime_checker(number):
  for i in range(2,floor(number/2)):
    if number%i==0:
      print("It is not a prime number.")
      return
  print("It is a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



