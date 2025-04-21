import re

email = input("Enter your email? ").strip()

if re.search(".+@.+\.edu",email):
    print("Valid Email-Id")
else:
    print("Invalid Email-Id")



# regex Vocularbary

# . any character except a newline
# * 0 or more occurrences of the preceding character
#  + 1 or more occurrences of the preceding character
#  ? matches 0 or 1 occurrence of the preceding character
#  {m} m repeations.
#  {m,n} m-n repeations.

