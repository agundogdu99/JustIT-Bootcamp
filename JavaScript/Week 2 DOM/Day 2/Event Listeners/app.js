const heading = document.querySelector('#heading')
const addBtn = document.querySelector('#addBtn')
const addedElements = document.querySelector('#addedElements')
const deleteBtn = document.querySelector('#deleteBtn')
const myForm = document.querySelector('#myForm')
const inpField = document.querySelector('#inpField')


// Event handler
// heading.onclick = () => {
//     console.log("Hi")
// }



// Event Listener - Better!
heading.addEventListener('click', function(e) {
    console.log(e)
    console.log("Hi")
    console.log("Hey Hoo")
})

window.addEventListener('keydown', function (e) {
    // console.log(e.code)
    if (e.code === 'KeyP') {
        console.log('You just pressed P!!!!!')
    }
})

heading.addEventListener('mouseover', function () {
    heading.style.color = 'blue'
})

heading.addEventListener('mouseout', function (){
    heading.style.color = 'black'
})

// Butoon that adds an element to the DOM on click

addBtn.addEventListener('click', function (){
    newElement = document.createElement('h2')
    newElement.innerText = "I am a new Element"
    addedElements.append(newElement)
})



// Button that deletes an element on click

deleteBtn.addEventListener('click', function (){
    addedElements.lastChild.remove()
})


// Action performed when form data is reset
myForm.addEventListener('reset', function (){
    resetForm = document.createElement('p')
    resetForm.innerText = 'Form has succesfully been reset!'
    myForm.append(resetForm)
})

myForm.addEventListener('keydown', function (){
    resetForm.remove()
})




