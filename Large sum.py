#! Python 3

# Find the first ten digits of the sum of the following one-hundred 50-digit numbers

import pyperclip

print("Please input the number you would like to find the greatest product of 13 adjacent digits:")
input()
Values = list(map(int, pyperclip.paste().split('\r\n')))

SumTotal = sum(Values)

print(str(SumTotal)[0:10])
