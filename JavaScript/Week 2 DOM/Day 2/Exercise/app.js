const heading = document.querySelector('h1')
console.log(heading)

heading.setAttribute('id', 'title')

heading.innerText = 'New title added through JS'


const newUl = document.createElement('ul')

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

for (let i = 0; i < document.querySelectorAll('li').length; i++) {
    document.querySelectorAll('li')[i].style.color ='red'
    document.querySelectorAll('li')[i].style.textAlign = 'center'
    document.querySelectorAll('li')[i].style.fontWeight = '800'
}

heading.remove()