import pygame
pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Game Screen")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, pygame.Rect(200, 150, 100, 50))
    font = pygame.font.SysFont("Times New Roman", 36)
    text = font.render("Hello, World!", True, BLACK)
    screen.blit(text, (200, 250))
    pygame.display.flip()

pygame.quit()