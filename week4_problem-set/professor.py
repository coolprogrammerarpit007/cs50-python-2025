import random
import sys

def main():
    get_level()


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level.isdigit() and level == '1' or level == '2' or level == '3':
                return generate_integer(int(level))

        except ValueError:
            continue


def generate_random_integer(num1,num2):
    rand_number = random.randint(num1,num2) 
    return rand_number


def generate_integer(level):
    is_playing = True
    number_list = []
    game_score = 0
    start_point = None
    end_point = None
    index = 0
    if level == 1:
        start_point = 1
        end_point = 9
    
    elif level == 2:
        start_point = 10
        end_point = 99

    else:
        start_point = 100
        end_point = 999

    while index < 10:
        game_chances = 1
        random_number1 = generate_random_integer(start_point,end_point)
        random_number2 = generate_random_integer(start_point,end_point)
        number_list.append(random_number1)
        number_list.append(random_number2)
        answer = int(input(f"{number_list[0]} + {number_list[1]} = "))
        if answer == (random_number1 + random_number2):
            index += 1
            game_score += 1
            number_list.clear()
            continue

        else:
            while is_playing:
                print("EEE")
                answer = int(input(f"{number_list[0]} + {number_list[1]} = "))
                if  answer != (number_list[0] + number_list[1]):
                    game_chances = game_chances + 1
                    if(game_chances == 3):
                        print("EEE")
                        is_playing = False
                        index += 1
                        print(f"{number_list[0]} + {number_list[1]} = {number_list[0] + number_list[1]}")
                        number_list.clear()
                        break
                    
                else:
                    index += 1
                    break


    print(f"User Score is: {game_score}")
    


if __name__ == "__main__":
    main()