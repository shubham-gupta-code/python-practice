# Q14. Check if a given year is a leap year or not.

year = int(input("Enter a year: "))

if (year%400==0) or (year%4==0 and year%100!=0):
    print(year, "is a Leap Year")

else:
    print(year, "is Not a Leap Year")

# you can google to know whether a year is leap year or not.
