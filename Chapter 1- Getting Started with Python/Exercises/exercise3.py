# Importing a datetime module that gains access to specific functions for date and time
import datetime
# A today variable that gets the current date and time
# The FIRST datetime. is the name module we are using
# The SECOND datetime. is the datetime class that stores things about date and time like year and hour
# today() gets the current date and time
today = datetime.datetime.today()
# With an f string, stores the today variable which shows the current date and time
print(f'The current date and time today is {today}')
