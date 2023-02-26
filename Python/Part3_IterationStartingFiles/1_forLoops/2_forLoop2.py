# for variableName in rangeObject(numberOfIteration)
# for loops that use the range() function
# range() is the sequence that you are going to iterate through
# range() is a built-in function just like input().


# range(stop) -> range object range(start, stop[, step]) -> range object
# When you call the range function, you can pass it up to three values:
# The start number
# The end number
# The step

"To Do: Predict, then Run, and then Investigate"

"start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3"
for findNum in range(10):
    print(findNum)


"Modify/Make"
"To Do: Task 1: Use the notes above in green to help you create the code block to produce an output that start at 1 and ends at 20"
for i in list(range(1, 21)):
    print(i)


"To Do: Task 2: Use the notes above in green to help you create the code block to produce an output that has a start(1), stop(30) and a step (5)"
for i in list(range(1, 30, 3)):
    print(i)

"To Do: Task 2:  Modify the code with the step value to count down in steps of 5 (from a high number to a low number)"

for i in list(range(100, 50, -5)):
    print(i)

"Further reading on python for statements"
# https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements
