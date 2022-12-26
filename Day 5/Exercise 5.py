#Write your code below this row 👇

for turn in range(1,101):
  if turn%15==0:
    print("FizzBuzz")
  elif turn%3==0:
    print("Fizz")
  elif turn%5==0:
    print("Buzz")
  else:
    print(turn)
