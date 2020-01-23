# import "\users\carol\appdata\local\programs\python\python37\lib\site-packages\pygame"
import sys
import time
import pygame
import classes as cl
import random
import math

### DEFINES ##########################################################################################

screen_width = 640
screen_heigth = 640
size = (screen_width, screen_heigth)
random.seed()

keys = {'up': False, 'down': False, 'left': False, 'right': False}

ground = 550
speed = 20
screen_speed = 1

platforms = []
min_width = 150
max_width = 200
space_between = 170
time_count = 180
rand_step = 30

# fases = []
# fases.append({'speed':1,'time':180})
# fases.append({'speed':2,'time':90})
# fases.append({'speed':4,'time':45})
# fases.append({'speed':8,'time':23})
fases = [{'speed': math.pow(2, i), 'time': 200 / math.pow(2, i)} for i in range(4)]

### PYGAME INIT ######################################################################################

if(pygame.init()[1] > 0):
    print("Error pygame.init")
    sys.exit(-1)
else:
    print("pygame.init: success")

screen = pygame.display.set_mode(size)
pygame.display.set_caption("THE GAME")
font = pygame.font.Font('freesansbold.ttf', 32) 


### OBJECTS #########################################################################################

y = 150
x = 0
for i in range(3):
    w = random.randrange(min_width,max_width,rand_step)
    x = random.randrange(x-300,x+300,rand_step)
    if x < 0:
        x = 0
    if x > screen_width-w:
        x = screen_width-w
    platforms.append(cl.Platform(x, y, "platform.png", 0, w, 25))
    y += space_between

player1 = cl.Player(x, y-30, "bola.png", False, False, -1*speed)
player1.resize_image(60, 60)
player1.count_plat = 3
player1.last_plat = x

### FUNCTIONS ########################################################################################


def get_pressed_keys(event, end):
    if event.type == pygame.QUIT:
        end = True
    elif event.type == pygame.KEYDOWN:
        pressed = pygame.key.get_pressed()
        # if pressed[pygame.K_UP]:
        #     pressed_jump()
        # if pressed[pygame.K_DOWN]:
        #     keys['down'] =  True
        if pressed[pygame.K_LEFT]:
            keys['left'] = True
        if pressed[pygame.K_RIGHT]:
            keys['right'] = True

    elif event.type == pygame.KEYUP:
        pressed = pygame.key.get_pressed()
        # if not pressed[pygame.K_UP]:
        #     keys['up'] = False
        # if not pressed[pygame.K_DOWN]:
        #     keys['down'] =  False
        if not pressed[pygame.K_LEFT]:
            keys['left'] = False
        if not pressed[pygame.K_RIGHT]:
            keys['right'] = False
    return end


def pressed_jump():
    player1.jumping = True
    player1.hit_ground = False
    player1.speed = -1*speed


def jump():
    player1.speed += 1
    if player1.speed >= 0:
        if player1.hit_ground:
            player1.jumping = False
            player1.speed = -1*speed

    player1.move(0, player1.speed, screen)


def check_colision(plat, game_over):
    if player1.y >= screen_heigth:
        game_over = True
    else:
        if (plat.x-25 <= player1.x <= plat.x-25 + plat.width) and (plat.y <= player1.y <= plat.y + plat.height):
            player1.hit_ground = True
        else:
            player1.hit_ground = False

    if player1.hit_ground:
        pressed_jump()
        jump()

    return game_over

def get_rand_plat():
    # x = random.randrange(0,screen_width-max_width,rand_step)
    x = random.randrange(player1.x-250,player1.x+250,rand_step)
    w = random.randrange(min_width,max_width,rand_step)
    if x < 0:
        x = 0
    if x > screen_width-w:
        x = screen_width-w
    player1.last_plat = x
    player1.count_plat += 1
    return (x,w)

def add_plat():
    a = get_rand_plat()
    x = a[0]
    w = a[1]
    platforms.append(cl.Platform(x, 150, "platform.png", 0, w, 25))
    
### MAIN LOOP ########################################################################################


end = False
game_over = False
count = 0
player1.jumping = True
while not end:
    for event in pygame.event.get():
        end = get_pressed_keys(event, end)

    if player1.jumping:
        jump()
    if keys['left']:
        player1.move(-5, 0, screen)
    if keys['right']:
        player1.move(5, 0, screen)

    for plat in platforms:
        game_over = check_colision(plat,game_over)

    for plat in platforms:
        plat.move(0,screen_speed,screen)
        if plat.y > screen_heigth:
            platforms.remove(plat)
    count += 1

    if not game_over:
        if count == time_count:
            count = 0
            add_plat()

    if player1.count_plat == 5:
        screen_speed = fases[1]['speed']
        time_count = fases[1]['time']
    elif player1.count_plat == 15:
        screen_speed = fases[2]['speed']
        time_count = fases[2]['time']
    elif player1.count_plat == 30:
        screen_speed = fases[3]['speed']
        time_count = fases[3]['time']

    screen.blit(pygame.image.load("background.jpg"), (0, 0))
    if not game_over:
        player1.show_image(screen)
        for plat in platforms:
            plat.show_image(screen)
    else:
        text1 = font.render('GAME OVER', True, (255,255,255),(0,0,0))
        textRect1 = text1.get_rect()
        textRect1.center = (screen_width // 2, screen_heigth // 2 - 150)

        text2 = font.render('SCORE: ' + str(player1.count_plat), True, (255,255,255),(0,0,0))
        textRect2 = text2.get_rect()
        textRect2.center = (screen_width // 2, screen_heigth // 2 - 100)

        screen.blit(text1,textRect1)
        screen.blit(text2,textRect2)
    pygame.display.update()
