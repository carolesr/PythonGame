import pygame

class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = self.load_image(image)

    def load_image(self, image):
        try:
            img = pygame.image.load(image)
        except:
            print("Error loading " + image)
            raise SystemExit
        return img

    def show_image(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def resize_image(self, w, h):
        try:
            self.image = pygame.transform.scale(self.image, (w, h))
        except:
            print("Error resizing image")
    
    def move(self, dx, dy,screen):
        self.x += dx
        self.y += dy
        self.show_image(screen)

class Player(Entity):
    def __init__(self, x, y, image, jumping, hit_ground, speed):
        self.jumping = jumping
        self.hit_ground = hit_ground
        self.speed = speed
        self.last_plat = 0
        self.count_plat = 0
        super().__init__(x, y, image)


class Platform(Entity):
    def __init__(self, x, y, image, speed, width, height):
        self.speed = speed
        self.width = width
        self.height = height
        super().__init__(x, y, image)
        self.resize_image(width, height)