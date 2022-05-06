def addition():
    print("Enter a Number: ")
    num1=int(input(""))
    print("Enter another Number: ")
    num2 = int(input(""))
    ans = num1 + num2
    print("Answer is: ", ans)

def subtraction():
    print("Enter a Number: ")
    num1=int(input(""))
    print("Enter another Number: ")
    num2 = int(input(""))
    ans = num1 - num2
    print("Answer is: ", ans)

def multiplication():
    print("Enter a Number: ")
    num1=int(input(""))
    print("Enter another Number: ")
    num2 = int(input(""))
    ans = num1 * num2
    print("Answer is: ", ans)

def division():
    print("Enter a Number: ")
    num1=int(input(""))
    print("Enter another Number: ")
    num2 = int(input(""))
    if num2!=0:
        ans = num1 / num2
        print("Answer is: ", ans)
    else:
        print("Error: You cannot divide by '0'")

repeat = 1
while repeat == 1:
    print('''1. Addition
2. Subtraction
3. Multiplication
4. Division''')
    choice = int(input(""))

    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    else:
        division()

    repeat=int(input('''Do more math?
1. Yes
2. No
'''))
