import time
from termcolor import colored

def timer():

    minutes = input(colored('How many minutes?: ', 'light_cyan'))
    seconds = float(minutes) * 60

    # main loop
    while seconds >= 0:
        min, sec = divmod(seconds, 60)
        print(colored(f'{min} minutes, {sec} seconds remaining', 'light_cyan'), end = '\r')
        time.sleep(1) # the mechanism
        seconds -= 1

    # if gets here, then means the timer ran successfully
    with open('total_time.txt', 'r') as f:
        # read in current total minutes
        old_mins = int(f.readline().strip())

    # calculate new total minutes
    new_mins = int(minutes) + old_mins

    # write it to file
    with open('total_time.txt', 'w') as f:
        f.write(str(new))
    
    print(colored(f'Done! \n', 'light_green'))

    print_time(new_mins)

# prints out total time
def print_time(minutes):

    m = float(minutes)
    s = int(round(m * 60))
    d, r = divmod(s, 86400)
    h, r = divmod(r, 3600)
    mi, se = divmod(r, 60)
    print(colored(f'{d} days, {h} hours, {mi} minutes, {se} seconds.', 'light_cyan'))
