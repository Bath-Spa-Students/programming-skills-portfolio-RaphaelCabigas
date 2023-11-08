# A while loop set to true which will run the code within continously until stopped
while True:
    # The age variable that ask the user's age for availing the movie ticket
    # With the data type (int) converting the user input to an integer
    age = int(input(
        "To buy a movie ticket please enter your age: "))

    # The if-elif-else statements checks the age of the user
    if age < 3:  # If age is less than 3
        print("Your movie ticket is free")
    elif age >= 3 and age <= 12:  # Elif age is greater or equal to 3 and age is less than or equal to 12
        print("Your movie ticket is $10")
    else:  # Else for age is greater than 12
        print("Your movie ticket is $15")
    # Will print a statement corresponding to the age of the user

    # The input is stored in the buy_again variable that ask the user to continue or not
    buy_again = input("Type anything to buy again or Type N to stop: ")

    # This if-else statements checks the users input in buy_again
    if buy_again == "N":  # If the user's input is the letter N it will stop
        break
    else:  # Else the user types anything it will continue the loop
        continue
