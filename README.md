# hackday_notes
This is a repo for collaboration on the gesture control part of a snake game 
which will run on a set of programmable christmas tree lights. 

The gesture input is provided by a tensorflow.js model and will recognise 4 directions
Left, Right, Up and Down, either through the pose model using pointing gestures, 
or through the image model using a black arrow drawn on white paper. 

The output of the model will be hosted on a node server which will be accessable by
a python script which runs the snake game. The node server will also host the coordinates of the snake's
body and make this accessible to a raspberry pi running the lights. 
