"Read through the data types examples and reference or use it as a guide during lessons"
"Further reading on datatypes in python"
# https://www.w3docs.com/learn-python/python-data-types.html

# List is an ordered sequence of items. It is a very flexible data type in python
# The values in a list doesn't have to be of the same type
# items in a list can be modified
# declare a list1 variable and assign values of different datatypes in the list
# items can be accessed based on their index position

"Predict, then Run, and then Investigate"

emptyList = []  # creates an empty list
print(type(emptyList))
print(emptyList)

# creates a list with elements of different data types
list1 = [1, 5, 9.9, 5, "list", "list"]

# creates a list with elements of different data types
list2 = [1, 3, 4, 5, 10, 20]
print("\nThis is a List")
print(type(list1))
print(list1)
print(type(list2))
print(list2)


# Tuple is a sequence of items that are in order
# and it is not possible to modify the tuples. Therefore,
# tuples are faster than list and the primary use of tuples
# is to create, write and protect data
# items can be accessed based on their index position

# declare/create a tuple1 variable and assign values of different datatypes in the tuple
tuple1 = (6, -4, "Tuple", -4, 3.2, "Tuple")
print("\nThis is a Tuple")
print(type(tuple1))
print(tuple1)

# Set is a  collection of unique items that are not in order,
# it is an unordered datatype. Duplicates are eliminated in a set
# Set items cannot be accessed based on their index position

# declare/create a set1 variable and assign values of different datatpes in the set
set1 = {4, 5, 5, 5, 5, 5, 5, 10.5, "xyz", 1.3, 5, "xyz"}
print("\nThis is a Set")
print(type(set1))
print(set1)

# expected output
# duplicate items will be printed only once
# items in the list will be displayed in no particular order

# Dictionary stores data as key value pairs
# to retrieve a specific value from a dictionary you need to know the key

# create a dictionary with key value pairs
dictionary1 = {1: "John", 2: "Anna", 3: "Peter"}
dictionary2 = {"age": 23, "homeOwner": True}

print("\nThis is a Dictionary")
print(type(dictionary1))
print(dictionary2)

"Modify:"
"To DO:"
# Modify the data structures above by changing their values or object names
my_list = [10, "list", 20, "list", [30, "nested list"]]
my_tuple = ("Yes", 4, "I", 14, "am", 41, "Immutable")
my_set = {"abc", 1, 2, 3, "cba", 3, 2, 1, "abc"}
my_dictionary = {1: "Ahmet 1", 2: "Ahmet 2", 3: "Ahmet 3"}


"Make:"
"To DO:"
# Create a list with five elements(items)
my_list = [10, "list", 20, "list", [30, "nested list"]]
# Create a tuple with five elements(items)
my_tuple = ("Yes", 4, "I", 14, "am", 41, "Immutable")
# Create a set with five elements(items)
my_set = {"abc", 1, 2, 3, "cba", 3, 2, 1, "abc"}
# Create a dictionary with five key value pairs items
my_dictionary = {1: "prop 1", 2: "prop 2",
                 3: "prop 3", 4: "prop 4", 5: "prop 5"}

"To DO:Extension"
"Why and when would you use a:"
# list
# In order to create a simple list/collection of data that is ordered, can easily be accessed and is muteable
# Lists are also iterable, meaning they can be looped over with ease
# Also useful in situations where you want to sort the data

# tuple
# In order to create a simple list/collection of data that is ordered, can easily be accessed and is IMUTABLE
# Being imutable will protect its contents from being re-assigned
# Tuples are also iterable
# Also useful in situations where you want to sort the data

# set
# It could be used to find unique elements amoungst various collections of data
# Is also useful in scenarioes where you are required to filter out duplicates

# dictionary
# It is useful when you are storing large dataset and require to map key value pairs
# to each other...
# Doing so allows for efficient grouping of the data
