def multiples(a,b):
    if a%b == 0: # check if a divides by b
        return "Yes"
    else:
        return "No"

answer = multiples(10, 2)
print(f"The answer is {answer} ")