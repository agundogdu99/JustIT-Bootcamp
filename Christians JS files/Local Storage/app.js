const itemKey = document.getElementById('itemKey')
const itemValue = document.getElementById('itemValue')
const addBtn = document.getElementById('addBtn')
const deleteBtn = document.getElementById('deleteBtn')
const searchInput = document.getElementById('searchInput')
const searchBtn = document.getElementById('searchBtn')

addBtn.addEventListener('click', () => {
    const savedKey = itemKey.value
    const savedValue = itemValue.value

    if (savedKey && savedValue) {
        localStorage.setItem(savedKey, savedValue)
    }
})

// Output the data from local storage to the webpage
// for (let i = 0; i < localStorage.length; i++) {
//     const key = localStorage.key(i)
//     const value = localStorage.getItem(key)
//     let lsData = document.createElement('p')
//     lsData.setAttribute('id', `${key}`)
//     lsData.innerText = `${key} : ${value}`
//     document.body.append(lsData)
// }


// Button to clear local storage
deleteBtn.addEventListener('click', () => {
    localStorage.clear()
    location.reload()
})

// Search functionality
searchBtn.addEventListener('click', (e) => {
    e.preventDefault()
    const key = searchInput.value
    const searchResult = localStorage.getItem(key)
    const searchOutput = document.createElement('p')
    searchOutput.innerText = `Search Results: ${key} : ${searchResult}`
    document.body.append(searchOutput)
})