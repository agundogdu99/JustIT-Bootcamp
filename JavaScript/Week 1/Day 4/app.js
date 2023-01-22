// FUNCTIONS
    // Arrow Functions are most common
    // Functions are reusable blocks of code

    //Declaring an arrow function

    const greeting = () => {
        console.log('Hello World!')
    }

    // Call/Invoke the function

    greeting();


    // Light Switch Function example

    let lightsOn = false;

    const lightSwitch = () => {
        if (lightsOn) {
            lightsOn = false;
            console.log('Lights Off!')
        } else {
            lightsOn = true;
            console.log('Lights On!')
        }
    }

    // Call it

    lightSwitch();
    lightSwitch();
    lightSwitch();


// Functions with Parameters / Arguments

const atm = (accountNumber, amount) => {
    console.log(`
    Account #: ${accountNumber}
    Amount Withdrawn: £${amount}`)
}

atm(45646546, 2000)

// Global & Local Scope

const name = 'Lydia'
const age = 21
const city = 'London'

const getPersonInfo = () => {
    const name = 'Sarah'
    const age = 25
    const pet = "dog"
    console.log(`${name} is ${age} from ${city}. The city is coming from global scope`)
    return pet
    }

    getPersonInfo()


// Functions that call other functions

const secondsToMinutes = (seconds) => {
    return seconds / 60;
}
   
const secondsToHours = (seconds) => {
    return secondsToMinutes(seconds) / 60;
}

const secondsToDays = (seconds) => {
    return secondsToHours(seconds) / 24;
}

console.log(secondsToDays(186400))



// another example

const multiply10 = (num) => {
    return num * 10;
}

const multiply100 = (num) => {
    return multiply10(num) * 10;
}

console.log(multiply100(1))



// Different forms of syntax

    // Arrow - Modern
    const squaredArrow = (number) => {
        return number * number
    }

    // Function Declaration
    function squaredDeclaration(number) {
        return number * number;
    }

    // Anonymous Function
    const squaredAnon = function (number) {
        return number * number
    }

