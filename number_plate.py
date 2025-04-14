def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    punctuations = [
    " ",  # Space
    "!",  # Exclamation Point
    ".",  # Period
    "#",  # Pound Symbol
    "@",  # At Symbol
    ",",  # Comma
    "?",  # Question Mark
    ";",  # Semicolon
    ":",  # Colon
    "-",  # Hyphen
    "–",  # En Dash
    "—",  # Em Dash
    "(",  # Left Parenthesis
    ")",  # Right Parenthesis
    "[",  # Left Bracket
    "]",  # Right Bracket
    "{",  # Left Brace
    "}",  # Right Brace
    "'",  # Apostrophe
    '"',  # Double Quotation Mark
    "'",  # Single Quotation Mark
    "...",  # Ellipsis
    "~",  # Tilde
    "^",  # Caret
    "&",  # Ampersand
    "*",  # Asterisk
    "+",  # Plus Sign
    "=",  # Equals Sign
    "|",  # Vertical Bar
    "<",  # Less Than
    ">",  # Greater Than
    "/",  # Forward Slash
    "\\",  # Backslash
    "%",  # Percent Sign
    "$",  # Dollar Sign
    "_",  # Underscore
]

    is_valid_plate = True
    cound_digit = 0
    first_digit_zero = False
    if len(s) >= 2 and len(s) <= 6 and s[:2].isalpha():
        for index in range(len(s) - 1):
            if s[index].isdigit() and s[index + 1].isalpha():
                is_valid_plate = False
            
            # check if first digit is zero or not.
            if s[index].isdigit() and cound_digit < 1 and s[index] == '0' and not first_digit_zero:
                first_digit_zero = True
                cound_digit += 1
                is_valid_plate = False


            # CHECK IF IT INCLUDES ANY PUNCTUATIONS
            for letter in s:
                if letter in punctuations:
                    is_valid_plate = False
                else:
                    pass

            else:
                pass

   
        
    else:
        is_valid_plate = False

    return is_valid_plate

main()