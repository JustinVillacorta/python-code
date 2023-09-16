import calendar

# Get input from the user
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

# Display the calendar
cal = calendar.month(year, month)
print(cal)
