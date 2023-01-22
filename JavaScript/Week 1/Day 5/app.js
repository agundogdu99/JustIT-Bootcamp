// Objects

// Properties = the Data contained within an object
// Methods = Functions within objects. Things that the object can
// Objects work with KEY VALUE pairs
// "KEY : 'Value'"

// Object Example -

const coffeeShop = {
  name: "Costa",
  branchNumber: 250,
  specialOffers: true,
  drinksMenu: ["americano", "latte", "tea"],
};

console.log(coffeeShop);

// We can access object data or methods/properties
// dot notation
console.log(coffeeShop.name);
console.log(coffeeShop.drinksMenu[0]);

// bracket notation
console.log(coffeeShop["branchNumber"]);

// We can add new key/value pairs to an object that already exists
coffeeShop.desserts = ["blueberry muffin", "chocolate muffin"];

console.log(coffeeShop);

// We can UPDATE property values
coffeeShop.branchNumber = 100;
//OR coffeeSop['branchNumber'] = 100
console.log(coffeeShop);

// Adding offers to the coffeeShop object
coffeeShop.breakfastOffer = "Free bagel with any Coffee!";
coffeeShop.lunchOffer = "Free coffee with any sandwich!";

console.log(coffeeShop);

let time = 1000;
let offer = "no offer";

if (time < 1100) {
  offer = coffeeShop.breakfastOffer;
  console.log(offer);
} else if (time < 1500) {
  offer = coffeeShop.lunchOffer;
  console.log(offer);
}

// Adding Methods to our object (functions within objects)

coffeeShop.open = () => {
  return "We are Open";
};

coffeeShop.close = () => {
  return "Sorry, we are closed...";
};

console.log(coffeeShop);
console.log(coffeeShop.close());

//
//
//

// Alarm Clock Object
const alarm = {
  weekendAlarm: "Sleep in it's the weekend",
  weekDayAlarm: "Get up at 7:00 am",
  checkAlarm(day) {
    if (day === "saturday" || day === "sunday") {
      return this.weekendAlarm;
    } else {
      return this.weekDayAlarm;
    }
  },
};

console.log(alarm.checkAlarm("sunday"));
