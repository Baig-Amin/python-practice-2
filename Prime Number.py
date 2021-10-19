num = int(input("Enter a number to check whether it is prime or not: "))

for i in range(2, int((num/2))+1):

    if num % i == 0:
        print("Not a prime number.")
        break
else:
    print("Prime number.")