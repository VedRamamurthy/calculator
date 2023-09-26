OPERATIONS = ("multiply", "divide", "add", "subtract","remainder","exponent")
OPS = ("m","d","s","a","r","e")
operation = ""
operands = ""

def display():
      for i in OPERATIONS:
        num = int(OPERATIONS.index(i)) + 1
        print(num, ".", i)

def get_choice():
  operation =  input("Please choose and operation: ")
  while operation not in OPS:
    print("Incorrect")
    display()
    operation =  input("Please choose and operation: ")
  return operation

def get_numbers():
  num1 = float(input("Enter number: "))
  num2 = float(input("Enter number: "))
  return num1, num2

def multiply(num1, num2):
  print(num1*num2) 

def divide(num1, num2):
  print(num1/num2)

def add(num1, num2):
  print(num1+num2)

def subtract(num1, num2):
  print(num1-num2) 

def exponent(num1, num2):
  print(num1^num2)

def remainder(num1, num2):
  print(num1%num2)
  
display()
operands = get_numbers()
choice = get_choice()

if choice == "mulitply":
  multiply(operands[0],operands[1])
elif choice == "divide":
  divide(operands[0],operands[1])
elif choice == "add":
  add(operands[0],operands[1])
elif choice == "subtract":
  subtract(operands[0],operands[1])
elif choice == "remainder":
  remainder(operands[0], operands[1])
elif choice == "exponent":
  exponent(operands[0], operands[1])
  


