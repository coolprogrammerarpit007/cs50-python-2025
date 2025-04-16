import random 
import sys

def main():
    is_playing = True
    secret_number = False
    is_game_level = False
    game_level = 0
    try:
        while is_playing:
            try:
                game_level = int(input("Level: "))
                is_game_level = True
                secret_number = random.randint(1,game_level)
                print(f"Secret Number: {secret_number}")
                is_game_level = True
            except:
                continue

            if is_game_level:
                while True:
                    user_guess = input("Guess: ")
                    if user_guess.isalpha():
                        continue

                    elif int(user_guess) < 0:
                        continue

                    else:
                        break
                    
                if user_guess.isdigit() and int(user_guess) > 0 :
                    if guess_random_number(int(user_guess),secret_number):
                        is_playing = False
                        sys.exit()

                    else:
                        while is_playing:
                            new_guess = int(input("Guess: "))
                            if guess_random_number(new_guess,secret_number):
                                is_playing = False
                                sys.exit()
                            else:
                                continue

                

               


    except ValueError:
        print("Invalid input. Please enter a number.")
        main()
                        




# guess random_number function
def guess_random_number(user_guess,secret_number):
    if user_guess == secret_number:
        print("Just right!")
        return True
    elif user_guess < secret_number:
        print("Too small!")
        return False
    else:
        print("Too large!")
        return False


if __name__ == "__main__":
    main()