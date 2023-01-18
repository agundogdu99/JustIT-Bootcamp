let myName = 'Ahmet';
console.log(`My name is ${myName}`);

// name, age, fav film

let myAge = '35';
let favFilm = 'Three Idiots';

console.log(`Hello, I am ${myName} and my favourite film is ${favFilm}`);

// ate bfast lunch dinner form yesterday - change variables for today

let breakfast = 'porridge';
let lunch = 'eggs & toast';
let dinner = 'stew with rice';

console.log(`Yesterday, I ate ${breakfast} for breakfast, ${lunch} for lunch and ${dinner} for dinner`);



breakfast = 'poached eggs';
lunch = 'sandwich';
dinner = 'chicken with rice';

console.log(`Today, I plan to eat ${breakfast} for breakfast, ${lunch} for lunch and ${dinner} for dinner`);



// string methods

let newBreakfast = breakfast.replace('poached eggs', 'fried eggs');

console.log(`Today, I plan to eat ${newBreakfast} for breakfast, ${lunch} for lunch and ${dinner} for dinner`);

console.log(breakfast.length)



let text = "Hello World"
let question = "How are you?"
console.log(text.concat(", ", question));



// math methods

let x = 5.687
console.log(Math.trunc(x));

console.log(Math.pow(4,2));
console.log(Math.sqrt(30));

// number between 1 & 20

let randomNumber = Math.ceil(Math.random() * 20)
console.log(randomNumber);


