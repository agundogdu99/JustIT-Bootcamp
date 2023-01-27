// Storing relevant elements from the DOM
const overlay = document.querySelector('#overlay')
const container = document.querySelector('.container')
const eventKey = document.querySelector('#eventKey')
const eventCode = document.querySelector('#eventCode')
const eventKeyCode = document.querySelector('#eventKeyCode')

window.addEventListener('keydown', (e) => {
    // On keypress hide the overlay div
    overlay.style.display = "none"
    // On keypress show the container with info
    container.style.display = "flex"

    if (e.code === "Space") {
        eventKey.innerText = "Spacebar"
        eventCode.innerText = e.code
        eventKeyCode.innerText = e.keyCode
    } else {
        eventKey.innerText = e.key
        eventCode.innerText = e.code
        eventKeyCode.innerText = e.keyCode
    }
})