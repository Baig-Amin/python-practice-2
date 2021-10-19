#The included code stub will read an integer, n, from STDIN.
#Without using any string methods, try to print the following:
#123...n Exm: n=5 output: 12345

n = int(input())

if n >= 1 and n <= 150:

    for i in range(1,n+1):
        print(i,end="")

        