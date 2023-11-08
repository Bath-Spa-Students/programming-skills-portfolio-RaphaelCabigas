# This is a make_shirt function in which we use def to define on what the function is going to do
# With two parameters of size and message
def make_shirt(size, message):
    print(f'The size of the shirt is {size} with a message: {message}.')


# We use positional arguments which means the order of these values corresponds to the order of the parameters
# With the first value as the size and the second value as the message
make_shirt("extra large", "Bath Spa")

# We use keyword arguments to make it more clearer on what parameter we want to change
# We assign these valuess to the size and message parameters
make_shirt(message="Creative Computing", size="small")

# The size and message are set to our desired outcome
# The code within these functions called will be executed in which prints the message
