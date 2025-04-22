import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'<iframe\s?.*\s?src="http[s]?://[w]{0,3}\.?youtube\.{1}com/[a-z]+/\w+"',s):
        match = re.findall(r'http[s]?://[w]{0,3}\.?youtube\.{1}com/[a-z]+/\w+',s)
        modified_url = match[0].split('/')
        return f"https://youtu.be/{modified_url[-1]}"
    else:
        sys.exit(1)



if __name__ == "__main__":
    main()