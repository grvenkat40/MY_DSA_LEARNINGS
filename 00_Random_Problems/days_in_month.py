def days_in_month(month, year):
    if month == 2:
        if (year%400 == 0) or (year%4==0 and year%100!=0):
            return 29
        else:
            28
    elif month in [4, 6, 9,11]:
        return 30
    else:
        return 31
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

print("Number of days:", days_in_month(month, year))