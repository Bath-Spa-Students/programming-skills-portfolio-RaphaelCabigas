# Control structure: logical design to control order of statements
# Decision structure: check conditions
# Be careful regarding indentation - no curly braces in Python for IN and IF statements
# = Assignment operator is used for assigning value
# == operator determines the equality of both operands
# AND | you need both operands in the statement
# OR | you don't need both of the operands in the statement if one is true and one is not then it is still true
# NOT | opposite of the statement

# if statements example
sales = float(input("Enter money:"))
bonus = 0
if sales > 5000:
    bonus = 500
else:
    bonus = 0
print("Your bonus: "+str(bonus))

name = str(input("Enter your name: "))
if name == "Raphael":
    print("Good morning!")
else:
    print("Access Denied")

apple = int(input("Selling one apple for 2 AED (Input money here): "))
if apple >= 2:
    print("Here is one apple for you.")
else:
    print("Sorry not enough money. No apple for you.")

numlist = [3,6,9,12,15,18,21]
if 30 not in numlist:
    print("There is no 30 in list")
else:
    print("There is 30 in list")

# single decision structure = if statement only
money = 100
if money > 10:
    print("You have more money than me.")

# double decision structure = if and else statement
favnumber = 8
if favnumber == 9 :
    print("That is the right number")
else:
    print("That is wrong")

# dual alternative decision structure
temperature = int(input("What is the temparture for today? "))
if temperature < 40:
    print("A little cold, isn't it?")
else:
    print("Nice weather we're having.")

# ASCII code
str1 = "Mary"
str2 = "Mark"
str1 > str2
print("Mary is greater than Mark")

# Nested decision structure = more than two conditions 

earning = int(input("Enter your earning per year: "))
work_experience = float(input("Enter your work experience: "))

if earning > 30000:
    if work_experience >= 2:
        print("You are eligible for loan.")
    else:
        print("Sorry your work experience is less than 2 years.")
else:
    print("Your earning is less than 30,000.")

grade = int(input("What is your grade: "))

if grade >= 90 and grade <= 100:
    print("You pass with high honors.")
elif grade >= 85 and grade < 90:
    print("You pass with honors.")
elif grade >= 75 and grade <= 84:
    print("You pass.")
else: 
    print("You failed.")
