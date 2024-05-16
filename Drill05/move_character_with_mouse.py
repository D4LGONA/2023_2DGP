from pico2d import *
from random import *
from math import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def move():
    global x, y, h_x, h_y
    x1, y1 = x, y
    x2, y2 = h_x, h_y

    distance = sqrt((x1-x2) ** 2 + (y1-y2) **2)

    for i in range(0, int(distance) + 1, 1):
        t = i / int(distance)
        x = (1-t) * x1 + t * x2 
        y = (1-t) * y1 + t * y2 
        draw()

def draw():
    global frame, h_x, h_y, x, y
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    cursor.draw(h_x, h_y)
    if h_x > x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    update_canvas()       
    frame = (frame + 1) % 8 

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
h_x, h_y = randint(0, 1280), randint(0, 1024)
frame = 0
hide_cursor()

while running:
    move()
    h_x, h_y = randint(0, 1280), randint(0, 1024)
    handle_events()

close_canvas()




