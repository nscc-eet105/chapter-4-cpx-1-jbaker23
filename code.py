#My name is Jacob Baker and this is Chapter 4 CPX 1 which i am completing on June 24

from adafruit_circuitplayground import cp
def all_lights():
    while True:
        if cp.touch_A2:
            for i in range(10):
                cp.pixels[i] = (255, 0, 255)
        else:
            for i in range(10):
                cp.pixels[i] = (0, 0, 0)


all_lights()
