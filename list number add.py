a=[]
total = 0

for i in range(0,5):
    name = input("Enter name: ")
    num = input("Enter number: ")
    num1 = int(num)
    a.append(name)
    a.append(num1)

for x in range(0,len(a)):
    total = total + a[x]
#total = sum(a[num1])
print(total)
