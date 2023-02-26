
"Use python for loop  and len() function to iterate over a list and display the index and items simultaaneously "

"To Do: Predict, then Run, and then Investigate"

countries = ["Scotland", "Spain", "England", "Wales", "Brazil"]
for country in range(len(countries)):
    print(f"{country} | {countries[country]}\n")


"Use python for loop  and enumerate() function to iterate over a list and display the index and items simultaaneously "

# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.

countries = ["Scotland", "Spain", "England", "Wales", "Brazil"]
for country in enumerate(countries):
    print(country)

"To Do: Task 1: Investigate and explain what datatype does the enumerate function return"
# The enumerate() function in Python returns an enumerate object
# it is an iterator that generates a sequence of tuples containing pairs of elements from an iterable
# (i.e. list) and their corresponding index positions.
# Each tuple contains two values - the index position of the element in the iterable, and the element itself.


"Modify"
"To Do: Task 2: Complete the code below to iterate though both lists, add comment to explain your code"
highscore = [125, 63, 35, 12]
for counter in range(0, len(highscore)):
    print(highscore[counter])


usersList = ["Anna", "Paul", "Joe", "Jane", "Anne", "Pauline", "Joan", "Janet"]
for users in enumerate(usersList):
    print(f"{users}")
