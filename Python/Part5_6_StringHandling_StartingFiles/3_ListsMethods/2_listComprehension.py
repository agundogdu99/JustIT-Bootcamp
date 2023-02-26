" List comprehension is a concise way to create lists"
"""list comprehension gives us easy to use syntax to 
create one list out of another while applying some logic 
and condition. List syntax comprehension goes into square brackets
"""
#  Consists of brackets containing an expression followed by a for clause

# index    0  1   2  3  4  5 .............
# aList = [1, 2,  3, 4 ,5]
# bList = [6, 7, 8,  9, 10

"To Do: Predict, then Run, and then Investigate"
aList = [1, 2, 3, 4, 5]
bList = [6, 7, 8, 9, 10]

print(aList)
print(bList)

print(aList[2])
print(bList[3], bList[4])

# joined lists
joinedList = aList + bList
print(f"The joined list\n{joinedList}")


# Slicing items  from two lists

slicedItems = aList[0:3] + bList[1:4]
print(f"Sliced List\n{slicedItems}")

# add values from one list to another
"List comprehension"
listAB = [aList[i] + bList[i] for i in range(len(bList))]
print(f"The addedd items from listA {aList} and listB {bList}\n{listAB} ")


# Find common list items
cList = [1, 2, 3, 4, 5, 12, 13, 14, 15, 20, 21]
dList = [6, 7, 8, 9, 10, 4, 5, 12, 13, 14, 30]
print(f"{cList}\n{dList}")


"This is not list comprehension"
for nums in cList:
    if nums in dList:
        print(f"The common numbers in c and d lists: {nums}")


"This is List comprehension"
commonNums = [nums for nums in cList if nums in dList]
print(
    f"The common numbers in both list c and d using list comprehension:\n{commonNums}\n"
)
"This is not list comprehension"
squareNums = []
for nums in range(5):
    squareNums.append(nums ** 2)
    print(squareNums)

"List comprehension"
squareNums1 = [nums ** 2 for nums in range(5)]
print(f"List comprehension\n{squareNums}")

"To Do: Task 1: "
# Exercise: sort and print the items in the commons variable in ascending and descending order
# commonNums
sortedCommonNums = sorted(commonNums)
reverseSortedCommonNums = sorted(commonNums, reverse=True)
print(sortedCommonNums)
print(reverseSortedCommonNums)

# Exercise:  create two lists with at least two/three common names in both lists
my_list1 = ["Football", "Hockey", "Tennis", "Golf", "Skiing", "Volleball"]
my_list2 = ["Handball", "Hockey", "Climbing", "Golf", "Running", "Volleball"]
# find the common names from both lists and put them in a commonNames List
common_mylist = [sport for sport in my_list1 if sport in my_list2]
print(common_mylist)
# use the input and then the if to search the common names list for a specific name
searchSport = input("Enter sport name: ")
if searchSport in common_mylist:
    print(f'I found {searchSport}')
else:
    print(f"Sorry mate, {searchSport} isnt there")
# Exercise : Slice list aList from 0 - 5 and bList from 0 - 4 and put them together in a new list
newABlist = aList[:5] + bList[:4]
print(f"My new ABlist is {newABlist}")


"Further reading on List Comprehension"
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
# https://docs.python.org/3/library/functions.html#zip
