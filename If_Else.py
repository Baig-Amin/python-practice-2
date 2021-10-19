#Given an integer,n, perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird 

import math
import os

n = int(input())

if n >= 1 and n <=100:

    if n % 2 == 0:

        if n >=2 and n <=5:
            print("NOt Weird")

        elif n >=6 and n <=20:
            print("Weird")

        elif n > 20:
            print("NOt Weird")

    else:
      print("Weird")