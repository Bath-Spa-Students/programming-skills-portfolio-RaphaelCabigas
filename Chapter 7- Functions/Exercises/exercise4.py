# This is a make_shirt function in which we use def to define on what the function is going to do
# We assign the two parameters size and message with a default value of "large" and "I Love Python"
def make_shirt(size="large", message="I Love Python"):
    print(f'A {size} shirt has been made with a message: {message}.')
    # F strings are use so we can make the sentence organize with the parameters


# The size and message parameter is set to the default value
make_shirt()

# The size parameter is set to "medium"
# The message parameter is set to the default value
make_shirt("medium")

# The size and message parameter is set to our desired size with a different message using keyword arguments
make_shirt(size="small", message="Bath Spa")

# The code within these functions called will be executed in which prints the message
