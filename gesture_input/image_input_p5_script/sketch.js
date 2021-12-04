// Teachable Machine
// The Coding Train / Daniel Shiffman
// https://thecodingtrain.com/TeachableMachine/2-teachable-game.html
// https://editor.p5js.org/codingtrain/sketches/tqoOkW_ai

// The video
let video;
let flipVideo;

// Storing the label
let label = "waiting...";

// The classifier
let classifier;
let modelURL = 'https://teachablemachine.withgoogle.com/models/-7PRcXdAr/';

// STEP 1: Load the model!
function preload() {
  classifier = ml5.imageClassifier(modelURL + 'model.json');
}

function setup() {
  createCanvas(640, 480);
  // Create the video
  video = createCapture(VIDEO);
  video.size(640, 480);
  video.hide();
  // Mirror the video since we trained it that way!
  flipVideo = ml5.flipImage(video);

  // STEP 2: Start classifying
  classifyVideo();

  // frameRate(5);

}

// STEP 2 classify!
function classifyVideo() {
  // Flip the video!
  flipVideo = ml5.flipImage(video);
  classifier.classify(flipVideo, gotResults);
  flipVideo.remove()
}

function draw() {
  background(255);

  // Draw the video?
  image(flipVideo, 0, 0);
  textSize(32);
  fill(0);
  text(label, 10, 50);
  console.log(label)
  

  }

  noStroke();
  fill(255, 0, 0);
  rect(food.x, food.y, 1, 1);

// STEP 3: Get the classification!
function gotResults(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  label = results[0].label;
  // classify again!
  classifyVideo();
}
