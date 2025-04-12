# week-1 conditional programs

# problem 1
# import sys
# user_input = input("What is the great question to the life? ")
# user_input = user_input.replace("-"," ").lower()

# match user_input:
#     case "42":
#         print("Yes")
#     case _:
#         print("No")


# Problem 2

# user_input = input("Enter Greeting: ").lower()

# if user_input.startswith("hello"):
#     print("$0")
# elif user_input.startswith("h"):
#     print("$20")
# else:
#     print("$100")


#  problem 3

# file_name = input("Enter File Name: ")
# if file_name.endswith("gif"):
#     print("image/gif")
# elif file_name.endswith("jpg"):
#     print("image/jpeg")
# elif file_name.endswith("jpeg"):
#     print("image/jpeg")
# elif file_name.endswith("png"):
#     print("image/png")
# elif file_name.endswith("pdf"):
#     print("application/pdf")
# elif file_name.endswith("txt"):
#     print("text/plain")
# elif file_name.endswith("zip"):
#     print("application/zip")
# else:
#     print("application/octet-stream")



#  Math Interpretor

# expression = input("Expression: ").split(" ")
# [num1,operator,num2] = expression
# if operator == "+":
#     print(f"{float(num1) + float(num2):.1f}")
# elif operator == "-":
#     print(f"{float(num1) - float(num2):.1f}")
# elif operator == "*":
#     print(f"{float(num1) * float(num2):.1f}")
# elif operator == "/":
#     print(f"{float(num1) / float(num2):.1f}")

# Problem 5

def main(time):
    convert(time)

def check_sehdule(converted_time):
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    [hrs,mins] = time.split(":")
    total_time = int(hrs) + int(mins)/60
    check_sehdule(total_time)

time =  input("Enter Time (#:#) ")
if __name__ == "__main__":
    main(time)