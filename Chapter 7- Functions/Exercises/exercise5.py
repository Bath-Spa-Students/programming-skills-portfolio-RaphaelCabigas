# This is a describe_city function in which we use def to define on what the function is going to do
# With two parameters of name and country with a default value of "Philippines"
def describe_city(name, country="Philippines"):
    print(f'{name} City can be found in {country}')
    # F strings are use so we can make the sentence organize with the parameters


# The name parameters are set to a city in and not in the country
# The message parameter is set to our default value
describe_city("Pasig")
describe_city("Makati")
describe_city("New York")

# The code within these functions called will be executed in which prints the message
