# Node.JS
Node is a runtime environment for javascript. It allows us to run and use js in our computer.
Node REPL (Read, Evaluate, Print, Loop)

To use node and run js files from the terminal you can use the following command:
```cmd
node yourScript.js
```

### Native Modules
This are the built in modules


```js
// fs stands for File System and its the module that lets you handle and manage files in the system
const fs = require("fs"); //common js module import
import "fs" // ESM module import (new way of importing). For this to work you need to set the type config of your project to module based

fs.writeFile("myNewFile.txt", "Hello World from Node.js", (err)=>{
    if (err) throw err;
    console.log("The file has been saved");
});

fs.readFile("myFile.txt", "utf-8", (err)=>{
    if (err) throw err;
    console.log("The file has been loaded");
});
```
### Installing Modules
Node Package Manager (NPM) its the main package manager for Node.js
```cmd
The followinng commands execute the same instructions
npm install "packageToInstall"
npm i ""packageToInstall"
```
