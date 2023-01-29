//Store DIV in constant
const dataOutput = document.querySelector('.dataOutput')

// Writing a async function fetch request to enable us to get data from any API
async function getData() {
    // Await the response from API
    const response = await fetch('https://thronesapi.com/api/v2/Characters')
    // We wait on the response and convert it to JSON upon receiving it
    const apiData = response.json()
    //Once received we return the api data in order to work with it
    return (apiData)
}

// addEventListener to await our page loading

document.addEventListener('DOMContentLoaded', async function() {
    // Declare an empty array to store data
    let apiData = []

    // Try Catch block to catch an error if fetch is unsuccessful
    try {
        // Try to fetch the Data
        apiData = await getData()
    } catch (error) {
        // If an error occurs, log it to the console
        console.log(error)
    }
    // We now have the API data to work with
    console.log(apiData)

    for (let { firstName, lastName, imageUrl } of apiData) {
        const cardContainer = document.createElement('div')
        cardContainer.classList.add('cardContainer')

        const characterName = document.createElement('h2')
        characterName.innerText = `${firstName} ${lastName}`
        cardContainer.append(characterName)

        const imageContainer = document.createElement('div')
        imageContainer.classList.add('imageContainer')
        cardContainer.append(imageContainer)
        const characterImage = document.createElement('img')
        characterImage.setAttribute('src', imageUrl)
        imageContainer.append(characterImage)    
        
        dataOutput.append(cardContainer)
    }

    // const adviceOutput = document.createElement('p')
    // adviceOutput.innerText = `"${apiData.slip.advice}"`
    // dataOutput.appendChild(adviceOutput)
})


