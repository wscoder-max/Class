import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Sprites")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite((255, 0, 0), 50, 50)
sp2 = Sprite((0, 255, 0), 50, 50)
sp1.rect.x = 100
sp1.rect.y = 100
sp2.rect.x = 200
sp2.rect.y = 150
all_sprites_list.add(sp1)
all_sprites_list.add(sp2)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    all_sprites_list.update()
    screen.fill((255, 255, 255))
    all_sprites_list.draw(screen)
    
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        sp1.rect.x -= 1
    if pressed[pygame.K_RIGHT]:
        sp1.rect.x += 1
    if pressed[pygame.K_UP]:   
        sp1.rect.y -= 1
    if pressed[pygame.K_DOWN]:
        sp1.rect.y += 1

    pygame.display.flip()

pygame.quit()