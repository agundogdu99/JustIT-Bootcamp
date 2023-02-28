import random

# colours = random.sample(["red", "blue"], counts=[4, 2], k=6)
"is equivalent to:"
colours = random.sample(["red", "red", "red", "red", "blue", "blue"], k=6)


# .sample(range(50), 7)
print(colours)

colours.sort()
print(colours)
