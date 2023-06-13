# Express.JS
Its a js framework that allows us to create backend structures.

```js
const express = requiere("express");
const bodyParser = requiere("body-parser");

const app = express();
app.use(bodyParser.urlencoded({extended: true}));

app.get("/",function(req, res){
    res.sendFile(__dirname + "/index.html");
    //__dirname is a built-in variable used to get the current path dynamically
});

app.post("/",function(req, res){
    var num1 = Number(req.body.n1);
    var num2 = Number(req.body.n2); //parseFloat(req.body.n2) this would be the casting in case they were floats

    var result = num1 + num2;
    res.send("The result of the calculation is " + result);
})

app.listen(3000,function(){
    console.log("Server started on port 3000");
});
```