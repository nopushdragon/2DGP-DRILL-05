from pico2d import *

open_canvas(800,600)
background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


while True:
    clear_canvas()
    background.clip_draw(0,0,1280,1024,400,300,800,600)
    update_canvas()
    delay(0.05)
    pass

close_canvas()