from pico2d import *
import random


TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
Hand_arrow = load_image('hand_arrow.png')

running = True
x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

new_x = random.randint(1,TUK_WIDTH)
new_y = random.randint(1,TUK_HEIGHT)

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def random_hand():
    global new_x,new_y

    new_x = random.randint(1, TUK_WIDTH)
    new_y = random.randint(1, TUK_HEIGHT)

def draw_master():
    global frame
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    Hand_arrow.draw(new_x, new_y)  # 랜덤 위치 손
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x1, y1)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    handle_events()

def trace_cursor():
    global x1,y1,new_x,new_y,frame

    if new_x > x1 and new_y > y1:
        a = (new_y-y1)/(new_x-x1)
        b = y1 - x1 * a
        for x1 in range(x1,new_x+1,10):
            y1 = a * x1 + b
            draw_master()
        random_hand()
    elif new_x < x1 and new_y > y1:
        a = (new_y - y1) / (new_x - x1)
        b = y1 - x1 * a
        for x1 in range(x1, new_x + 1, -10):
            y1 = a * x1 + b
            draw_master()
        random_hand()
    elif new_x < x1 and new_y < y1:
        a = (new_y - y1) / (new_x - x1)
        b = y1 - x1 * a
        for x1 in range(x1, new_x + 1, -10):
            y1 = a * x1 + b
            draw_master()
        random_hand()
    elif new_x > x1 and new_y < y1:
        a = (new_y - y1) / (new_x - x1)
        b = y1 - x1 * a
        for x1 in range(x1, new_x + 1, 10):
            y1 = a * x1 + b
            draw_master()
        random_hand()

while running:

    trace_cursor()

close_canvas()




