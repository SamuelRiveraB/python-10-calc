from art import logo

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2


exit = False
count = 0

while exit == False:
  if count == 0:
    print(logo)
    num1 = float(input("What's the first number?: "))
  else:
    num1 = count
  print("+\n-\n*\n/")
  op = input("Pick an operation: ")
  if op == "+" or op == "-" or op == "*" or op == "/":
    num2 = float(input("What's the next number?: "))
    if(op == "+"):
      res = add(num1,num2)
      print(f"{num1} + {num2} = {res}")
      count = res
    elif(op == "-"):
      res = subtract(num1,num2)
      print(f"{num1} - {num2} = {res}")
      count = res
    elif(op == "*"):
      res = multiply(num1,num2)
      print(f"{num1} * {num2} = {res}")
      count = res
    elif(op == "/"):
      res = divide(num1,num2)
      print(f"{num1} / {num2} = {res}")
      count = res
    conti = input(f"Type anything to continue with {count} or type 'n' to start a new calculation: ")
    if conti == 'n':
      count = 0
  else:
    print("Unknown operator, closing program...")
    break