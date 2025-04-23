#  Classes and Objects
# Classes are like blueprint and Objects are the Instances of class.

class Student:
    ...


def main():
    student = get_student()
    print(f"{student.name} is from House of {student.house}")


def get_student():
    # student = Student()
    # student.name = input("Enter Student Name: ")
    # student.house = input("Enter Student House: ")
    name = input("Enter Student Name: ")
    house = input("Enter Student House: ")
    student = Student(name,house)
    return student


if __name__ == "__main__":
    main()



