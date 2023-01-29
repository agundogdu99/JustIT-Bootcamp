// Store the output div in a constant
const dataOutput = document.querySelector('.dataOutput')

// Asynchronous Function to fetch the external data
async function getData() {
    // Await the response from the API
    const response = await fetch("https://api.adviceslip.com/advice")
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

    // Create a P tag to store the advice 
    const adviceText = document.createElement('p')
    // Output the advice to the element
    adviceText.textContent = `"${apiData.slip.advice}"`
    // Add a class to the element for styling
    adviceText.classList.add('advice')
    // Add the advice element to the dataOutput div
    dataOutput.append(adviceText)
})