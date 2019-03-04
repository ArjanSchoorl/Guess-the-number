from random import randint


# This function checks if the val is an integer
def integer(val):
    try:
        # Trying to get the integer of val
        int(val)
        # Return True if val is an integer
        return True
    except ValueError:
        # If val is not an integer than print sentence and return False
        print("This is not a number, please full in a number!")
        return False


# This function checks if the minimum is greater or equal to the maximum
def min_max_range(min, max):
    if int(min) >= int(max):
        # If the minimum is greater or equal to the maximum
        # Then print the sentence and return False
        print("Minimum is greater than maximum")
        print("")
        return False
    else:
        # If the minimum is less than maximum return True
        return True


# This function checks if the number that is given is in between the range
def out_of_range(num):
    if int(num) < int(x) or int(num) > int(y):
        # If the number is less than the minimum or the number is greater than the maximum
        # Then print the sentence and return False
        print("Out of range!")
        print("")
        return False
    else:
        # If the number is in range then return True
        return True


# Declare the state and 
state = 0
print("Guess the number!")


# Start the game - Guess the number
while True:
    while state == 0:
        # Get the minimum and maximimum for the range
        print("")
        x = input("Give a minimum number: ")
        y = input("Give a maximum number: ")
        if min_max_range(x, y):
            # If min_max_range() returns True then get a random_number
            # And create a list for the used numbers and go to state one
            random_number = randint(int(x), int(y))
            num_list = []

            # This is to debug the program, You will know the random_number
            # print(random_number)
            state = 1
        else:
            # if min_max_range() returns False, try again by change the state to zero
            state = 0

    while state == 1:
        # Get a guessed number from the user
        # That number is stored in a list 
        # If the user is correct the state will go to zero 
        # Otherwise the user has to guess again
        guess_number = input(f"Guess the number from {str(x)} to {str(y)}: ")
        # If the guessed number is an integer and in the range
        # Then check if the number is too low or too high or is correct
        if integer(guess_number) and out_of_range(guess_number):
            # Add the guessed number to the list
            num_list.append(int(guess_number))
            num_list.sort()
            if int(guess_number) > random_number:
                # If the guessed number is greater than the random number
                # Then print the sentence and give the list with already guessed numbers
                # And change the state to one
                print(f"Number {guess_number} is too high")
                print(f"Guessed numbers: {num_list}")
                print("")
                state = 1

            elif int(guess_number) < random_number:
                # If the guessed number is less than the random number
                # Then print the sentence and give the list with already guessed numbers
                # And change the state to one
                print(f"Number {guess_number} is too low")
                print(f"Guessed numbers: {num_list}")
                print("")
                state = 1

            else:
                # If the guessed number is equal to the random number
                # Then print that the user guessed the number
                # And change the state to zero
                print("You guessed the number!")
                print("")
                state = 0
        # If the guessed number is not an integer or out of the range
        # Then go back to state one and the user has to guess another number 
        else:
            state = 1
