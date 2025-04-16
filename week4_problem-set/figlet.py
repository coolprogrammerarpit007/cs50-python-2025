from pyfiglet import Figlet
import sys
import random


def check_valid_font(font_name):
    return Figlet(font=font_name)

try:
    if len(sys.argv) == 3:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and check_valid_font(sys.argv[2]):
            user_input = input("Input: ")
            font_style = sys.argv[2]
            f = Figlet(font=font_style)
            print(f.renderText(f"{user_input}"))

        else:
            print("Invalid usage")
            sys.exit(1)

    elif len(sys.argv) == 1:
        user_input = input("Input: ")
        figlet = Figlet()
        figfonts = figlet.getFonts()
        font_style = random.choice(figfonts)
        f = Figlet(font=font_style)
        print(f.renderText(f"{user_input}"))

    else:
        print("Invalid usage")
        sys.exit(1)

except Exception:
    print("Invalid usage")
    sys.exit(1)
