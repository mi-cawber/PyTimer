from termcolor import colored
m = float(input("Minutes: "))
s = int(round(m * 60))
d, r = divmod(s, 86400)
h, r = divmod(r, 3600)
mi, se = divmod(r, 60)
print(f'{d} days, {h} hours, {mi} minutes, {se} seconds.')
