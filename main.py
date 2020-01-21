# import "\users\carol\appdata\local\programs\python\python37\lib\site-packages\pygame"
import sys
import time
import pygame
import classes as cl

### DEFINES ##########################################################################################

screen_width = 800
screen_heigth = 600
size = (screen_width, screen_heigth)

keys = { 'up':False, 'down':False, 'left':False, 'right':False}

ground = 450
speed = 20
gravity = 0.5

# jumping_speed = -1*speed
# jumping = False
# hit_ground = False

### PYGAME INIT ######################################################################################

if(pygame.init()[1] > 0):
   print("Error pygame.init")
   sys.exit(-1)
else:
    print("pygame.init: success")

screen = pygame.display.set_mode(size)
pygame.display.set_caption("THE GAME")

### OBJECTS #########################################################################################

player1 = cl.Player(200, ground, "bola.png", False, False, -1*speed)
player1.resize_image(60, 60)

platform1 = cl.Platform(330, 330, "platform.png", 0, 150, 30)
# platform1.resize_image(150,30)

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
    
    player1.move(0,player1.speed,screen)

def check_colision():
    # print(player1.y)
    if ground-speed <= player1.y <= ground+speed:
        player1.hit_ground = True
    elif platform1.x <= player1.x <= platform1.x + platform1.width:
        if platform1.y <= player1.y <= platform1.y + platform1.height:
            player1.hit_ground = True
        else:
            platform1.hit_ground = False
    else:
        player1.hit_ground = False

    if player1.hit_ground:
        pressed_jump()
        jump()

### MAIN LOOP ########################################################################################

end = False
while not end:
    for event in pygame.event.get():
        end = get_pressed_keys(event, end)
        
    if player1.jumping:
        jump()
    if keys['left']:
        player1.move(-5,0,screen)
    if keys['right']:
        player1.move(5,0,screen)

    check_colision()
        
    screen.blit(pygame.image.load("background2.jpg"), (0,-80))
    player1.show_image(screen)
    platform1.show_image(screen)
    pygame.display.update()