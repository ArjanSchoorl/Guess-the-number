from random import randint

state = 0
x = 0 # Minimum range
y = 100 # Maximum range

def integer(val):
    try:
        int(val)
        return True
    except ValueError:
        print("This is not a number, please full in a number!")
        return False

def out_of_range(val):
    if int(val) < x or int(val) > y:
        print("Out of range!")
        return False
    else:
        return True


while True:
    while state == 0:
        random_number = randint(x, y)
        num_list = []
        state = 1
        print(random_number)  # Debug mode

    while state == 1:
        guess_number = input(f"Guess the number from {x} to {y}: ")
        if integer(guess_number) and out_of_range(guess_number):
            num_list.append(int(guess_number))
            if int(guess_number) > random_number:
                print(f"Number {guess_number} is too high")
                print(f"Guessed numbers: {num_list}")
                state = 1

            elif int(guess_number) < random_number:
                print(f"Number {guess_number} is too low")
                print(f"Guessed numbers: {num_list}")
                state = 1

            else:
                print("You guessed the number!")
                print("")
                state = 0

        else:
            state = 1
