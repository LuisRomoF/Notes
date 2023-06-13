# API
APIs are a set of commands, functions, protocols and objects that programmers can use to créate software or interact with an external system.

APIs act as intermediaries, enabling developers to access the functionality and data of external systems, services, or platforms without needing to understand the underlying implementation details. They provide a standardized way for different software components to interact, facilitating interoperability and integration.

## Endpoint
An endpoint is an access point to send the HTTP requests to and get information back.
It represents a unique URL location or address that a client can send requests to in order to access a particular resource or perform a specific action.
Endpoints act as the interface between the client (such as a web browser or mobile application) and the server hosting the API.
Each endpoint is associated with a specific HTTP method, such as GET, POST, PUT, DELETE, etc.

## Paths
Paths refer to the specific component of a URL or URI that comes after the domain name or base URL. They are used to identify and locate a particular resource or endpoint within an API.
```
https://example.com/api/v1/thisisonepath

https://example.com/api/v1/thisisanotherpath
```

## Parameters 
Parameters help identify and query specific information in a more flexible way. They are set in as a key-value pair. Parameters come at the end of the url after the '?'
```
In this example the URL contains to keys (contains and flag) and their respective values (word and True)
https://example.com/api/v1?contains=word&flag=True
```

## Authentication 
A common way to implement authentification is by using Api Keys which are tied to each individual user. This keys are passed in the url as parameters.

```js
const express = requiere("express");
const https = require("https");

const app = express();

app.get("/", function(req, res){

    const url = "https://api.yourapi.org/..."

    http.get(url, function(response){
        console.log(response);

        response.on("data", function(data){
            const weatherData = JSON.parse(data)
        })
    })

    res.send("server is up and running")
})
```
