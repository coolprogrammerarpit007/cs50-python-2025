def main():
    user_input = input("Input: ").strip()
    print(shorten(user_input))

def shorten(word):
    vowel_list = ('a','e','i','o','u')
    new_str = word
    for char in new_str:
        if char in vowel_list or char.lower() in vowel_list:
            word = word.replace(char,'')
        else:
            pass

    return word        

if __name__ == "__main__":
    main()





