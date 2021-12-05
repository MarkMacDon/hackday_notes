import requests
import json
import sys
import time

PORT=8080
url = f'http://localhost:{PORT}/'

headers = {'Content-type': 'application/json'}
body = {
  "coordinates": "(coordinates, go, here)"

}



postRes = requests.post(url, headers=headers, json=body)

print('FLUSHED')
sys.stdout.flush()

if __name__ == "__main__":
    print('in main')
    sys.stdout.flush()
