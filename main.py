from random import randint


# This is the main function
def main():
    while True:
        # Get the input from the user
        print()
        continu = input("Do you want to continue? Yes/No: ").lower()
        # If the user will continue, run the function guess()
        if continu == 'y' or continu == 'yes':
            guess()
        # If the user do not want to continue, close the program
        else:
            print("Closing...")
            return False


# This function is the where everything is processed
# In this function the user get the answer to their input
def guess():
    # Get the minimum and maximum numbers
    # Those numbers are for the range to guess
    num_min = input("Give a minimum number: ")
    num_max = input("Give a maximum number: ")
    # If the input numbers are integers and the minimum is less then the maximum
    # It will run the code below here
    if check_input(num_min, num_max):
        # This creates a random number between the range 
        num_random = randint(int(num_min), int(num_max))
        # This creates a list to store the guessed numbers
        num_list = set()
        # This counts how many times the user has tried
        count = 0
        # Go to state 1
        state = 1
        while state == 1:
            print()
            # Get a guessed number from the user
            num_guess = input(f"Guess the number from {str(num_min)} to {str(num_max)}: ")
            # This will check if the number is an int and if the number is in range
            if integer(num_guess) and in_range(num_guess, num_min, num_max):
                # If so the number will be stored in the list
                num_list.add(int(num_guess))
                count = count + 1
                # If the guessed number is greater than the random number
                # Then print the sentence and print the list with already guessed numbers
                if int(num_guess) > num_random:
                    print(f"Number {num_guess} is too high")
                    print(f"Guessed numbers: {num_list}")
                # If the guessed number is less than the random number
                # Then print the sentence and print the list with already guessed numbers
                elif int(num_guess) < num_random:
                    print(f"Number {num_guess} is too low")
                    print(f"Guessed numbers: {num_list}")
                # If the user guessed the random number
                # Print that he guessed the number and how many times it took
                # Then return False
                else:
                    print(f"You guess the number! Number: {num_guess}")
                    print(f"It took {count} times to guess the number")
                    return False
            # Go back to state 1
            else:
                state = 1
    # Print the sentence and return False
    else:
        print("Mininum or maximum is not a number or the minimum is greater then the maximum")
        return False


# This function checks if the numbers are an integer
def check_input(num1, num2):
    # Trying to get the integer of num1 and num2
    try:
        int(num1)
        int(num2)
        # If those are integers, then check if num2 is greater than num1
        # Then return True
        if int(num1) < int(num2):
            return True
    # If the above is not True, return  False
    except ValueError:
        return False


# This function checks if the number is an integer
def integer(num):
    # Trying to get the integer of num
    try:
        int(num)
        return True
    # If num is not an integer than print the sentence and return False
    except ValueError:
        print("Your input is not a number")
        return False


# This function checks if the number that is given is in between the range
def in_range(num, num_min, num_max):
    # If the number is less than the minimum or the number is greater than the maximum
    # Then print the sentence and return False
    if int(num) < int(num_min) or int(num) > int(num_max):
        print("The guessed number is out of range")
        return False
    # If the number is in range then return True
    else:
        return True


# Run the main function
main()
