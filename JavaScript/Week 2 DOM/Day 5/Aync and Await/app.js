//Store DIV in constant
const dataOutput = document.querySelector('.dataOutput')

// Writing a async function fetch request to enable us to get data from any API
async function getData() {
    // Await the response from API
    const response = await fetch('https://api.adviceslip.com/advice')
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
    console.log(apiData.slip.advice)

    const adviceOutput = document.createElement('p')
    adviceOutput.innerText = `"${apiData.slip.advice}"`
    dataOutput.appendChild(adviceOutput)
})


