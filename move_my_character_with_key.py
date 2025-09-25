from pico2d import *

open_canvas(800,600)

background = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

def handle_events():
    global state

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            exit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                state = "Rrun"
            elif event.key == SDLK_LEFT:
                state = "Lrun"
            elif event.key == SDLK_UP:
                if state in ("Ridle", "Rrun"):
                    state = "Rup"
                elif state in ("Lidle","Lrun"):
                    state = "Lup"
            elif event.key == SDLK_DOWN:
                if state in ("Ridle", "Rrun"):
                    state = "Rdown"
                elif state in ("Lidle","Lrun"):
                    state = "Ldown"
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                state = "Ridle"
            elif event.key == SDLK_LEFT:
                state = "Lidle"
            elif event.key == SDLK_UP or event.key == SDLK_DOWN:
                if state in ("Ridle","Rrun","Rup","Rdown"):
                    state = "Ridle"
                if state in ("Lidle","Lrun","Lup","Ldown"):
                    state = "Lidle"

def move_character():
    global x,y

    if state == "Rrun":
        x += 5
        if x > 800:
            x = 800
    elif state == "Lrun":
        x -= 5
        if x < 0:
            x = 0
    elif state == "Rup" or state == "Lup":
        y += 5
        if y > 600:
            y = 600
    elif state == "Rdown" or state == "Ldown":
        y -= 5
        if y < 0:
            y = 0

x = 400
y = 300
frame = 0
state = "Ridle"

while True:
    clear_canvas()
    background.clip_draw(0,0,1280,1024,400,300,800,600)
    if state == "Ridle":
        character.clip_draw(frame * 100, 300, 100, 100, x, y)
    elif state == "Lidle":
        character.clip_draw(frame * 100, 200, 100, 100, x, y)
    elif state == "Rrun"or state == "Rup" or state == "Rdown":
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif state == "Lrun" or state == "Lup" or state == "Ldown":
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    move_character()
    frame = (frame + 1) % 8
    delay(0.05)
    pass

close_canvas()