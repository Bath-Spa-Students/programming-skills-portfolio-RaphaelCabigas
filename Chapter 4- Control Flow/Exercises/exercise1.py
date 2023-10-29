# PASS VERSION: "GREEN" +5 POINTS

# A alien_color variable with a string value "green"
alien_color = "green"

# An if statement testing if the alien_color variable has the string "green"
# If it is "green" then it will print +5 points
if alien_color == "green":
    print("+5 points earned") # Since the value of the variable is "green" it will execute the print statement

# FAIL VERSION: "YELLOW" NO OUTPUT

# A alien_color variable with a string value "yellow"
alien_color = "yellow"

# The same if statement as before but for "yellow"

if alien_color == "green":
    print("+5 points earned") # Since the value of the variable is "yellow" and there is no condition for "yellow" it will not have an output 