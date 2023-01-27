// DOM = Document Object Model

// Querying the DOM

// getElementById()
// Selects the element with the corresponding ID from the DOM
const title = document.getElementById('title')
// console.log(title)

// getElementsByClassName()
// Selects all elements with the corresponding className from the DOM
const listItems = document.getElementsByClassName('listItems')
// console.log(listItems)

// getElementsByTagName()
// Selects all elements with the corresponding TagName from the DOM
const liElements = document.getElementsByTagName('li')
// console.log(liElements)

// querySelector()
// We pass in a CSS selector and querySelector grabs the first element
// that matches from the DOM
const paragraph = document.querySelector('p')
// console.log(paragraph)

// querySelectorAll()
// We pass in a CSS selector and querySelectorAll grabs all the elements
// that matches from the DOM
const paragraphs = document.querySelectorAll('p')
// console.log(paragraphs)

// Styling an Element with JS
title.style.color = "Red"

// paragraphs.style.color = "Blue"
for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.backgroundColor = "Blue"
}

// Creating an Element and adding it to the DOM

// Store the UL in an element
const ul = document.querySelector('ul')
// console.log(ul)

// Use createElement() to create a new list item
const newListItem = document.createElement('li')
// console.log(newListItem)

// Add the li to the ul using append()
ul.append(newListItem)
// console.log(ul)

// Modify text of element using .innerText
newListItem.innerText = `Item 5 (New)`

// Modify / Add an attribute to an element
newListItem.setAttribute('id', 'itemFive')

// Remove an attribute from an element
newListItem.removeAttribute('id')

// Add a class to an element
newListItem.classList.add('newClass')

// Remove a classList from an element
newListItem.classList.remove('newClass')

// Removing an element from the DOM
newListItem.remove()


// Traversing the DOM
// console.log(ul)
// console.log(ul.parentElement)
// console.log(ul.parentNode)

const htmlElement = document.documentElement
console.log(htmlElement)
console.log(htmlElement.parentElement)
console.log(htmlElement.parentNode)

// Child Node Traversal
console.log(ul.childNodes)
console.log(ul.childNodes[1])
console.log(ul.firstChild)
console.log(ul.lastChild)

// Select just the element children
console.log(ul.children)
console.log(ul.firstElementChild)
console.log(ul.lastElementChild)

// Clone an Element
const itemTwo = ul.children[1]
console.log(itemTwo)

const itemTwoClone = itemTwo.cloneNode(true)

ul.append(itemTwoClone)

// Check for Sibling Relationship
console.log(ul.previousSibling)
console.log(ul.nextSibling)

// Check for element only simbling relationship
console.log(ul.previousElementSibling)
console.log(ul.nextElementSibling)


