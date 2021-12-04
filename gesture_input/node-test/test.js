const http = require('http');

const server = http.createServer((req, res)=>{

   // log the request data
   console.log(req.url, req.method, req. headers);

   // set header content type
   res.setHeader('Content-Type', 'text/html')
   // populate the response object
   res.write('<html>');
   res.write('<head> <title> Hello TutorialsPoint </title> </head>');
   res.write(' <body> Hello Tutorials Point </body>');
   res.write('</html>');
   //write end to mark it as stop for node js response.
   res.end();
});
server.listen(3001, 'localhost', () => {
   console.log('listening for requests on port 3000');
}, );