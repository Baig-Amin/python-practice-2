def fahrenheit(x):
    result = (x * 1.8) + 32
    print("%.1f degree Fahrenheit" %result)

def celsius(x):
    result = (x - 32) / 1.8
    print("%.1f degree Celsius" %result)

print("......Welcome to temperature converter......")

while True:

    print("\nSelect Option")
    print("1. Celsious to Fahrenheit")
    print("2. Fahrenheit to elsious")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice in ('1', '2', '3'):

        if choice == '1':
            temp = float(input("Enter the celsius degree: "))
            fahrenheit(temp)
        
        elif choice == '2':
            temp = float(input("Enter the fahrenheit degree: "))
            celsius(temp)
            
        elif choice == '3':
            quit()
    
    else:
        print("Invalid Input")
