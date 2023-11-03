# A dictionary named river containing 3 rivers and the country that can be found in
rivers = {
    'Amazon River': 'Brazil',
    'Nile River': 'Egypt',
    'Yangtze River': 'China',
}

# The keys/rivers are assigned with the "river" variable
# The values/countries are assigned with the "country" variable

# A for loop when the key and value pair is found
# Inside rivers in which .items() gets each pair
for river, country in rivers.items():
    print(f'The {river} can be found in {country}')
    # It will execute the print statement for each pair found
    # F strings are use so we can make the sentence organize with each pair

# A for loop when the key/river is found
# Inside rivers in which .keys() gets each river
for river in rivers.keys():
    print(river)
    # It will execute the print statement for each river found

# A for loop when the value/country is found
# Inside rivers in which .values() gets each country
for country in rivers.values():
    print(country)
    # It will execute the print statement for each country found
