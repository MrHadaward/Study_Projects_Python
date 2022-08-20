import time
import os

# Objective of this project is to calculate in days, hours and seconds how many time has passed since the Epoch (1 jan 1970) 

while True:

# Epoch counts how many seconds has passed since 1 jan 1970

    epoch = time.time()

# Seconds in an hour calculates how many seconds there are in an hour 
    
    secondsinanhour = 60 * 60

# Seconds in day calculates how many seconds there are in a day 

    secondsinaday  = 24 * 60 * 60

# Days calculates how many days has passed since the epoch, hours how many hours, miutes how many minutes and seconds how many seconds

    days = (epoch - epoch % (secondsinaday)) / secondsinaday
    hours = ((epoch % secondsinaday) - (epoch % secondsinaday) % secondsinanhour ) / secondsinanhour
    minutes = (((epoch % secondsinaday) % secondsinanhour) - ((epoch % secondsinaday) % secondsinanhour) % 60) / 60
    seconds = (epoch % secondsinaday) % secondsinanhour % 60

    print('----------------------------------------------------------------\n')
    print(f'{int(days)} Days {int(hours)} Hours {int(minutes)} Minutes {int(seconds)} Seconds \n')
    print('----------------------------------------------------------------\n')
    
# Wait one second and clean the screen 

    time.sleep(1)
    os.system('cls')
    