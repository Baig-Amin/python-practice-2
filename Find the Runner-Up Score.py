#Given the participants' score sheet for your University Sports Day,
#you are required to find the runner-up score.
#You are given n scores.
# Store them in a list and find the score of the runner-up.
#The first line contains n.
#The second line contains an array A[] of n integers each separated by a space.

n = int(input())

if n >= 2 and n <= 10:

    arr = map(int, input().split())
    arr = list(set(list(arr)))
    ar = len(arr)
    arr = sorted(arr)
    print(arr[ar-2])

else:
    quit()