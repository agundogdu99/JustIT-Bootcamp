const heading = document.querySelector('#heading')
const addBtn = document.querySelector('#addBtn')
const deleteBtn = document.querySelector('#deleteBtn')
const addedElements = document.querySelector('#addedElements')

// Event Handler -
// heading.onclick = () => {
//     console.log("Event Handler")
// }

// heading.onclick = () => {
//     console.log("Message 2")
// }

// Event Listener
heading.addEventListener("click", (e) => {
    console.log(e)
})

// heading.addEventListener("click", () => {
//     console.log("Message 2")
// })

// Keypress event / Event Object
window.addEventListener("keypress", (e) => {
    if (e.code == "KeyP") {
        console.log("You just pressed the P key")
    }
})

// Mouseover Event 
heading.addEventListener("mouseover", () => {
    heading.style.color = "Blue"
})

// Mouseout Event
heading.addEventListener("mouseout", () => {
    heading.style.color = "Black"
})

// Button that adds element to the DOM on click
let newElement = ""

addBtn.addEventListener("click", () => {
    newElement = document.createElement('h2')
    newElement.innerText = "I am a new element!"
    addedElements.append(newElement)
})


// Button that deletes an Element on Click
deleteBtn.addEventListener("click", () => {
    addedElements.lastChild.remove()
})