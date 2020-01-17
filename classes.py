import pygame

class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = self.load_image(image)#[0]
        #self.surface = self.load_image(image)[1]

    def load_image(self, image):
        try:
            img = pygame.image.load(image)
        except:
            print("Error loading " + image)
            raise SystemExit
        return img #, img.get_rect()

    def show_image(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def resize_image(self, w, h):
        try:
            self.image = pygame.transform.scale(self.image, (w, h))
        except:
            print("Error resizing image")

class Player(Entity):
    def __init__(self, x, y, image, jumping, hit_ground, speed):
        self.jumping = jumping
        self.hit_ground = hit_ground
        self.speed = speed
        super().__init__(x, y, image)

    def move(self, dx, dy,screen):
        self.x += dx
        self.y += dy
        self.show_image(screen)