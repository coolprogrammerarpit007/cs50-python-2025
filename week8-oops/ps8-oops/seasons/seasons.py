from datetime import date,datetime
from num2words import num2words
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


def leap_days(start):
    start_date = date.fromisoformat(start)
    end = date.today()
    end_date = date.fromisoformat(str(end))
    remaining_days = (end_date - start_date).days
    return (remaining_days)

def numbers_to_words(number):
    mins_in_words = (num2words(number)).split(' ')
    formatted_words = ""
    for word in mins_in_words:
        if word != "and":
            formatted_words += word + " "

    return formatted_words.capitalize()
def main():
    birth_date = input("Enter Date: ")
    if is_valid_date(birth_date):
        days_in_the_year = leap_days(birth_date)
        minutes_in_year = int(days_in_the_year) * 24 * 60
        print(f"{numbers_to_words(minutes_in_year)} minutes")
    else:
        sys.exit(1)
    

if __name__ == "__main__":
    main()