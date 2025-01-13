#Leap Year Checker
#Ana Milosevic
#11/06/24

#Initialiize
#Functions
#If a year is divisible by 4, it is a leap year.
#However, if they year is also divisible by 100, it is not a leap year
#If it is divisible by 400, it is a leap year

def is_leap_year(year):
    #Code goes here
    if year % 400 == 0:
        print("It is a leap year")
    elif year % 100 == 0:
        print("It is not a leap year")
    elif year % 4 == 0:
        print("It is a leap year")

#Main
is_leap_year(2024) #True
is_leap_year(1900) #False
is_leap_year(1600) #True
