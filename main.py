# import "\users\carol\appdata\local\programs\python\python37\lib\site-packages\pygame"
import sys
import time
import pygame
import classes as cl

### PYGAME INIT ######################################################################################

if(pygame.init()[1] > 0):
   print("Error pygame.init")
   sys.exit(-1)
else:
    print("pygame.init: success")

screen_width = 800
screen_heigth = 600
size = (screen_width, screen_heigth)
keys = { 'up':False, 'down':False, 'left':False, 'right':False}
ground = 400

screen = pygame.display.set_mode(size)
pygame.display.set_caption("THE GAME")

### OBJECTS #########################################################################################

player1 = cl.Player(200, 200, "mickey.png", "Mickey")
player1.speak("hóhó")

player1.resize_image(100, 100)

### FUNCTIONS ########################################################################################

def get_pressed_keys(event, end):
        if event.type == pygame.QUIT:
            end = True
        elif event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()        
            if pressed[pygame.K_UP]:
                keys['up'] = True        
            if pressed[pygame.K_DOWN]:
                keys['down'] =  True
            if pressed[pygame.K_LEFT]:
                keys['left'] = True
            if pressed[pygame.K_RIGHT]:
                keys['right'] = True

        elif event.type == pygame.KEYUP:
            pressed = pygame.key.get_pressed()        
            if not pressed[pygame.K_UP]:
                keys['up'] = False        
            if not pressed[pygame.K_DOWN]:
                keys['down'] =  False
            if not pressed[pygame.K_LEFT]:
                keys['left'] = False
            if not pressed[pygame.K_RIGHT]:
                keys['right'] = False
        return end

### MAIN LOOP ########################################################################################

end = False
hit_ground = False
while not end:
    for event in pygame.event.get():
        end = get_pressed_keys(event, end)
        
    if keys['up']:
        player1.move(0,-5,screen)
    if keys['down'] and not hit_ground:
        player1.move(0,5,screen)
    if keys['left']:
        player1.move(-5,0,screen)
    if keys['right']:
        player1.move(5,0,screen)

    if player1.y >= ground:
        hit_ground = True
    else:
        hit_ground = False
        
    screen.blit(pygame.image.load("background2.jpg"), (0,-80))
    player1.show_image(screen)
    pygame.display.update()
    # pygame.display.flip()