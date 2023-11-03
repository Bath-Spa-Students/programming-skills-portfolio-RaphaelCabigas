# Dictionaries for different pets and their owners
pet1 = {'Dog': 'Rainier'}
pet2 = {'Bird': 'Jonathan'}
pet3 = {'Hamster': 'Luna'}
pet4 = {'Dragon': 'Gerald'}

# A list named pets that stores all of the dictionaries
pets = [pet1, pet2, pet3, pet4]

# A for loop for the "pets" list where in the "animal" variable is used for each item in the "pets" list
# The FIRST for loop runs through each DICTIONARY/ITEM INSIDE THE "PETS" LIST
for animal in pets:
    # THE SECOND for loop runs through each KEY-VALUE PAIRS INSIDE THE DICTIONARIES

    # The keys/kind of animal are assigned with the "kind" variable
    # The values/owner name are assigned with the "owner" variable

    # A for loop when the key and value pair is found
    # inside the dictionaries in which .items() gets each pair
    for kind, owner in animal.items():
        print(f'{owner} has a pet {kind}')
        # It will execute the print statement for each pair found
        # F strings are use so we can make the sentence organize with each pair
