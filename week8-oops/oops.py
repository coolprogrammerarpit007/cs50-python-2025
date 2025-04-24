# class Student:
#     def __init__(self,name,house,patronous=None):
#         if not name:
#             raise ValueError("Missing Name")
#         if house and house not in ("Gryffindorr","Slythrin","Hupplepuff","Revenclaw"):
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#         self.patronous = patronous


#     def __str__(self):
#         print(f"{self.name} is from the house of {self.house} and he has {"patronous of " + self.patronous if self.patronous else "not any patronous."}")


#     def charm(self):
#         match(self.patronous):
#             case "stag":
#                 return "🦌"
#             case "otter":
#                 return "🦦"
#             case "lion":
#                 return "🦁"
#             case "snake":
#                 return "🐍"


# def main():
#     student = get_student()
#     print(f"{student.name} from the house of {student.house}")
#     student.__str__()


# def get_student():
#     name = input("Enter Student Name: ").lower()
#     house = input("Enter Student House: ").capitalize()
#     patronous = input("Enter student's patronous: ").lower()
#     student = Student(name,house,patronous)
#     print("Expecto Patronous:")
#     print(student.charm())
#     return student


# if __name__ == "__main__":
#     main()



#  Decorators

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"
    

#     # Getter for the name
#     @property
#     def name(self):
#         return self._name
    

#     # setter for the name
#     @name.setter
#     def name(self,name):
#         if not name:
#             raise ValueError("Invalid name")
#         self._name = name
    

#     # Getter for the House
#     @property
#     def house(self):
#         return self._house
    

#     # setter for the house
#     @house.setter
#     def house(self,house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house



# def main():
#     student = get_student()
#     student.house = "Number 4 House,Private Drive "
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()


# Class Methods

import random


# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor","Slythrin","Hupplepuff","Revenclaw"]

#     def sort(self,name):
#         return f"{name} is sorted into {random.choice(self.houses)}"
    

# hat = Hat()
# print(hat.sort("Harry"))
# Notice how when we pass the name of the student to the sorting hat, it will tell us what house is assigned to the student. Notice that hat = Hat() instantiates a hat. The sort functionality is always handled by the instance of the class Hat. By executing hat.sort("Harry"), we pass the name of the student to the sort method of the particular instance of Hat, which we’ve called hat.

# We may want, though, to run the sort function without creating a particular instance of the sorting hat (there’s only one, after all!). We can modify our code as follows:



class Hat:
    houses = ["Gryffindor","Slythrin","Hupplepuff","Revenclaw"]
    
    @classmethod
    def sort(cls,name):
        return f"{name} is sorted into the {random.choice(cls.houses)}"
    

# print(Hat.sort("Harry Potter"))



class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is from the house of {self.house}"
    
    # Getter Name
    @property
    def name(self):
        return self._name
    
    # Setter name
    @name.setter
    def name(self,name):
        self._name = name


    # Getter House
    @property
    def house(self):
        return self._house
    
    # Setter House
    @house.setter
    def house(self,house):
        self._house = house

    @classmethod
    def get(cls):
        name = input("Enter Name: ")
        house = input("Enter House: ")
        return cls(name,house)
    

    
    

def main():
    student = Student.get()
    student.name = "Draco Malfoy"
    student.house = "Slythrin"
    return f"{student.name} is from the house of {student.house}"


# if __name__ == "__main__":
#     print(main())



# Inheritance 
class Wizard:
    def __init__(self,name):
        self.name = name


class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name,subject):
        super().__init__(name,Professor)
        self.subject = subject
