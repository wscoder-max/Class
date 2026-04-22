import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Color changing sprite')

    colors = {
        'Red': pygame.Color('red'),
        'Green': pygame.Color('green'),
        'Blue': pygame.Color('blue'),
        'Yellow': pygame.Color('yellow'),
        'White': pygame.Color('white')
    }
    current_color = colors['White']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)

        if x == 0: current_color = colors['Blue']
        elif x == screen_width - sprite_width: current_color = colors['Yellow']
        elif y == 0: current_color = colors['Red']
        elif y == screen_height - sprite_height:
            current_color = colors['Green']
        else:
            current_color = colors['White']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


if __name__ == "__main__":
    main()
