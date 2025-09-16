import time

def timer(minutes):
    seconds = minutes * 60

    while seconds >= 0:
        min, sec = divmod(seconds, 60)
        print(f'{min} minutes, {sec} seconds remaining', end = '\r')
        time.sleep(1)
        seconds -= 1


timer(1)
