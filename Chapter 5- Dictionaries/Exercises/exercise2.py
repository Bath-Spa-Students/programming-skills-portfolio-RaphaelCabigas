# A dictionary named glossary containing python terms and their meanings
glossary = {'Input': 'gets the input from the user',
            'Integers': 'are the numbers',
            'Floats': 'are the numbers with decimal points',
            'Strings': 'a line of characters enclosed by quotation marks',
            'Comment': 'the # sign is used to explain the code to others'
            }

# A for loop when the key and value pair is found
# Inside the glossary in which .items() gets each pair
for word, meaning in glossary.items():
    print(f'{word}:\n{meaning}')
    # It will execute the print statement for each pair found
    # F strings are use so we can make each word and its meaning organize
