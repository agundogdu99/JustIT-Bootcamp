const itemKey = document.getElementById('itemKey')
const itemValue = document.getElementById('itemValue')
const addBtn = document.getElementById('addBtn')
const clearStorage = document.querySelector('#clearStorage')
const getUl = document.querySelector('#get-ul')
const searchStorage = document.querySelector('#searchStorage')
const getSearch = document.querySelector('#getSearch')
const searchStorageBtn = document.querySelector('#searchStorageBtn')



addBtn.addEventListener('click', function () {
    const savedKey = itemKey.value
    const savedValue = itemValue.value

    if (savedKey && savedValue) {
        localStorage.setItem(savedKey, savedValue)
    }
})

clearStorage.addEventListener('click', function () {
    localStorage.clear();
    // getUl.remove()
    location.reload()
})



for (i = 0; i < localStorage.length; i++) {
    newLi = document.createElement('li')
    newLi.innerText = `${localStorage.key(i)} : ${localStorage.getItem(localStorage.key(i))} `
    getUl.append(newLi)
}


searchStorageBtn.addEventListener('click', function (e) {
    e.preventDefault()
    const searchedValue = localStorage.getItem(searchStorage.value)
    if (searchedValue) {
        getSearch.innerText = `The value of ${searchStorage.value} is : ${searchedValue}`
    } else {
        getSearch.innerText = `The item you have searched for does not exist`
    }
})


