# Javascript
## Variable definition

```javascript
var myVariable = "Content";
var myVariable = 123;
var myVariable = true;
var yourInput = prompt("Type your input");
alert("this will be printed on screen");
```
## String Concatenation
```js 
var message = "Hello";
var name = "User";

// This is a comment
alert(message + " there, " + name);

/* This is 
a multiline
comment*/ 
```
## String functions
```js
// This will tell you the length of your string
var text = "This is a string"
alert(text.length); // This would print 16

text.slice(0,2) // This would print "Th"

text.toUpperCase(); //Transform the string to all uppercase
text.toLowerCase(); //Transform the string to all lowercase
```
## Functions
```js
function myFunction (parameter){
    //content of the function
    var newVar = 1.5 * parameter;
    return newVar;  
}

function lifeInWeeks(age) {
    var x = (90 * 365) - (age * 365);
    var y = (90 * 52) - (age * 52);
    var z = (90 * 12) - (age * 12);
    
    console.log("You have "+ x +" days, "+ y + " weeks, and " + z + " months left.");
}

function bmiCalculator(weight,height){
    var bmi = ((weight)/(height*height));
    return Math.round(bmi);
}

// get random element from array
function whosPaying(elements) {
    var rand = Math.floor(Math.random() * elements.length);
    return elements[rand];
}
```
## Control Flow Statements
#### IF Statement
```js
if (myVar === "value"){
    // this executes if true
}else{
    //this executes if false
}
```
#### While Loop
```js
while (condition){
    // this executes if true
}
```
#### For Loop
```js
//for(start,end, change)
for (i=0; i<100; i++){
    // Do something
}
```

## Comparators
* "===" is equal to, this one checks for equality including datatypes
* "==" equals to but this one doesnt check if the data types are equal
* "!==" is not equal to
* <,>,<=,>=
* "&&" AND
* "||" OR
* "!"  Not, the opposite of something
```js
function bmiCalculator (weight, height) {
    var bmi = weight/(height*height)
    var interpretation = ""
    if (bmi<18.5){
        interpretation = "Your BMI is "+ bmi+", so you are underweight."
    }else if (bmi>=18.5 && bmi<=24.9){
        interpretation = "Your BMI is "+ bmi+", so you have a normal weight."
    } else {
        interpretation = "Your BMI is "+ bmi+", so you are overweight."
    }
    return interpretation;
}
```

## Collections 
```js
var myArray = ['element1','element2']
myArray.length;
myArray.includes('element1') // this returns a boolean
var extract = myArray[0] // this returns the first element of the array

// Add elements
myArray.push(new_element)
// Remove elements
myArray.pop()
```

## Event Listeners
```js
var numberOfButtons = document.querySelectorAll(".myButton").lenght;

for (var i=0; i < numberOfButtons; i++){
    // here we use an anonymous function to perform actions when clicked
    document.querySelectorAll(".drum")[i].addEventListener("click",function(){
        alert("I got clicked!");
    })
}
```

## Objects
```js
var myObject = {
    name: "myName",
    myBool: true,
    myInt: 19
    myColl: ["coll1","coll2"]
}

// you can call the object properties this way
alert("My object has the following bool property" + myObject.myBool )
```
To generalize this and use it multiple times you can use a **Constructor Function**
```js
function myObject (myName,myInt,myBool,myColl){
    this.myName=myName;
    this.myInt=myInt;
    this.myBool=myBool;
    this.myColl=myColl;
    // object method
    this.myMethod = function(){
        //execute this if myMethod gets called
    } 
}

// To initialize the object
var newObject = new myObject("name",19,true,["coll1","coll2"]);
```

## Function Types
* **Higher Order Function:** They take other functions as parameters/inputs
* **Callback Function:** this are the functions that get passed to a Higher order function