/// SETUP
/// Install node.js and npm
/// Check that they are installed with 'npm -v' and 'node -v' respectively
/// npm init in folder


/// express is a minimalist web framework for node.js
const express = require('express');
/// bodyParser appears to be depricated but works
const app = express();

const urlString = '/changeDirection';

var i = 1;
/// When there is a GET request to the server...
app.get(urlString,(req,res) => {
    /// Respond with this json
    /// * you can view this by going to the url http://localhost:3000/changeDirection
    /// * or to the url <your-IP-address>:3000/changeDirection
    res.json({"Test" : `Message number ${i} sent to url from Server`});
    /// var i keeps track of the number of get requests (increases every time the page is reloaded)
    i++;

    console.log('This will print every time there is a GET request (for ex. the page is reloaded)')
})


/// When there is a post request...
app.post(urlString,(req,res) => {
    console.log('This will print every time there is a POST request')

    /// print the request body and headers
    console.log(req.body);
    console.log(req.headers);
    // send a json response to the POST request
    res.json({"Response":'This is a post response from server'})
});

/// Here is where we interact with the python scripts
const { spawn } = require('child_process');
const { TextDecoder } = require('util');
/// create a child process, specifying language and file path (**can also add args here)
const pythonProcess = spawn('python3',["testpy.py"]);

/// listen for data on the child process stream...
pythonProcess.stdout.on('data', (data) => {
    /// when data is recieved, print it
    console.log(`DATA REVIEVED FROM testPy.py: ${data}`);
    // data is revieved as Uint8Array
    dataAsString = new TextDecoder().decode(data);
    console.log(dataAsString);
})

var port = 3000;
app.listen(port);
console.log(`Server started on port ${port}`); 

/// *** FOR YOUR SNAKE GAME ***

// direction = <direction from machine learning model>

// app.get(urlString,(req,res) => {
//   res.json({"Direction":`${direction}`})
// });
