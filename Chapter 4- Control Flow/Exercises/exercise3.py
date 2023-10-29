# "GREEN" VERSION: +5 POINTS

# A alien_color variable with a string value "green"
alien_color = "green"

# An if-elif-else statement for the alien_color (green, yellow, red)
# If it is "green" then it will print +5 points
# If it is "yellow" then it will print +10 points
# Else it will print +15 points
if alien_color == "green":
    print("+5 points earned") # Since the value of the variable is "green" it will execute the if statement
elif alien_color == "yellow":
    print("+10 points earned")
else:
    print("+15 points earned")

# "YELLOW" VERSION: +10 POINTS

# A alien_color variable with a string value "yellow"
alien_color = "yellow"

# The same if-elif-else statement as before but for "yellow"
if alien_color == "green":
    print("+5 points earned")
elif alien_color == "yellow":
    print("+10 points earned") # Since the value of the variable is "yellow" it will execute the elif statement
else:
    print("+15 points earned")

# "RED" VERSION: +15 POINTS

# A alien_color variable with a string value "red"
alien_color3 = "red"

# The same if-elif-else statement as before but for "red"
if alien_color3 == "green":
    print("+5 points earned")
elif alien_color3 == "yellow":
    print("+10 points earned")
else:
    print("+15 points earned") # Since the value of the variable is "red" and there is no condition for "red" it will execute the else statement
