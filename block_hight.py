blocks = int(input("Enter the number of blocks: "))
i = 1
height = 0

while blocks > 0:

    if i > blocks:
        break

    blocks = blocks - i

    i = i + 1
    height = height + 1

print("The height of the pyramid:", height)
