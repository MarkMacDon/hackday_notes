import shutil
import time
import sys
# import board
# import neopixel
# import requests
# import json

# pixel_pin = board.D18
# ORDER = neopixel.RGB
# serverUrl = 'http://localhost:3000/uploads'
num_pixels = 500
# pixels = neopixel.NeoPixel(
#     pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
# )

lightIndex = sys.argv[1]

def turn_on_one_light(i):
    # pixels.fill((0,0,0))
    # pixels[num] = (255,255,255)
    # pixels.show()
     # Make the POST request
    i = int(i)
    print(f'Turned on light {i+1}')
    
if __name__ == "__main__":
    print('in main')
    turn_on_one_light(lightIndex)
    sys.stdout.flush()


# def get_number_of_lights():
#     print(num_pixels)
#     sys.stdout.flush()

# print('RUN')
# sys.stdout.flush()