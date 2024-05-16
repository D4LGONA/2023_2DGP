from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.1)

def run_circle():       # pass 일단 써놓기
    print('circle')
    
    cx, cy, r = 800 / 2, 600 / 2, 200 # 이런 식의 표현이 좋음
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        render_all(x, y)
        

def run_rectangle():
    print('rectangle')

    # bottom line
    for x in range(50, 750 + 1, 10):
        render_all(x, 90)
    
    # right line
    for y in range(90, 550 + 1, 10):
        render_all(750, y)

    # top line
    for x in range(750, 50 - 1, -10): # 문법적인 기능을 확인하기 위해서 IDLE에서 확인함.
        render_all(x, 550)

    # left line
    for y in range(550, 90 - 1, -10):
        render_all(50, y)

while True:
    run_circle()        # 함수를 먼저 만들고 내용을 만들 것
    run_rectangle()     # 테스트하기 쉽게 하려고 함수를 따로 뺌 주석처리 하고 테스트할 것
    #break              # break를 써서 우선 제대로 되는지 확인


close_canvas()
