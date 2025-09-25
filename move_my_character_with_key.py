from pico2d import *

open_canvas(800,600)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    pass

x = 400
y = 300
frame = 0


while True:
    clear_canvas()
    background.clip_draw(0,0,1280,1024,400,300,800,600)
    #캐릭터 그리기
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)
    pass

close_canvas()