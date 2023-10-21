#A locations list that stores five places in the world I would like to visit
locations = ["Japan", "Hawaii", "New Zealand", "Greece", "Italy"]

#ORIGINAL ORDER
print(locations)

#Using sorted() to print the list in ALPHABETICAL ORDER WITH NO CHANGE TO THE ORIGINAL LIST
print(sorted(locations))

#ORIGINAL ORDER
print(locations)

#Using sorted() and a reverse parameter set to TRUE to print the list in REVERSE ALPHABETICAL ORDER WITH NO CHANGE TO THE ORIGINAL LIST
print(sorted(locations, reverse=True))

#ORIGINAL order
print(locations)

#Using reverse() to CHANGE THE ORIGINAL ORDER OF THE LIST IN REVERSE and printing the list in order to show it changed
locations.reverse()
print(locations)

#Using reverse() to CHANGE THE ORDER OF THE LIST AGAIN and printing the list in order to show it is back to it's original order
locations.reverse()
print(locations)

#Using sort() to CHANGE THE ORDER OF THE LIST in ALPHABETICAL ORDER and printing the list in order to show it changed
locations.sort()
print(locations)

#Using sort() and a reverse parameter set to TRUE to CHANGE THE ORDER OF THE LIST in REVERSE ALPHABETICAL ORDER
#and printing the list in order to show it changed
locations.sort(reverse=True)
print(locations)