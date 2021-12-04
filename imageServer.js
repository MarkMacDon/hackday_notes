const http = require("http");
const path = require("path");
const fs = require("fs");

const express = require("express");
const app = express();

const multer = require("multer");
const upload = multer({ dest: 'uploads/' });
const { spawn } = require('child_process');

const urlString = "/upload"

const PORT = 3000;
let imageNumber = 0;
let num_lights = 10;

app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

// put the HTML file containing your form in a directory named "public" (relative to where this script is located)
app.get("/", express.static(path.join(__dirname, "./public")));

const handleError = (err, res) => {
  res
    .status(500)
    .contentType("text/plain")
    .end("Oops! Something went wrong!");
};


app.post(
  urlString,
  upload.single('file'),
  (req, res) => {
    const tempPath = req.file.path;
    const targetPath = path.join(__dirname, `./uploads/image${imageNumber}.jpg`);

    if (req.file.originalname.toLowerCase() === ".jpg") {
      fs.rename(tempPath, targetPath, err => {
        if (err) return handleError(err, res);

        pythonProcess = spawn('python3',["turn_on_light_for_picture.py", imageNumber]);
        pythonProcess.stdout.on('data', (data) => {
            /// when data is recieved, print it
            console.log(`${data}`);
        })
        // image0.jpg is background image
        if (imageNumber == 0) {
            console.log('Captured background image')
        }else {
            console.log(`Captured image number ${imageNumber} of ${num_lights}`);
        }
        res
          .status(200)
          .contentType("text/plain")
          .end(`${num_lights}`);
        imageNumber++;
      });
    } else {
      fs.unlink(tempPath, err => {
        if (err) return handleError(err, res);

        res
          .status(403)
          .contentType("text/plain")
          .end("Only .jpg files are allowed!");
      });
    }
    
  }
);

app.get("/image.jpg", (req, res) => {
    res.sendFile(path.join(__dirname, "./uploads/image.jpg"));
  });
