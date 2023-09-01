print("hello")
import pygame
import keyboard
import time


pygame.init()
window = pygame.display.set_mode((800,600))
running = True

player_x = 0
player_y = 0
speed = 1

move_up = False
move_left = False
move_down = False
move_right = False

def player_movement(event):
    global player_y
    global player_x
    global move_up
    global move_down
    global move_left
    global move_right

    move_up = False
    move_left = False
    move_down = False
    move_right = False

    if event.name == 'w':
        # player_y -= 1
        move_up = True


    elif event.name == 'a':
        # player_x -= 1
        move_left = True
    elif event.name == 's':
        # player_y += 1
        move_down = True
    elif event.name == 'd':
        # player_x += 1
        move_right = True

keyboard.on_press(player_movement)

FPS = 60

last_time = time.time()

while running:

    # FPS limiter
    current_time = time.time()
    dt = current_time - last_time
    last_time = current_time

    sleep_time = 1.0/FPS - (current_time - last_time)
    if sleep_time > 0:
        time.sleep(sleep_time)

    pygame.event.pump() 
    keys = pygame.key.get_pressed() 

    # logic
    # if keyboard.is_pressed('w'):
    #     player_y -= 1
    # if keyboard.is_pressed('a'):
    #     player_x -= 1
    # if keyboard.is_pressed('s'):
    #     player_y += 1
    # if keyboard.is_pressed('d'):
    #     player_x += 1

    if move_up:
        player_y -= 1
    if move_left:
        player_x -= 1
    if move_down:
        player_y += 1
    if move_right:
        player_x += 1



    if keyboard.is_pressed('esc'):
        running = False


    # render
    black = 0, 0, 0
    window.fill(black)

    green = 0,255,0
    player_rect = player_x, player_y, 50, 50

    pygame.draw.rect(window, green, player_rect,0 )
    pygame.display.flip()

    # time.sleep (100.0 / 1000.0);

pygame.quit()

x = 1
while True:
    x += 1
    print(x)
import pygame
exec(open("C:\test.py").read())