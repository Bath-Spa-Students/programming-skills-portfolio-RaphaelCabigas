# An user input that ask for the age of the person stored in the age variable
age = int(input("Enter your age: "))

# An if-elif-else statement for the age variable which tells the user the stage of their life
if age < 2:
    print("You are a baby.") # If age is less than 2 it will print "You are a baby."
elif age == 2 or age < 4:
    print("You are a toddler.") # Elif age is equal to 2 or less than 4 it will print "You are a toddler."
elif age == 4 or age < 13:
    print("You are a kid.") # Elif age is equal to 4 or less than 13 it will print "You are a kid."
elif age == 13 or age < 20:
    print("You are a teenager.") # Elif age is equal to 13 or less than 20 it will print "You are a teenager."
elif age == 20 or age < 65:
    print("You are an adult.") # Elif age is equal to 20 or less than 65 it will print "You are an adult."
else:
    print("You are an elder.") # Else for an age equal to 65 or older it will print "You are an elder"
