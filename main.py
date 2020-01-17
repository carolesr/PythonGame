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

ground = 400
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

player1 = cl.Player(200, 400, "bola.png", False, False, -1*speed)

player1.resize_image(100, 100)

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
    
    print(player1.speed)
    player1.move(0,player1.speed,screen)

### MAIN LOOP ########################################################################################

end = False
while not end:
    for event in pygame.event.get():
        end = get_pressed_keys(event, end)
        
    if player1.jumping:
        jump()

    # if keys['up']:
    #     #jump()
    #     # player1.move(0,-5,screen)
    # if keys['down'] and not player1.hit_ground:
    #     player1.move(0,5,screen)
    if keys['left']:
        player1.move(-5,0,screen)
    if keys['right']:
        player1.move(5,0,screen)

    if player1.y == ground:
        player1.hit_ground = True
        pressed_jump()
        jump()
    else:
        player1.hit_ground = False
        
    screen.blit(pygame.image.load("background2.jpg"), (0,-80))
    player1.show_image(screen)
    pygame.display.update()
    # pygame.display.flip()