import re

email = input("Enter your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,flags=re.IGNORECASE):
    print("Valid Email-Id")
else:
    print("Invalid Email-Id")



# regex Vocularbary
# [a-zA-Z0-9] -> \w
# . any character except a newline
# * 0 or more occurrences of the preceding character
#  + 1 or more occurrences of the preceding character
#  ? matches 0 or 1 occurrence of the preceding character
#  {m} m repeations.
#  {m,n} m-n repeations.
# ^ -> matches the start of the string.
#  $ -> matches the end of the string or  just before the newline at the end of the string.
#  [] -> set of characters.
#  [^] -> complimenting of set

# \d -> decimal digit
#  \D -> not a decimal digit
#  \s whitespace characters.
# \S not a whitespace character
#  \w -> word character as well as the numbers and the underscore.
#  \W -> not a word character.
#  (...) -> A Group
#  A|B either A or B
#  (?:...) not capturing version.