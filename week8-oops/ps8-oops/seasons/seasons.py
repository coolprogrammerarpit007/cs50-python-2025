from datetime import date,datetime
# import datetime
import re
import sys
import calendar


#  check if the date is valid or not.

def is_valid_date(date):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    if re.search(pattern,date):
        return True
    
    return False

def remaining_days(start_date,end_date):
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    return (end - start).days

def leap_days(start,end):
    start_year,start_month,start_day = start.split("-")
    end_year,end_month,end_day = end.split("-")

    start_date = date(int(start_year),int(start_month),int(start_day))
    end_date = date(int(end_year),int(end_month),int(end_day))
    leap_count = 0

    start_year = int(start_date.year)
    end_year = int(end_date.year)
    for year in range(start_year,end_year+1):
        if calendar.isleap(year):
            leap_count += 1

    return leap_count

def main():
    birth_date = input("Enter Date: ")
    if is_valid_date(birth_date):
        today = date.today()
        end_date = today.strftime("%Y-%m-%d")
        print(f"Birth Year: {birth_date}")
        print(f"Today: {end_date}")
        days_remaining = remaining_days(birth_date,end_date)
        print(f"Remaining Days: {days_remaining}")
        total_leap_days = leap_days(birth_date,end_date)
        total_days = total_leap_days + days_remaining
        print(f"Total Days: {total_days}")
        sys.exit()

if __name__ == "__main__":
    main()