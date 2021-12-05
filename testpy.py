### Here is a basic script that will retrieve data from a url and add it to a process stream
### For the snake game I think you will only need to retrieve data (directions)
### I dont think you will need to add data to the process stream or to POST requests

import json
import sys
import time
import requests

url = 'http://localhost:8080/'
# Get response from GET request
# res = requests.get(url)
# print(f'Here is the response content: {res.content}')

# # This sends the data out to the system so it can be added to the process stream
# # The node server will be listening to the stream and will recieve the printed data
# sys.stdout.flush()

# # Sleep function added to demonstrate the asyncronous functionality of streams
# time.sleep(2)

### Making a POST request ###

# Define the body content type in the header
headers = {'Content-type': 'application/json'}
# Format the body as defined in header (json)
body = json.dumps({
  "coords": [678]

})
# Make the POST request
postRes = requests.post(url, headers=headers, json=body)
print(postRes.json())
sys.stdout.flush()


# # Again, this is how you add the data to the spawn process stream
# print(f'Post Response {postRes.content}')
# sys.stdout.flush()

# # example: adding object to process stream
# class TestObject:
#     def __init__(self, name):  
#         self.name = name

#     # I assume that sending objects in a shared format, such as Map or Json, is preferrable
#     def asMap(self):
#         return {'name':self.name}
# testObject = TestObject('New Test Object')
# # This may print it as a string. Be sure to type check on the server
# print(testObject.asMap())
# sys.stdout.flush()


# ### *** FOR YOUR SNAKE GAME *** (Pseudocode since my python isn't so good...)
# # At every refresh:
# #   response = requests.get(url)
# #   ** res.content is a bytes string so you may have to reformat
# #   direction = res.content['direction']
# #   if (direction == 'left'):
# #       <handle left>
