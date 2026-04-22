import pygame
pygame.init()

pygame.display.set_mode((500, 500))
pygame.display.set_caption("My first Game Screen")

screen = pygame.display.get_surface()
my_image = pygame.image.load("my_image.png")

image_rect = my_image.get_rect()
image_rect.topleft = (100, 50) 

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((58, 58, 58)) 
        screen.blit(my_image, image_rect) 

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
