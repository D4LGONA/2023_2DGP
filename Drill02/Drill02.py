from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
degree = 270
state = 0
dir = 'right'
count = 0

while True:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if(state == 0):
        if (dir == 'right'):
            x += 1
            if (x >= 800 - 20):
                dir = 'up'
        elif (dir == 'up'):
            y += 1
            if (y >= 560):
                dir = 'left'
        elif (dir == 'left'):
            x -= 1
            if(x <= 20):
                dir = 'down'
        elif (dir == 'down'):
            y -= 1
            if(y <= 90):
                dir = 'right'
        if (x == 400 and y == 90):
            state = 1
    else:
        count += 1
        degree += 1
        x = 210 * math.cos(degree / 360 * 2 * math.pi) + 400
        y = 210 * math.sin(degree / 360 * 2 * math.pi) + 300
        if(count == 360):
            count = 0
            state = 0
    delay(0.001)
        
    

close_canvas()
