import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try: 
        if match := re.findall(r"(\d{1,2})(?:\:([0-5]{1,2}))?\s(AM|PM) to (\d{1,2})(?:\:([0-5]{1,2}))?\s(PM|AM)",s,re.IGNORECASE):
        
            start_period = match[0][2]
            start_time = match[0][0] if match[0][0] else 0
            if start_period == "PM" and start_time != "12":
                start_time = (int(start_time) + 12)
            start_mins = match[0][1] if match[0][1] else 0
            end_time = match[0][3] if match[0][3] else 0
            end_mins = match[0][4] if match[0][4] else 0
            end_period = match[0][5]
            if end_time != '12' and end_period == 'PM':
                end_time = (int(end_time) + 12) if (int(end_time) + 12) < 24 else 0
            if end_period == "AM" and end_time != "12":
                end_time = match[0][3] if match[0][3] else 0

            if int(end_time) == 12 and end_period == "PM":
                end_time = 12

            if start_time == "12" and start_period == "AM":
                start_time = 0

            
            return f"{int(start_time):02}:{int(start_mins):02} to {int(end_time):02}:{int(end_mins):02}"

        

        else:
            raise ValueError
        

    except ValueError:
        raise ValueError

    


if __name__ == "__main__":
    main()