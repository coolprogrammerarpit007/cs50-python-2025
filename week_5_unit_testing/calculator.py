# Unit Testing 

def main(num):
    print(f"Square of Numbers are: {square(int(num))}")


def square(num):
    return num * num



if __name__ == "__main__":
    number = input("Enter Number: ")
    main(number)