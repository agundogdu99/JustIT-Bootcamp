// DOM

// Querying the DOM
    // Check for certain elements / Grab data

// getElementById()
const title = document.getElementById('title')
console.log(title)

// getElementsByClassName()
const listItems = document.getElementsByClassName('listItems')
console.log(listItems)

// getElementsByTagName()
const liElements = document.getElementsByTagName('li')
console.log(liElements)


// querySelector()
    // We pass in a CSS selector, and queryselector grabs the FIRST elemen
    // that matches from the DOM

const paragraph = document.querySelector('p')
console.log(paragraph)

//querySelectorAll()
    // grabs ALL elements that matches from DOM
const paragraphs = document.querySelectorAll('p')
console.log(paragraphs)




// STYLING an element with JS
title.style.color = 'Red'

// This doesnt work => because its multiple elemets (like an array) paragraphs.style.color = 'blue'
//Instead - 
for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.backgroundColor = 'blue'
    paragraphs[i].style.color = 'white'
}


// Creating an Element and adding it to the DOM
    // Store UL
const ul = document.querySelector('ul')
console.log(ul)

    // use createElement() to create a new list item

const newListItem = document.createElement('li')
console.log(newListItem)

    // Add the li to the ul using append()

    ul.append(newListItem)
    console.log(ul)

    // Modify text of the element using .innerText
    newListItem.innerText = 'Item 5 (New)'

// Modify / Add an attribute to an element
newListItem.setAttribute('id', 'itemFive')

// Remove an attribute from element
newListItem.removeAttribute('id')

// Add a class to an element
newListItem.classList.add('newclass')

// Remove a classList from an element
newListItem.classList.remove('newclass')

// Removing an element from the DOM
newListItem.remove()