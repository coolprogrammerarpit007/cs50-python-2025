import sys

def format_string(friends):
    formatted_string = ""
    if len(friends) == 1:
        return f"Adieu, adieu, to {friends[0]}"
    
    elif len(friends) == 2:
        return f"Adieu, adieu, to {friends[0]} and {friends[1]} "

    else:
        for index in range(len(friends)-1):
            formatted_string += friends[index] + ", "


    return "Adieu, adieu, to " + formatted_string + "and " + friends[-1]



try:
    friends = []
    while True:
        name = input("Name: ")
        friends.append(name)

except EOFError:
    print()
    sys.exit(1)

except KeyboardInterrupt:
    result_string = format_string(friends)
    print(result_string)
    sys.exit(1)

