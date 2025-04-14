#  Exceptions Handling In Python

# try:
#     number = int(input("Enter Number: "))
# except:
#     print("Invalid Input")



try:
    number = int(input("Enter Number: "))
except ValueError:
    print("Invalid Input")
else:
    print(f"{number} is Integer.")