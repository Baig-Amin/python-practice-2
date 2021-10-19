def areacalculator():

    #global shape, area, pi

    area = 0.00
    pi = 3.1416

    print("\nSelect Option: ")
    print("1. Square")
    print("2. Circle")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Exit")

    shape = input("Enter the choice you want to calculate : ")

    if shape in ('1', '2', '3', '4', '5'):

        if shape == '1':
            side = float(input("Enter the value of side: "))
            area = area + (side ** 2)
            print("Square: "+"%.2f" %area)

        elif shape == '2':
            radius = float(input("Enter the value of radius: "))
            area = area + (2 * pi * radius)
            print("Circle: "+"%.2f" %area)
    
        elif shape == '3':
            length = float(input("Enter the value of length: "))
            width = float(input("Enter the value of width: "))
            area = area + (length * width)
            print("Rectangle: "+"%.2f" %area)
    
        elif shape == '4':
            base = float(input("Enter the value of base: "))
            height = float(input("Enter the value of height: "))
            area = area + (.5 * base * height)
            print("Triangle: "+"%.2f" %area)
        
        elif shape == '5':
            quit()

    else:
        print("Invalid Input")


while True:
    areacalculator()