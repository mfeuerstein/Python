# How to deal with random number generator

import random
import sys

nums = list()
counter = 0

print('Here are your numbers: \n')
while counter < 20:
    nums.append(random.randint(1, 6))
    print(nums[counter], end=" ")
    counter = counter + 1
else:
    print('\n')
    print(nums)
    nums.sort()
    nums.reverse()
    print(nums)
    print('\nAuf Wiedersehn!')
    sys.exit
