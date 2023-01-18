// Conditions

// If / Else syntax

// if (condition) {
//     console.log('run this code')
// } else if (2nd condition) {
//     console.log(run this code)
// } else {
//     run this code
// }



// Weather Example :

let weather = 'rain';

// == DOUBLE == comparison Operator

if (weather == 'sunny'){
    console.log(`Weather is ${weather}`);
} else if (weather == 'rain') {
    console.log(`Oh no, the weather forecast is: ${weather}!`);
} else {
    console.log(`Your weather system is messed up...`);
}

// === Strict equality - triple operators checks if VALUE and DATA TYPE is the same
//      i.e. 100 and "100" are not the same 



//switch 

let day = 'wednesday'

switch(day) {
    case 'monday':
        console.log('Weekend is over, happy monday!')
        break;
    
    case 'tuesday':
        console.log('Its Tuesday')
        break;

    case 'wednesday':
        console.log('Its Wednesday!')
        break;
    
    default:
        console.log('its some other day')
}



let testScore = 65;

switch (true) {
    case testScore >= 70:
        console.log('Distinction');
        break;

    case testScore >= 60:
         console.log('Merit');
         break;

    case testScore >= 50:
        console.log('Pass');
        break;
    default:
        console.log('Fail');
}