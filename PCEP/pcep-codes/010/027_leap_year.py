# Leap Year: Logic below - after 1582
# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

input_year = int(input("Enter a year:"))
leap_year = "Leap year"
common_year = "Common year"
output_msg = "Not within the Gregorian calendar period"

if input_year >= 1582: # Starting year
    if input_year % 4 > 0: # Common year for sure
        output_msg = common_year
    elif input_year % 100 > 0: # Divisible by 4 but NOT by 100 : Leap
        output_msg = leap_year
    elif input_year % 400 > 0: # Divisible by 4 and 100 and NOT by 400 : Common
        output_msg = common_year
    else:
        output_msg = leap_year

print(output_msg)

# Test data
# 2000: Leap, 2015: Common, 1999: Common, 1996: Leap, 1580: Not within the Gregorian calendar period