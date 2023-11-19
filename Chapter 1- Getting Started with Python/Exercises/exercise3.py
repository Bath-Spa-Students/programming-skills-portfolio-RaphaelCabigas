# Importing a datetime module that gains access to specific functions for date and time
import datetime
# A today variable that stores the command to get the current date and time
today = datetime.datetime.today()
# With an f string, stores the today variable which shows the current date and time
print(f'The current date and time today is {today}')
