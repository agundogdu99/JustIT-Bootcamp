// TASKS:

// Write a conditional statement that checks whether a customer is old enough to be served alcohol at a bar. Log a message to the console depending on the age of the customer.

let customerAge = 15;

if (customerAge < 18) {
    console.log(`You are ${customerAge} - We cannot serve you. You must be a minimum age of 18.`)
} else {
    console.log(`You are ${customerAge}. Being above 18, we can serve you!`)
}

// Declare a variable called "Password". Write an if statement that checks how many characters are in the password. If the password has 8 or more characters log the password to the console, if the password has less than 8 characters log to the console that the password is too short.

let password = 'password1234'
 if (password.length >= 8) {
    console.log('Your password has more than 8 characters. Your password is: ' + password);
 } else {
    console.log('Your password is too short');
 }


 // Create a variable that stores a number. Check whether the number is divisible by 3 or 5, if so log "This number is divisible by 3 or 5" to the console. Otherwise log an alternate message to the console.

 let num1 = 9;

 if (num1 % 3 === 0 || num1 % 5 === 0) {
    console.log(`Your number: ${num1}, is divisible by 3 OR 5`);
 } else {
    console.log(`Your number: ${num1}, is NOT divisible by 3 OR 5`);
 }



 // Create a variable that stores a number. Check if the number is divisible by 3, if so log "fizz" to the console. Check if the number is divisible by 5 and if so log "buzz" to the console. If the number is divisible by both 3 and 5, log "fizz buzz" to the console. Otherwise log the number to the console.

 if (num1 % 3 === 0 && num1 % 5 === 0) {
    console.log('fizz buzz');
 } else if (num1 % 3 === 0) {
    console.log('fizz')
 } else if (num1 % 5 === 0) {
    console.log('buzz')
 } else {
    console.log(num1)
 }
 
 
// Write some code to check whether or not a number is a palindrome (read the same backwards as it is forwards. e.g. 1001 is 1001 backwards).

 let checkPalindrome = 1001;
 let numString = checkPalindrome.toString()
 let reverseNum = numString.split('').reverse().join('');


if (numString === reverseNum) {
    console.log('Number is a palindrome!');
} else {
    console.log('Not a Palindrome')
}