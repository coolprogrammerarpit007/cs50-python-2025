import re
import sys

def main():
    print(count(input("Text: ")))


def count(s):
    s = s.strip()
    if match:= re.findall(r"\b(um)\b",s,re.IGNORECASE):
        return len(match)

    else:
        return 0






if __name__ == "__main__":
    main()