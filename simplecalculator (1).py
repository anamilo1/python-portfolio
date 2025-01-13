#Simple Calculator
#Ana Milosevic
#11/18/24

#NOTES

#While Loops
#Only want to loop under certain conditions

#Example 1:
# i = 0
# while i < 10:
#     print("i is " + str(i))
#     i = i + 1

#Example 2:
# while True: #Forever Loop
#     print("This will loop forever")
#     break


#Functions
#Simple Calculator

#Init
#Functions
#Main

#While Loops
#Only want to loop under certain conditions

#Example 1:
#i = 0
#while i < 10:
    #print("i is " + str(i))
    #i = i +1

#Example 2:
#while True: #Forever Loop
    #print("This will loop forever")
    #break

#Function
#Adds two numbers together and prints them out
def add(num1, num2):
    result = int(num1) + int(num2)
    print(result)
def subtract(num1, num2):
    result = int(num1) - int(num2)
    print(result)
def multiply(num1, num2):
    result = int(num1) * int(num2)
    print(result)
def divide(num1, num2):
    result = int(num1) / int(num2)
    print(result)
#Main
print("Welcome to simple calculator")
while True:
    print("Please select an operation")
    print("""1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit""")
    operation = int(input("(1-5) option: "))
    if operation == 1:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        add(int1, int2)
    if operation == 2:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        subtract(int1, int2)
    if operation == 3:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        multiply(int1, int2)
    if operation == 4:
        int1 = int(input("Enter the first number: "))
        int2 = int(input("Enter the second number: "))
        divide(int1, int2)
    if operation == 5:
        quit()
