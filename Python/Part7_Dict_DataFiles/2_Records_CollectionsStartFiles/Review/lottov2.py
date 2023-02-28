import random

"""
To choose a sample from a range of integers, use range() for the population argument. This is especially fast and space efficient for sampling from a large population:
sample(range(10000000), 60)
"""
numbers = random.sample(range(50), 7)
print(numbers)

numbers.sort()
print(numbers)
