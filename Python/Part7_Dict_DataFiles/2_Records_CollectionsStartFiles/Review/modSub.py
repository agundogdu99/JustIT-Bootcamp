def modulus ():
    num= int(input("Enter any  number: ")) # assign value to variable
    for i in range(1,num): # set the start value to be number 1 and the end value as user input number
        i+=1 # increment start value by 1 until it adds up to the user input value
        if i%10 ==0: #used modulus to not print any number divisible by 10 without remainder
            continue# continue with the loop 
        elif i>100:#checks if a number is greater than 100
            break# stops loop if the check condition is true
        else:print(i)#returns all values except those that are a multiple of 10
modulus()
