const express = require('express');
const app = express();  
const { spawn } = require('child_process');

var bodyParser = require('body-parser')
var jsonParser = bodyParser.json()
app.use(bodyParser.json())

const cors = require('cors');
const corsOptions ={
    origin:'*', 
    credentials:true,            //access-control-allow-credentials:true
    optionSuccessStatus:200,
}
app.use(cors(corsOptions)) 


pythonProcess = spawn('python3',['node_communication.py']);

pythonProcess.stdout.on('data', (data) => {
    /// when data is recieved, print it
    console.log(`${data}`);
})
const urlString = '/';


var responseJson = {}

app.get(urlString,(req,res) => {
    //TODO get coords from snake game
    // var snakeCoordinates = ``
    // responseJson['coords'] = snakeCoordinates
    res.json(responseJson);

    console.log('This will console.log every time there is a GET request')
})

// When there is a post request this will check if it is coordinates or directions
// Then it will extract the relevant data and put it in a response
// This response can be viewed/accessed by going to the <hostIP>:PORT
app.post(urlString, jsonParser, function (req, res) {
    console.log(req.body)
    let bodyString = JSON.stringify(req.body);

    // Handles Direction
    if (bodyString.includes('Down')){
        responseJson['direction'] = 'Down'
    } else if (bodyString.includes('Up')){
        responseJson['direction'] = 'Up'
    } else if (bodyString.includes('Left')){
        responseJson['direction'] = 'Left'
    } else if(bodyString.includes('Right')){
        responseJson['direction'] = 'Right'
    }
    // Handles coordinates
    if (bodyString.includes('coordinates')) { // is coordinates
        responseJson['coords'] = bodyString
        console.log(`HERHERHE ${bodyString}`)
    }  

    console.log(`POST REQUEST BODY STRING ${bodyString}`)
    
    res.json(responseJson)
  })

var port = 8080;
app.listen(port);
console.log(`Server started on port ${port}`); 
 





/// ML model (posting dirction) Y => Node (repository) Y <=> 
// snake game (outputting coords) Y => Node (repository) => Pi (unpack overlay on new grid) 