from __future__ import print_function
from traceback import print_tb


score = input("Please enter the scores: ")
output = score.split()
output = sorted(output)
print(output[-2])