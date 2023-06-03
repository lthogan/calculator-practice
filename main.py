#calculator

print("Welcome to the Python Calculator")

#gets first number

i = 0
while i == 0:
    num1 = input("Enter a number: ")
    try:
        num1 = float(num1)
        i += 1
    except:
        print("You must enter a number")
print(num1)

i = 0
while i == 0:
    operation = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division: ")
    try:
        operation = int(operation)
        if operation == 1 or 2 or 3 or 4:
            i += 1
        else:
            print("Must enter 1, 2, 3, or 4.")
    except:
        print("Must enter 1, 2, 3, or 4.")
print(operation)

i = 0
while i == 0:
    num2 = input("Enter another number: ")
    try:
        num2 = float(num2)
        i += 1
    except:
        print("You must enter a number")
print(num2)

if operation == 1:
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
if operation == 2:
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
if operation == 3:
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
if operation == 4:
    print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
