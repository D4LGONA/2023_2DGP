from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        #self.image.clip_draw_to_origin(server.background.window_left, server.background.window_bottom, server.background.cw, server.background.ch, 0, 0)
        self.image.draw(self.x - server.background.window_left, self.y - server.background.window_bottom)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - server.background.window_left - 10, self.y - server.background.window_bottom - 10, self.x - server.background.window_left + 10, self.y - server.background.window_bottom + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)
                pass
            case 'zombie:ball':
                other.ball = self