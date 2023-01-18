// 1 - Create an array of your favourite Films / TV shows, up to 5 items. Using an array method add 2 more items to your array. Use a loop to cycle through the array and log each item to the console.
console.log('task 1')

let favFilms = ['movie1', 'movie2', 'movie3', 'movie4', 'movie5'];

favFilms.push('movie6', 'movie7')

for (let i = 0; i < favFilms.length; i++) {
    console.log(favFilms[i]);
}


 

// 2 - Use a loop to generate 10 random numbers between 1-100 and log them to the console.

console.log('task 2')

 for (let i = 0; i <=10; i++) {
    console.log(Math.ceil(Math.random() * 100))
 }



// 3 - Write a loop that counts backwards from 20-0, logging each number to the console.

console.log('task 3')

for (let i = 20; i >= 0; i--) {
    console.log(i);
}


// 4 - Write a loop to generate 5 random numbers between 1-50. For each number generated, check if the number is divisible by 5 or not. Log whether it is divisible or not to the console.

 console.log('task 4')

 let i = 0;
 let generatedNumber

 while (i < 5) {
    generatedNumber = Math.ceil(Math.random() * 50)
    i++
    if (generatedNumber % 5 === 0) {
        console.log(`The number ${generatedNumber} is divisible by 5!`)
    } else {
        console.log(`DARN! The number ${generatedNumber} is NOT divisible by 5!`)
    }
 };



// Additional Activity: If you manage to finish the tasks, spend some time experimenting with array methods to gain an understanding of how they can be put to use in our code.