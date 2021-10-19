print("\n..........Welcome. Add your item and price to see total cost...........")

print("\nStart adding you item and price. or press 'e' to see the total.")

item = {}
total = 0
i = 1

#n = int(input("\nEnter the number of items: "))

#for i in range(1,n+1):
while i > 0:

    k = input("\nEnter Product name: ")
    if k == 'e':
        break
    v = int(input("Enter product price: "))

    item.update({k:v})

total = sum(item.values())

print(f"\n {item}")
print(f"Total cost = {total}")