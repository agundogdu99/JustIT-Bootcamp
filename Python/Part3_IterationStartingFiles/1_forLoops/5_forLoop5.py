import random
"To Do: Predict, then Run, and then Investigate "

countries = ["Scotland", "Spain", "England", "Wales",
             "Brazil", "Argentina", "Italy", "France"]


print("Printed all countries in the terminal")
for country in range(len(countries)):
    print(f"{countries[country]}")


print("\nNot all countries are printed in terminal")
for country in range(5):
    print(f"a {countries[country]}")

"To Do: Task 1: Explain why the first loop printed all the countries and the second for loop did not"
# First loop printed all the countries as the range was the exact length of the List
# Second loops index range was limited to 5 (exclusively)
"Modify"
"To Do: Task 2: Modify the number in the second for loop range function from '5' to any other number and explain the output"
for country in range(random.randint(0, len(countries))):
    print(f"{countries[country]}")
# Selects randomly using randint
