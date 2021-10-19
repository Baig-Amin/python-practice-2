# Welcome massage
print("\n..........Welcome to DBBL ATM banking..........\n")

# Reading id from user
id = int(input("\nEnter your 4 digit account pin: "))

n = 4
for i in range(1, n):
    if id > 1000 and id < 9999:
        print("Accepted")
        break

    else:
        k = 3-i
        print(f"Invalid Id.. Re-enter. You have only {k} chance left.")
        id = int(input("\nEnter your 4 digit account pin: "))