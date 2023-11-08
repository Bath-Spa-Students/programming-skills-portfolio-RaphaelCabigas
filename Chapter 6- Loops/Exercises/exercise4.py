# A sandwich_orders list storing names of different sandwiches
sandwich_orders = ["Peanut Butter",
                   "Ham and Cheese", "Grilled Chicken",
                   "Strawberry Jelly", "Roast Beef", "Avocado",
                   "Tuna Spread", "Nutella", "Egg"]

# A finished_sandwiches list
finished_sandwiches = []

# A while loop that checks every item inside of sandwich_orders list and will end after all have been checked
while sandwich_orders:
    # A ordered variable that stores an item inside of the sandwich_orders list with the help of pop()
    ordered = sandwich_orders.pop(0)

    # A print statement with a message for the each ordered sandwich that happens
    # With an f string to put the ordered variable
    print(f'Here is your order, a {ordered} Sandwich.')
    # The append() will add the ordered sandwich variable to the finshed_sandwiches list
    finished_sandwiches.append(ordered)

# This will execute after all the items sandwich_orders have been done
print(f'Finished Sandwiches: {finished_sandwiches}')
