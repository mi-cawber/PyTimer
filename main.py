import time

def timer():

    minutes = input('How many minutes?: ')
    seconds = minutes * 60

    while seconds >= 0:
        min, sec = divmod(seconds, 60)
        print(f'{min} minutes, {sec} seconds remaining', end = '\r')
        time.sleep(1)
        seconds -= 1

    # if gets here, then means the timer ran successfully
    with open('total_time.txt', 'r') as f:
        old_mins = int(f.readline().strip())

    # write new total minutes
    new_mins = minutes + old_mins
    with open('total_time.txt', 'w') as f:
        f.write(str(new))
    
    # total hours
    secs_total = new_mins % 60
    mins_total = new_mins % 60
    hrs_total = new_mins / 60
    days_total = hrs_total / 60
    
    print(f'Done! \n
          Total minutes: {new}')

