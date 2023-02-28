print("hi")

# Nested dictionary
myFamily = {
    "firstChild": {"name": "Alice", "age": 24},
    "secondChild": {"name": "Paul", "age": 19},
}


# ####################
for aList, items in enumerate(myFamily.items()):
    print(f"\nThis is child {aList} and list items: {items}")
    for indexPos, anItem in enumerate(items):
        print(f"This is index {indexPos} : item: {anItem}")

for aList, items in myFamily.items():
    print(f"\nThis is child {aList} and list items: {items}")
    for indexPos, anItem in enumerate(items):
        print(f"This is index {indexPos} : item: {anItem}")
