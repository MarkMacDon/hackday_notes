import json
import requests
import time

# Can be faster than framerate
framerateInSeconds = 0.001 

while True:
    r = requests.get('http://192.168.1.72:8080/')
    
    if r.encoding is None:
        r.encoding = 'utf-8'
    
    for line in r.iter_lines(decode_unicode=True):
        if line:
            print(json.loads(line))

            # capture lights data ((index, r,g,b) * 500lights) in object
            # Inject that into lights display script
    
    time.sleep(framerateInSeconds)

    