# index = 3
# while index != 0:
#     print("Meow Meow!!")
#     index -= 1


# program to convert camel case to snake case

def main(text):
    result = change_case(text)
    print(f"snake_case: {result}")

def change_case(str):
    new_str = ""
    for letter in str:
        if letter.isupper():
            new_str += "_"
        new_str += letter.lower()
    return new_str
            


text = input("camelCase: ")
if __name__ == "__main__":
    main(text)