
month = int(input("Enter the month in numeric form: "))
day = int(input("Enter the day in numeric form: "))
year = int(input("Enter the year in two numerical digits (for example: 98, 20, 21): "))


if month>12 or month<1:
    print("Error: Invalid Month Input")
elif day<1 or day>31:
    print("Error: Invalid Day Input")
elif year<10  or year>100:
    print("Error: Invalid Year Input")
else:
    print("Success: Congratulations! you entered the correct date.")
    print("The date is ", month,'/', day,'/', year)
