#  Modules and Library in Python

from random import choice,shuffle
import statistics
import sys

friends = [
    "Mohit",
    "Rajesh",
    "Priyanshu",
    "Rohan",
]

# print(random.choice(friends))
# print(random.choice(["Heads","Tails"]))

# print(ch(["virat","novak","cristiano"]))


# shuffle -> randomizing the order in the list

# cards = [
#     "jack",
#     "queen",
#     "king"
# ]

# shuffle(cards)
# for card in cards:
#     print(card)


import sys
# statistics Library :- to done statistical operations.

# print(statistics.mean([50,50,50,50,50,50]))

# Command Line Arguments.
# sys module is used to get the command line arguments.
#  sys.argv gives the list of all the variables typed by the user before he / she type enter.

# try:
#     print("Hello, my name is: ",sys.argv[1])
# except IndexError:
#     print("Please provide your name as a command line argument.")

# print(len(sys.argv))
# if (len(sys.argv) < 2):
#     print("Too Few Arguments!")
#       sys.exit(1)

# elif (len(sys.argv) > 2):
#     print("Too Many Arguments!")

# else:
#     print(f"My name is: {sys.argv[1]}")




