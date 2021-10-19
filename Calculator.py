def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x, y):
    return x / y

def take_input():

    global num1, num2

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    return num1, num2

while True:

    print("\nSelect Option: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice in ('1', '2', '3', '4', '5'):

        if choice == '1':
            take_input()
            print(f"{num1} + {num2} = {add(num1,num2)}")
        
        elif choice == '2':
            take_input()
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        
        elif choice == '3':
            take_input()
            print(f"{num1} * {num2} = {mul(num1,num2)}")

        elif choice == '4':
            take_input()
            print(f"{num1} / {num2} = {div(num1,num2)}")

        elif choice == '5':
            quit()
    
    else:
        print("Invalid Input")
