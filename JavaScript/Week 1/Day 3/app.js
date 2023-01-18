// Arrays

let coffeeOrder = ["James - Americano", "Hannah - Frappucino", "Alex - Latte"];

console.log(coffeeOrder);
console.log(coffeeOrder[2]);

coffeeOrder[1] = "Hannah - Tea";

console.log(coffeeOrder);

// Side Note - look into array methods

// array length
console.log(coffeeOrder.length);

coffeeOrder.push("Christian - Water");
console.log(coffeeOrder);

coffeeOrder.pop();

//

// ++ operator
// placed before
// placed afater


let colors = ["red", "blue", "green", "yellow", "purple"];
console.log(colors);

// for loop
for (let i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}

colors.forEach(item => console.log(item));

//multiples of 2 loop

let multiplesOfTwo = [];

for (let i = 1; i <= 20; i++) {
    if (i % 2 === 0) {
        multiplesOfTwo.push(i);
    }
}

console.log(multiplesOfTwo);


// While Loop

let number = 0

while (number <= 10) {
    console.log(number)
    number++
}

// While Loops example 2

let cards = ['diamond', 'club', 'heart', 'spade'];

let currentCard = cards[Math.floor(Math.random() * cards.length)]

while (currentCard !== 'spade') {
    console.log(currentCard)
    currentCard = cards[Math.floor(Math.random() * cards.length)]
}



console.log('do while')

// Do While Loop
//evaluates the condition after the code has run
// will run at least once!

let x = 5
let y = 0

do {
    x = x + y
    console.log(x)
    y++
} while (y < 10);
