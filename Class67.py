import pygame
import random
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Colour Changing Sprite")

class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (255, 0, 0)
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (250, 200)
    def change_color(self):
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_color)

sp1 = Sprite()
all_sprites = pygame.sprite.Group()
all_sprites.add(sp1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                sp1.change_color()

    screen.fill((255, 255, 255))  
    all_sprites.draw(screen)  
    
    pygame.display.flip()  

pygame.quit()