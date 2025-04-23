from validator_collection import validators,checkers,errors

def main():
    email = input("What's your email address? ").strip().lower()
    print(is_valid(email))


def is_valid(email):
    try:
        result = validators.email(email)
        return "Valid"

    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()