// Grab h1 element from the DOM
const heading = document.querySelector('h1')

// Add an ID to the h1 element
heading.setAttribute('id', 'heading')
// heading.classList.add('heading')

// NOTE: Styling via the DOM will overwrite external CSS
// heading.style.color = "Red"

// Update text of heading
heading.innerText = "New Title"

// Create an unordered list element
const newUL = document.createElement('ul')

// Creaated individual list itmes
const liOne = document.createElement('li')
const liTwo = document.createElement('li')
const liThree = document.createElement('li')

// Added all the listItems to the UL
newUL.append(liOne, liTwo, liThree)

// Gave the listItmes a class
liOne.classList.add('listItems')
liTwo.classList.add('listItems')
liThree.classList.add('listItems')

// Assinged the innerText value of the list items
liOne.innerText = "Item One"
liTwo.innerText = "Item Two"
liThree.innerText = " Item Three"

// Added the unordered list with the list items to the body
document.body.append(newUL)

// Stored listItems in a nodelist
const listItems = document.querySelectorAll('.listItems')
console.log(listItems)

// Looped through the list items to style the elements
for (let i = 0; i < listItems.length; i++) {
    listItems[i].style.color = "Blue"
}

// Remove an element
// heading.remove()





