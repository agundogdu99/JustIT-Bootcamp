
"Further reading on datatypes in python"
# https://docs.python.org/3/library/stdtypes.html#tuple
# https://docs.python.org/3/library/stdtypes.html#set
# https://www.w3docs.com/learn-python/python-data-types.html


"A set is an unordered list"


"Predict, then Run, and then Investigate"
# once a set is created the values/items can not be changed
set1 = {10, 20, 30, "xyz", "abc"}
print(type(set1))
print(set1)

set1.update([1, 4, "bcd"])  # set can be updated with new items/value
print(set1)

set2 = {4, 7, "paul", "peter"}
set1.update(set2)
print(set1)

# items in a set can ony be removed using the name/value of the set item not via index
set1.remove("peter")
print(set1)

# Add an element to a set.
set1.add("Python")  # new items/value can be added to a set after creation
print(set1)

"To Do: Investigate and exlain in your own words the purpose of the for Loop in the code block below"
# The for loop uses a temporary variable 'i' to iterate over set2 and print each of the unique values

for i in set2:
    print(i)

set3 = {21, 22, 23, "John"}
print(set3)

set4 = input("Enter Value: ")
print(set4)


"Modify:"
"To DO:"
# Modify the data structures above by changing their values or object names


"Make:"
"Task 1: Follow the set examples above to create a set with five countries"
my_countries = {'Turkey', 'England', 'India', 'Russia', 'Belgium'}
# print the items(countries) in the set
print(my_countries)
# add two more countries
my_countries.update(['France', 'Italy'])
# delete a counry of your choice
my_countries.remove('England')
# print the set items
print(my_countries)


"Predict, Run and Investigate the frozen set"
fSet3 = frozenset(set3)
print(fSet3)


"Make:"
"To DO: Try to add an item to frozen set 'fset' and explain the outcome"
fSet3.update('Test')
# AttributeError: 'frozenset' object has no attribute 'update'
