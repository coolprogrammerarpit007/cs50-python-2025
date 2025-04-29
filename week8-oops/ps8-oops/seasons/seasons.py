from datetime import date
import re
import inflect
import sys

#  function to check if date is valid or not.

def is_valid_date(date_str):
    if re.search(r'[0-9]{4}-[0-9]{2}-[0-9]{2}',date_str):
        year,month,day = date_str.split("-")
        if int(month) > 12 or int(day) > 31:
            return False
        else:
            return True
    else:    
        return False


#  method to get the days b/w two dates.

def get_minutes(start_year):
    start_year = date.fromisoformat(start_year)
    today = date.today()

    days = (today - start_year).days
    minutes = days * 24 * 60
    return minutes


def main():
    birth_date = input("Date of Birth: ")
    if is_valid_date(birth_date):
        minutes_total = get_minutes(birth_date)
        p = inflect.engine()
        in_words = p.number_to_words(minutes_total, andword="")
        in_words = in_words.capitalize()
        return f"{in_words} minutes"

    else:
        print("Invalid date")
        sys.exit(1)


if __name__ == "__main__":
    print(main())

