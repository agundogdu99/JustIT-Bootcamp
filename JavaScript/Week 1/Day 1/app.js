console.log('Hello');

// Data Types:

// String
console.log('Hello');

// Number - no quotation marks
console.log(5);

// Decimal

// Boolean
    // True False
    console.log(true);
    console.log(false);

// Undefined
console.log(undefined);

// Null
console.log(null);




//Properties

// e.g. Get length of string - .length
console.log("Hello World".length)




// Methods - need the brackets

// e.g. 
console.log("method example".toUpperCase());



// Math Library
    // e.g. Math.Random -  Generates a number between 0-1
    console.log(Math.random());

// Chaining methods
    // Round Down to get random whole number
    console.log(Math.floor(Math.random() * 10))

    //Round using Math.round()
    console.log(Math.round(Math.random() * 10))

    // Round UP using Math.ceil()
    console.log(Math.ceil(Math.floor() * 10))




// Variables

    // Storing data in variable that we canaccessand work with

    // var - Do not use - old method
    var doNotUse = "OLD & INVALID";

    // let
    let canChange = 'can be re-assigned';

    // const
    const cantChange = 'cannot be re-assigned';



// = assignment operator
let x = 100;
console.log(x)

// x = x + 100; OR
x += 100

console.log(x);


// Concatenation

let day = 'Monday';

console.log('Today is ' + day);
// OR use TEMPLATE LITERAL
console.log(`Today is ${day}`);