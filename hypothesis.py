num = int(input("Enter an integer number: "))

step = 0

while num != 1:

    if num % 2 == 0 :
        #print("Even")
        num = int(num / 2)
        print(num)
        step = step + 1

    else:
        #print("Odd")
        num = int(3 * num + 1)
        step = step + 1
        print(num)

print(f"Steps: {step}")

