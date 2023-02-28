"List methods"
"list.append(item)"  # add item at end of list
"list.insert(index,item)"  # add item at index
"list.pop(index)"  # remove item at index
"list.remove(item)"  # remove item
"list.index(item)"  # search for index of item
"list.count(item)"  # get occurrences of item
"list.reverse()"  # reverse list
"list.sort()"  # sort list

"Traverse"  # Move through a sequence.
"Method"  # A function that belongs to an object.
# A function that you have created yourself and imported into other programs that you have created.
"Custom  built function"
# A dynamic data structure that holds items under one name. The items can be of varying data types.
"List"

"To Do: Predict, then Run, and then Investigate"
# The list below contains string literals (i.e. pieces of text) and need to be in quotes

#                 0         1         2        3         4
listOfNames = ["Nicole", "Laura", "Silvia", "Steve", "Juliet"]
print(listOfNames)  # Prints the list
print(listOfNames[2])  # Prints Silvia

"What is the use of the len()?"
for index in range(len(listOfNames)):
    print(f"{index} : {listOfNames[index]}")

print(f"\n{listOfNames}")
# What item is returned from the list and why?
print(f"{listOfNames[3]}\n")


twoDLists = [
    #      0      1          2       3       4
    ["Nicole", "Laura", "Silvia", "Steve", "Juliet"],  # 0
    # List of numbers
    [10, 20, 30, 40, 50],  # 1
    # List of Tecnologies
    ["JS", "Python", "HTML", "CSS", "NoSQL"],  # 2
]

"To Do: Task1"

# You have been provided with the multidimentional list ABOVE.
"Your tasks are listed below"
# 1. Print the multidimentional list
print(twoDLists)
# 2. Print Nicole, number 10 and JS
print(f"{twoDLists[0][0]} - {twoDLists[1][0]} - {twoDLists[2][0]}")
# 3. Print Laura, number 20 and Python
print(f"{twoDLists[0][1]} - {twoDLists[1][1]} - {twoDLists[2][2]}")
# 4. Print Juliet, number 50 and NoSQl
print(f"{twoDLists[0][-1]} - {twoDLists[1][-1]} - {twoDLists[2][-1]}")
# print(twoDLists[row/list level][index position of item in the list])


"To Do: Task2"
# Create a 2D list with 6 items
my_2d = [["A", 1], ["B", 2], ["C", 3], ["D", 4], ["E", 5], ["F", 6]]
# name of your choice
# print the 2nd, 4th and last item in the list
print(
    f"Second item: {my_2d[1]}, Fourth item: {my_2d[3]}, Last item: {my_2d[-1]}")

"To Do: Task3: Practice exercise over the weekend"
# # Create a shopping list program
