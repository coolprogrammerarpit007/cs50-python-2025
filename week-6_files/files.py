# Files,CSV and Image Manipulation 

# names = list()
# for _ in range(3):
#     name = input("What's your name? ")
#     names.append(name)


# for name in sorted(names):
#     print(name)


#  saving data into the file
# name = input("Enter your name: ")

# file = open("names.txt","w")  // will always create or re-create a new file
# file = open("names.txt","a") # append data to the existing file
# file.write(name + "\n")
# file.close()


# Using with keyword 

# with open("names.txt" , "a") as f_hand:
#     f_hand.write(name + "\n")
#     f_hand.write("Nice to meet you everyone!" + "\n")


#  reading a file

# with open("names.txt","r") as f_hand:
#     lines = f_hand.readlines()

# for line in lines:
#     print(line.rstrip())


# Adding all the names in the file to the variable

# names = []


# with open("names.txt","r") as f_hand:
#     lines = f_hand.readlines()


# for line in lines:
#     if len(line) >= 1:
#         names.append(line.strip())


# print(f"Friends List: {names}")


# for name in sorted(names):
#     if name != "":
#         print(f"Hello My Friend: {name}")



#  Storing Data Into CSV

# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"Student Name: {row[0]} and his House Name: {row[1]}")


# sorting all these students based on their name.

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student = {}
        student["name"] = name   # can be written as: student = {'name' : name,'house':house}
        student["house"] = house
        students.append(student)


def get_student_name(student):
    return student['name']

# for student in sorted(students,key=get_student_name,reverse=True):
#     print(f"Student {student['name']} is in the {student['house']} house.")

# lambda is an Anonmus functions
for student in sorted(students,key=lambda student:student['name']):
    print(f"Student {student['name']} is in the {student['house']} house.")