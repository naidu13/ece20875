#!/usr/bin/python3
year=2021
# Your code should be below this line

if year % 400 == 0:
    print('True')
elif year % 4 == 0 and not year % 100 == 0:
    print('True')
else:
    print('False')