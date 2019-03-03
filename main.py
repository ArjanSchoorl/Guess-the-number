from random import randint

state = 0
x = 0  # Minimum range
y = 100  # Maximum range


def integer(val):
    try:
        int(val)
        return True
    except ValueError:
        print("This is not a number, please full in a number!")
        return False


def min_max_range(val, val2):
    if int(val) >= int(val2):
        print("Minimum is greater than maximum")
        print("")
        return False
    else:
        return True


def out_of_range(val):
    if int(val) < int(x) or int(val) > int(y):
        print("Out of range!")
        return False
    else:
        return True


while True:
    while state == 0:
        x = input("Give a minimun number: ")
        y = input("Give a maximum number: ")
        if min_max_range(x, y):
            random_number = randint(int(x), int(y))
            num_list = []
            # print(random_number)  # Debug mode
            state = 1
        else:
            state = 0

    while state == 1:
        guess_number = input(f"Guess the number from {str(x)} to {str(y)}: ")
        if integer(guess_number) and out_of_range(guess_number):
            num_list.append(int(guess_number))
            if int(guess_number) > random_number:
                print(f"Number {guess_number} is too high")
                print(f"Guessed numbers: {num_list}")
                print("")
                state = 1

            elif int(guess_number) < random_number:
                print(f"Number {guess_number} is too low")
                print(f"Guessed numbers: {num_list}")
                print("")
                state = 1

            else:
                print("You guessed the number!")
                print("")
                state = 0

        else:
            state = 1
