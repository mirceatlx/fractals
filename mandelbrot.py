from PIL import Image
from numpy import complex, array
import colorsys

width = 1024


def rgb_convers(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int)) 

def mandelbrot(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 1000):
        if(abs(c) > 2): # preventing divergence
            return rgb_convers(i)
        
        c = c * c + c0 # mandelbrot set equation
    return (0, 0, 0)

img = Image.new('RGB', (width, int(width / 2)))
pixels = img.load()

for x in range(img.size[0]):

    for y in range(img.size[1]):
        pixels[x, y] = mandelbrot((x - (0.75 * width)) / (width / 4), (y - (width / 4)) / (width / 4))

img.show()
