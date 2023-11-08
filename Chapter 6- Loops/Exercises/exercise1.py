# A pizza list that will store toppings inside
pizza = []

# A while loop set to true which will run the code within continously until stopped
while True:
    # The toppings variable that ask the user's desired toppings on the pizza
    toppings = input(
        "Enter any toppings you would like to add on your pizza: ")

    # The append() will add the user's input of toppings on the pizza variable
    pizza.append(toppings)

    # A print statement to inform the user that the toppings will be added on the pizza
    # With an f string to put the user's input of toppings in the statement
    print(f'Okay, we will be adding some {toppings} toppings on your pizza!')

    # The input is stored in the add_more variable that ask the user to continue to add more toppings or not
    add_more = input("Type anything to add more toppings or Type N to stop: ")

    # An if statement that checks the users input in add_more
    # If the user's input is the letter N it will stop and print
    if add_more == "N":
        # With an f string to put the pizza list in the print statement
        print(f'The pizza toppings added are the following: {pizza}')
        break  # a break statement to stop the while loop
