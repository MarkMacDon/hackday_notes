from datetime import datetime
from matplotlib.colors import get_named_colors_mapping

import numpy as np

from datetime import datetime

import numpy as np

from tree_animator import TreeAnimator
from utils.color import hsv_to_rgb
import requests
import json

serverURL ='http://192.168.1.72:8080/'

class NewAnimation(TreeAnimator):
    def __init__(self, coords_path=None):
        self.a=0
        self._snakeCoords
        self._lightIndexes
        super().__init__(coords_path=coords_path)

    def initialize_animation(self):
        self.angle = 0

        self.color_A = (255,0,0) # red
        self.color_B = (0,255,0) # green

    def _get_snake_coords_from_http(self):
        r = requests.get(serverURL)
    
        if r.encoding is None:
            r.encoding = 'utf-8'

        data = []
        for line in r.iter_lines(decode_unicode=True):
            if line:
                data = json.loads(line)
                print(data.get('Coords'))   
                self._snakeCoords = data.get('Coords')

    def calculate_colors(self, xyz_coords, start_time):

        self._get_snake_coords_from_http()

        colors = np.zeros((self.NUM_LIGHTS, 3), dtype=np.uint8)
        for i in range(self.NUM_LIGHTS):
            if self.a % 2 == 0:
                colors[i] = self.color_A
            else:
                colors[i] = self.color_B
        
        


            # capture lights data ((index, r,g,b) * 500lights) in object
            # Inject that into lights display script

        self.color_A = hsv_to_rgb(1,1,1)
        self.color_b = hsv_to_rgb(2,2,2)
        self.a +=1

            
        return colors

    def snake_coords_to_light_index(snakeCoords):  # => list[lightIndexes]
            
            # Which snake coord corresponds to which light index
            # coords max, min for x, y,
            # width is (max - min) / 20 = box width
            # Width for each horizontal band
            grid = []
            assert: grid maxHeight / yRange = number of pixels in snake game  
                    grid maxWidth / xRange = snakeGame width

            while yRange < yMax:
                for coord in coordinates:
                    newRow =[]
                    if coord['y'] <= yRange:
                        newRow.append[coord]
                grid.append(newRow)
                yRange += yRange
            
            finalGrid = []
            for row in grid:
                newRow =[]
                for coord in row:
                    if coord['x'] <= xRange:
                        newRow.append(coord)
                finalGrid.append(newRow)
                xRange.append(newRow)
            
            

            
             self._light_indexes = lightIndexes # List[lightIndex]

if __name__ == "__main__":
    anim = NewAnimation()

    anim.animation_loop()
