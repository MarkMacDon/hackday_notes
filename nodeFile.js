

/// SETUP
/// Install node.js and npm
/// Check that they are installed with 'npm -v' and 'node -v' respectively
/// npm init in folder


/// express is a minimalist web framework for node.js
const express = require('express');
/// bodyParser appears to be depricated but works
const app = express();
var bodyParser = require('body-parser')

const cors = require("cors");
const corsOptions ={
   origin:'*', 
   credentials:true,            //access-control-allow-credentials:true
   optionSuccessStatus:200,
}

app.use(cors(corsOptions)) 
app.use(bodyParser.json())

const urlString = '/';

var i = 1;
var x = 3;
var y = 5;

var responseJson = {}
/// When there is a GET request to the server...
app.get(urlString,(req,res) => {
    /// Respond with this json
    /// * you can view this by going to the url http://localhost:3000/changeDirection
    /// * or to the url <your-IP-address>:3000/changeDirection
    responseJson['coords'] = `(0,${x},${y},${x}),(1,${i},255,0),(2,255,255,0),(3,255,255,0),(4,255,255,0)`
    res.json(responseJson);
    /// var i keeps track of the number of get requests (increases every time the page is reloaded)
    i++;
    x++;
    y++;

    console.log('This will console.log every time there is a GET request (for ex. the page is reloaded)')
})

var jsonParser = bodyParser.json()

app.post(urlString, jsonParser, function (req, res) {
    // create user in req.body
    let bodyString = JSON.stringify(req.body);
    console.log(bodyString);
    if (bodyString.includes('Down')){
        responseJson['direction'] = 'Down'
    } else if (bodyString.includes('Up')){
        responseJson['direction'] = 'Up'
    } else if (bodyString.includes('Left')){
        responseJson['direction'] = 'Left'
    } else if(bodyString.includes('Right')){
        responseJson['direction'] = 'Right'
    }
    res.json(responseJson)
  })

// /// When there is a post request...
// app.post(urlString,(req,res) => {
//     console.log('This will console.log every time there is a POST request')

//     /// console.log the request body and headers
//     console.log(`BODY: ${req.body}`);
//     console.log(req.headers);
//     // send a json response to the POST request
//     res.json({"Response":'This is a post response from server'})
// });

// // /// Here is where we interact with the python scripts
const { spawn } = require('child_process');
/// create a child process, specifying language and file path (**can also add args here)
const pythonProcess = spawn('python3',["testpy.py"]);

/// listen for data on the child process stream...
pythonProcess.stdout.on('data', (data) => {
    /// when data is recieved,console.log it
    console.log(`DATA REVIEVED FROM testPy.py: ${data}`);
    // data is revieved as Uint8Array
    dataAsString = new TextDecoder().decode(data);
    console.log(dataAsString);
})

var port = 8080;
app.listen(port);
console.log(`Server started on port ${port}`); 

/// *** FOR YOUR SNAKE GAME ***

// direction = <direction from machine learning model>

// app.get(urlString,(req,res) => {
//   res.json({"Direction":`${direction}`})
// });
