//Grab h1 form element
const heading = document.querySelector('h1')
console.log(heading)

// Add an ID to the element h1
heading.setAttribute('id', 'title')

// Update of heading text
heading.innerText = 'New title added through JS'

// Creating new UL element
const newUl = document.createElement('ul')

// const liOne = document.createElement('li')
// const liTwo = document.createElement('li')
// const liThree = document.createElement('li')

// newUl.append(liOne, liTwo, liThree)

// liOne.classList.add('listItems')
// liTwo.classList.add('listItems')
// liThree.classList.add('listItems')

// liOne.innerText = "Hi 1"
// liTwo.innerText = "Hi 2"
// liThree.innerText = "Hi 3"

// document.body.append(newUl)

// const listItems = document.querySelectorAll('.listItems')
// console.log(listItems)



const newLiElements = ['item 1', 'item 2', 'item 3']

newLiElements.forEach(function(item) {
    // Create a <li> element
    let li = document.createElement("li");
    // Add the item text to the <li> element
    li.innerHTML = item;
    // Add the <li> element to the <ul> element
    newUl.appendChild(li);
  });



const body = document.querySelector('body')
body.append(newUl)

const liItems = document.querySelectorAll('li')

for (let i = 0; i < liItems.length; i++) {
    liItems[i].style.color ='red'
    liItems[i].style.textAlign = 'center'
    liItems[i].style.fontWeight = '800'
}

heading.remove()