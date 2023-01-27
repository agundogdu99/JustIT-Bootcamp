// JSON - JavaScript Object Notation

// Differences:

// Works in key/value pairs - both wrapped in double quotes
// Cannot contain functions (methods)
// Can be created and interpreted by other langunages
// Popular method of transferring data - commonly used by APIs

let JSONObj = { "firstName": "David", "lastName": "Smith", "age": 27, "married": true }

let JSONArray = ["Red", "Green", "Blue"]

let JSONNested = [{ "name": "James", "age": 35 }, { "name": "Hannah", "age": 30 }]

// console.log(JSONNested)
// console.log(JSONNested[1].name)

let JSONString = `{
    "people":[
      {"firstName":"David", "lastName":"Smith", "age": 27, "married": true},
      {"firstName":"Amy", "lastName":"Blake", "age": 43, "married": true},
      {"firstName":"Mark", "lastName":"Foster", "age": 56, "married": false}
    ]
    }`

// parse - Take a JSON String and convert it to a workable JSON Object

// strinify - Takes a JSON Object and converts it to a string that can be transferred

// console.log(JSONString)

// const JSONObject = JSON.parse(JSONString)
// console.log(JSONObject)

// Mock Data Example
// Element Imports
const firstName = document.getElementById('firstName')
const lastName = document.getElementById('lastName')
const email = document.getElementById('email')

const mockData = [{ "id": 1, "first_name": "Jessie", "last_name": "Chaise", "email": "jchaise0@biblegateway.com", "gender": "Female" },
{ "id": 2, "first_name": "Dee dee", "last_name": "Tapply", "email": "dtapply1@reddit.com", "gender": "Female" },
{ "id": 3, "first_name": "Kariotta", "last_name": "Appleby", "email": "kappleby2@digg.com", "gender": "Female" },
{ "id": 4, "first_name": "Ilse", "last_name": "Morlon", "email": "imorlon3@typepad.com", "gender": "Female" },
{ "id": 5, "first_name": "Mellisa", "last_name": "Berrigan", "email": "mberrigan4@msn.com", "gender": "Female" },
{ "id": 6, "first_name": "Nolan", "last_name": "Pile", "email": "npile5@jimdo.com", "gender": "Male" },
{ "id": 7, "first_name": "Job", "last_name": "Hawse", "email": "jhawse6@dagondesign.com", "gender": "Male" },
{ "id": 8, "first_name": "Free", "last_name": "Newlands", "email": "fnewlands7@imageshack.us", "gender": "Male" },
{ "id": 9, "first_name": "Valentijn", "last_name": "Wraxall", "email": "vwraxall8@reddit.com", "gender": "Male" },
{ "id": 10, "first_name": "Peadar", "last_name": "Medlar", "email": "pmedlar9@phpbb.com", "gender": "Male" }]

console.log(mockData)

firstName.innerText = mockData[0].first_name
lastName.innerText = mockData[0].last_name
email.innerText = mockData[0].email