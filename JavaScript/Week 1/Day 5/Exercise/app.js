// 1: Create an object called ‘person’ with keys of name age and city.
//      Add a method to the person object that greets the person using their name.

const person = {
  usersName: "Ahmet",
  age: 35,
  city: "London",
  greet() {
    console.log(`Hello ${this.usersName}!`);
  },
};

console.log(person.greet());

// 2: Without amending the original object I would like you to add an array of your
// favourite films to the person object. I would like you to then add a method to your
//object that returns a sentence stating the persons ‘name’, ‘age’ , ‘city’ and one
// of their favourite films.

person.favFilms = ["movie1", "movie2", "movie3"];

console.log(person.favFilms)
console.log(person)

person.aboutPerson = function() {
    return `${this.usersName}'s age is ${this.age} and lives in ${this.city}. One of his favourite films are ${this.favFilms[Math.floor(Math.random() * 3)]}`
};

// person.aboutPerson = () => {
//     return `${person.usersName} ${person.age} ${person.city} ${person.favFilms[0]}`
// };

console.log(person.aboutPerson())

// 3:  Create a pet object with the following properties: ‘name’, ‘typeOfAnimal’, ‘age’
// and ‘colour’. Incorporate a ‘drink’ method and an ‘eat’ method that returns a
// sentence about the animal eating or drinking.

const myPet = {
    petName: 'Rolo',
    typeOfAnimal: 'Dog',
    age: 7,
    colour: 'brown',
    drink () {
        return `Slurp Slurp... ${this.petName} said this water is Hydrating!`
    },
    eat () {
        return `${this.petName} the big ${this.colour} ${this.typeOfAnimal} enjoyed his meal!`
    }
}

console.log(myPet.eat())
console.log(myPet.drink())


// person.aboutPerson = function() {
//     return `${this.usersName}'s age is ${this.age} and lives in ${this.city}. One of his favourite films are ${this.favFilms[Math.floor(Math.random() * 3)]}`
// };



  