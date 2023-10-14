#A variable that has a value of a person's name with whitespaces, a tab, and a new line.
name = "   \tRaphaelCabigas\n   "

#Name without using any strip function
print("Name:")
print(name)

#Strip removes any spaces from both sides
print("Name with a strip function:")
print(name.strip())

#R Strip removes any spaces from the right side
print("Name with a R strip function:")
print(name.rstrip())

#L Strip removes any spaces from the left side
print("Name with a L strip function:")
print(name.lstrip())