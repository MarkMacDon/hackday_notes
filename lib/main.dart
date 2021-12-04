import 'dart:io';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:camera/camera.dart';
import 'package:http_parser/http_parser.dart';

import 'package:path_provider/path_provider.dart';
import 'package:shared_preferences/shared_preferences.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final cameras = await availableCameras();
  final firstCamera = cameras.first;
  final SharedPreferences prefs = await SharedPreferences.getInstance();
  runApp(MyApp(firstCamera: firstCamera, prefs: prefs));
}

class MyApp extends StatelessWidget {
  final firstCamera;
  final prefs;
  MyApp({this.firstCamera, this.prefs});
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(
        title: 'Flutter Demo Home Page',
        camera: firstCamera,
        prefs: prefs,
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage(
      {Key key, this.title, @required this.camera, @required this.prefs})
      : super(key: key);

  final String title;
  final CameraDescription camera;
  final SharedPreferences prefs;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  CameraController _controller;
  Future<void> _initializeControllerFuture;
  int imageIndex = 1;
  File _image;
  FileImage _backgroundImage;

  String recievedMessage = 'Message not yet recieved';
  void sendMessageToServer() async {
    var client = http.Client();
    try {
      var url = 'http://192.168.1.72:3000/upload';
      client.post(url,
          body: json.encode({'start': 'Start sending images'}),
          headers: {'Content-type': 'application/json'});

      http.Response getResponse = await http.get(url);
      print('Message recieved from Server: ${getResponse.body}');

      setState(() {
        recievedMessage = getResponse.body.toString();
      });
    } finally {
      client.close();
    }
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    // To display the current output from the Camera,
    // create a CameraController.
    _controller = CameraController(
      // Get a specific camera from the list of available cameras.
      widget.camera,
      // Define the resolution to use.
      ResolutionPreset.medium,
    );

    // Next, initialize the controller. This returns a Future.
    _initializeControllerFuture = _controller.initialize();
  }

  @override
  void dispose() {
    // Dispose of the controller when the widget is disposed.
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                'Send and Recieve Message From Server',
                style: TextStyle(fontSize: 22),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 20),
              Transform.scale(
                scale: 3.0,
                child: TextButton(
                    onPressed: () => sendMessageToServer(),
                    child: Text('Send')),
              ),
              SizedBox(height: 20),
              Text(recievedMessage),
              SizedBox(height: 20),
              Center(
                child: _image == null
                    ? Text('No image selected')
                    : Image.file(_image),
              ),
              SizedBox(height: 20),
              FutureBuilder<void>(
                future: _initializeControllerFuture,
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.done) {
                    // If the Future is complete, display the preview.
                    return CameraPreview(_controller);
                  } else {
                    // Otherwise, display a loading indicator.
                    return const Center(child: CircularProgressIndicator());
                  }
                },
              ),
              CircleAvatar(
                radius: 50,
                backgroundColor: Colors.white,
                backgroundImage: _backgroundImage,
              )
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        // Provide an onPressed callback.
        onPressed: () => startImageCaptureAndSend(),
        child: const Icon(Icons.camera_alt),
      ),
    );
  }

  void takeCameraPictures() async {
    // Take the Picture in a try / catch block. If anything goes wrong,
    // catch the error.
    try {
      // Ensure that the camera is initialized.
      await _initializeControllerFuture;

      // Attempt to take a picture and get the file `image`
      // where it was saved.
      final imageXfile = await _controller.takePicture();
      Directory appDocDirectory = await getApplicationDocumentsDirectory();
      final String imagesPath = appDocDirectory.path;
      final File savedImage =
          await File(imageXfile.path).copy('$imagesPath/$imageIndex.jpg');
      final fileImage = FileImage(savedImage);
      imageIndex++;
      int numImagesToUpload = await uploadImageToServer(fileImage);
    } catch (e) {
      // If an error occurs, log the error to the console.
      print('ERROR: $e');
    }
  }

  Future<void> startImageCaptureAndSend() async {
    FileImage newImage = await getCameraImage();
    int numImagesToUpload = await uploadImageToServer(newImage);

    for (int i = 0; i < numImagesToUpload; i++) {
      await uploadImageToServer(await getCameraImage());
    }
  }

  Future<FileImage> getCameraImage() async {
    try {
      // Ensure that the camera is initialized.
      await _initializeControllerFuture;
      // Attempt to take a picture and get the file `image` where it was saved.
      final imageXfile = await _controller.takePicture();
      Directory appDocDirectory = await getApplicationDocumentsDirectory();
      final String imagesPath = appDocDirectory.path;
      final File savedImage =
          await File(imageXfile.path).copy('$imagesPath/$imageIndex.jpg');
      // ? Is image index necessary?
      imageIndex++;
      final fileImage = FileImage(savedImage);
      return fileImage;
    } catch (e) {
      print('ERROR: $e');
      throw Exception('$e');
    }
  }

  //  Returns number of images left to be taken and uploaded
  Future<int> uploadImageToServer(FileImage image) async {
    var client = http.Client();
    try {
      String url = 'http://192.168.1.72:3000/upload';
      Uri uri = Uri.parse(url);
      Uri imageUri = Uri.parse(image.file.path);
      int numImagesToUpload = 0;

      var request = http.MultipartRequest("POST", uri);
      request.fields['name'] = 'imageName';
      request.files.add(
        await http.MultipartFile.fromBytes(
          'file',
          await File.fromUri(imageUri).readAsBytes(),
          filename: '.jpg',
          contentType: MediaType('image', 'jpg'),
        ),
      );
      await request.send().then((response) async {
        if (response.statusCode == 200) {
          print('Uploaded!');
          numImagesToUpload = int.parse(await response.stream.bytesToString());
        } else {
          print('ERROR!: ${response.statusCode}  ${response.stream.first}');
          return 'Error';
        }
      });
      return numImagesToUpload;
    } catch (e) {
      print('ERROR: $e');
      return (0);
    } finally {
      client.close();
    }
  }
}
