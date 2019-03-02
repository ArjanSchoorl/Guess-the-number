from random import randint
random_number = randint(0,1000)
state = 0


while True:
    while state == 0:
        guess_number = input("Guess the number from 0 to 1000: ")
        state = 1
    while state == 1:
        if int(guess_number) > random_number:
            print("Number " + guess_number + " is too high")
            state = 0
        elif int(guess_number) < random_number:
            print("Number " + guess_number + " is too low")
            state = 0
        else:
            print("You guessed the number!")
            state = 3
