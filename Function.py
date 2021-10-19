#Check the input year is leap year or not.

def is_leap(year):

    if year >= 1900 and year <= 1000000:

        if year % 4 == 0:
        
            if year % 100 == 0:
            
                if year % 400 == 0:

                    return True
            
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        quit()

year = int(input())

print(is_leap(year))