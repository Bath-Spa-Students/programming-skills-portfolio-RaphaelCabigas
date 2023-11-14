# A a variable asking for an input with a int() which converts the input to an integer
a = int(input("Enter a number greater or less than 100: "))
# y variable storing 1 and z variable storing 2
y = 1
z = 2
# An if statement that checks if a is greater than 100 the code within it will run
# However if a is not greater than 100, the values of y and z will not change
if a > 100:
    y = 20
    z = 40

# prints the values of y and z
print(y)
print(z)
