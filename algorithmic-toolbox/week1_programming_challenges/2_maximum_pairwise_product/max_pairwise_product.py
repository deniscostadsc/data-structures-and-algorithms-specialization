from operator import mul
from functools import reduce

n = int(input())
numbers = [int(i) for i in input().split()]

if len(numbers) == 2:
    print(reduce(mul, numbers))
    exit(0)

max_1 = max(numbers[0:2]) 
max_2 = min(numbers[0:2])
 
for number in numbers[1:]:
    if number > max_1:
        max_2 = max_1
        max_1 = number
    elif number > max_2:
        max_2 = number

print(max_1 * max_2)
