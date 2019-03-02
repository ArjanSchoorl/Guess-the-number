from random import randint

state = 0


def integer(val):
    try:
        int(val)
        return True
    except ValueError:
        print("This is not a number, please full in a number")
        print("")
        return False


while True:
    while state == 0:
        random_number = randint(0, 100)
        state = 1
        #print(random_number)
    while state == 1:
        guess_number = input("Guess the number from 0 to 100: ")
        print("")
        if integer(guess_number):
            if int(guess_number) > random_number:
                print("Number " + guess_number + " is too high")
                state = 2
            elif int(guess_number) < random_number:
                print("Number " + guess_number + " is too low")
                state = 2
            else:
                print("You guessed the number!")
                print("Let's try it again!")
                print("")
                state = 0
        else:
            state = 1
    while state == 2:
        print("Try again!")
        state = 1
