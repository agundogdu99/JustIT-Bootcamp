// Store the output div in a constant
const dataOutput = document.querySelector('#dataOutput')

// Asynchronous Function to fetch the external data
async function getData() {
    // Await the response from the API
    const response = await fetch("https://hp-api.onrender.com/api/characters")
    // We wait on the reponse and convert it to JSON upon receiving it
    const apiData = response.json()
    // Once received we return the api data in order to work with it
    return (apiData)
}

// addEventlistener to await our page loading
document.addEventListener("DOMContentLoaded", async () => {
    // Declare an empty array to store the data
    let apiData = []

    // Try catch to catch an error if fetch is unsuccessful
    try {
        // Try to fetch the data
        apiData = await getData()
    } catch (error) {
        // If any error occurs log it to the console
        console.log(error)
    }

    // We now have the apiData to work with
    console.log(apiData)

    for (let { name, image, house } of apiData) {
        const cardContainer = document.createElement('div')
        cardContainer.classList.add('cardContainer')
        const imageContainer = document.createElement('div')
        imageContainer.classList.add('imageContainer')
        const characterName = document.createElement('h2')
        characterName.innerText = `${name}`
        cardContainer.append(characterName)
        const characterHouse = document.createElement('h3')
        characterHouse.innerText = `${house}`
        cardContainer.append(characterHouse)
        cardContainer.append(imageContainer)
        const characterImage = document.createElement('img')
        characterImage.setAttribute('src', image)
        imageContainer.append(characterImage)
        dataOutput.append(cardContainer)
    }
})