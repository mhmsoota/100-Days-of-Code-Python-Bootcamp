#Calculator
def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

from replit import clear

cont = "y"
answer = None
while cont == 'y' or cont == 'n':
  if answer == None:
    num1 = float(input("First Number: "))
  else:
    num1 = answer
    print(f"First Number: {num1}")
  num2 = float(input("Second Number: "))
  for keys in operations:
    print(keys)
  operation_symbol = input("Pick an operation from above : ")
  answer = operations[operation_symbol](num1,num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

  cont = input(f"Type 'y' to continue calculating with {answer}, 'n' to start afresh and any other key to stop")
  if cont == 'n':
    answer = None
  clear()
