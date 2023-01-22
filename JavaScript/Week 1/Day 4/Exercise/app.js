// 1: Write a function that takes in a name as a parameter and returns a personalised greeting.
 console.log('task 1')

 const greeting = (name) => {
    return `Hello ${name}! Welcome to JS Functions...`
 }

 console.log(greeting('Ahmet'))


// 2: Write a function that takes in a number as a parameter and checks whether the number is odd or even.

console.log('task 2')

const checkOddOrEven = (num) => {
    if (num % 2 === 0) {
        return `Number: ${num} is EVEN`
    } else {
        return `Number: ${num} is ODD` 
    }
}

console.log(checkOddOrEven(10))
 

// 3: Write an ATM function that takes in a pin number and withdrawal amount as parameters. 
// The pin must match a stored pin value and the withdrawal amount must be lower than the account balance value. 
// If the pin is correct and the withdrawal amount is less than the balance, approve the 
// transaction. If the pin is incorrect or funds are insufficient, decline the transaction.



const checkAtmWithdrawal = (userPin, amount) => {
    const storedPin = 1234
    const accountBalance = 1000

    if (userPin === storedPin && amount <= accountBalance) {
        return `Your Transaction has been approved. £${amount} withdrawn. New Balance: £${accountBalance - amount}`
    } else if (userPin !== storedPin) {
        return `You have entered an incorrect Pin`
    } else if (userPin === storedPin && amount > accountBalance) {
        return 'You have Insufficient funds to make this transaction'
    } else {
        `Your transaction cannot be made at this time. Systems Down`
    }
}

console.log(checkAtmWithdrawal(1234, 300))
