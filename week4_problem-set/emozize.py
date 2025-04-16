import emoji


try:
    user_input = input("Input: ")
    print(f"Output: {emoji.emojize(user_input,language='alias')}")

except ValueError:
    print("Provide a proper Input....")