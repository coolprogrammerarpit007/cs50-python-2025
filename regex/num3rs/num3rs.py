import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$",ip):
        numbers = ip.split(".")
        for number in numbers:
            if not int(number) > 255:
                continue
            else:
                return False
            
        return True
    return False
       

if __name__ == "__main__":
    main()