import random
import json
import os

from pico2d import *
import game_framework
import game_world

import server
from boy import Boy
from ball import Ball
import collision

# fill here
from background import FixedBackground as Background
#from background import TileBackground as Background


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            server.boy.handle_event(event)



def init():
    global balls
    # fill here
    server.background = Background()
    game_world.add_object(server.background, 0)

    server.boy = Boy()
    game_world.add_object(server.boy, 2)
    server.boy.set_background(server.background)

    balls = [Ball(random.randint(0 + 50, server.background.w - 50), random.randint(0 + 50, server.background.h - 50)) for _ in range(100)]
    game_world.add_objects(balls, 1)

    game_world.add_collision_pair('boy:ball', server.boy, None)
    for o in balls:
        game_world.add_collision_pair('boy:ball', None, o)

    pass

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass