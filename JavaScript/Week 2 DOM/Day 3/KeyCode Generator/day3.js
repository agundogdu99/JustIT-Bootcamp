// Storing relevant elemts from the DOM
const overlay = document.querySelector('#overlay')
const container = document.querySelector('.container')
const eventKey = document.querySelector('#eventKey')
const eventCode = document.querySelector('#eventCode')
const eventKeyCode = document.querySelector('#eventKeyCode')


window.addEventListener('keydown', function(e){
    console.log(e)
    console.log(e.key)
    console.log(e.code)
    console.log(e.keyCode)
    // On keypress - Hide the overlay div
    overlay.style.display = 'none'
    // On keypress - Display container
    container.style.display = 'flex'


    if (e.code === 'Space') {
        eventKey.innerText = 'Space'
    eventKeyCode.innerText = e.keyCode
    eventCode.innerText = e.code
    } else {
        eventKey.innerText = e.key
    eventKeyCode.innerText = e.keyCode
    eventCode.innerText = e.code
    }
})