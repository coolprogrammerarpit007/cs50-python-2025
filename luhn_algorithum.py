# LUHN Algorithum to validate social security numbers.
import sys
def main(card_number):
    translation_table = str.maketrans({"-":""," ": ""})
    translated_number = card_number.translate(translation_table)
    result = "Validated Number!" if is_validate(translated_number) else "Not Validated!"
    return result

def is_validate(translated_number):
    reversed_number = translated_number[::-1] # will get the reversed number
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    even_digits = reversed_number[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number =( number // 10) + (number % 10)
        sum_of_even_digits += number
    odd_digits = reversed_number[0::2]
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

   
    total = sum_of_even_digits + sum_of_odd_digits
    return True if total % 10 == 0 else False 


if __name__ == "__main__":
    number = input("Enter Card Number: ")
    print(main(number))