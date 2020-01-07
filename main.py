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

screen = pygame.display.set_mode(size)
pygame.display.set_caption("THE GAME")

### OBJECTS #########################################################################################

obj1 = cl.Entity(100, 100, "bola.png")
player1  = cl.Player(200, 200, "mickey.png", "Mickey")
player1.speak("hóhó")

obj1.resize_image(100, 100)
player1.resize_image(100, 100)

### MAIN LOOP ########################################################################################

end = False
direction = 'stop'
key_down = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        elif event.type == pygame.KEYDOWN:
            key_down = True
            keys = pygame.key.get_pressed()        
            if keys[pygame.K_UP]:
                direction = 'm_up'      
            elif keys[pygame.K_DOWN]:
                direction = 'm_down'
            elif keys[pygame.K_LEFT]:
                direction = 'm_left'
            elif keys[pygame.K_RIGHT]:
                direction = 'm_right'

            # if event.key == pygame.K_UP:
            #     direction = 'm_up'         
            # elif event.key == pygame.K_DOWN:
            #     direction = 'm_down'
            # elif event.key == pygame.K_LEFT:
            #     direction = 'm_left'
            # elif event.key == pygame.K_RIGHT:
            #     direction = 'm_right'
        elif event.type == pygame.KEYUP:
            key_down = False
            direction == 'stop'

    if key_down:
        if(direction == 'm_up'):
            player1.move(0,-5,screen)
        elif(direction == 'm_down'):
            player1.move(0,5,screen)
        elif(direction == 'm_left'):
            player1.move(-5,0,screen)
        elif(direction == 'm_right'):
            player1.move(5,0,screen)

    print(direction + ' ' + str(key_down))
        
    screen.blit(pygame.image.load("background.jpg"), (0,-80))
    obj1.show_image(screen)
    player1.show_image(screen)
    pygame.display.update()
    # pygame.display.flip()