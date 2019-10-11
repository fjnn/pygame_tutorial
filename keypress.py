#!/usr/bin/env python3

# first
import pygame
pygame.init()

# (window_width, window_height) = (1920, 1440)
(window_width, window_height) = (500, 500)


char1_x = 50
char1_y = 50
char1_width = 40
char1_height = 60
vel = 10
win = pygame.display.set_mode((window_width, window_height))

# backgroud = pygame.image.load('forrest2_scaled.png')


# second
pygame.display.set_caption("Hello World")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fourth
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        char1_x -= vel

    if keys[pygame.K_RIGHT]:
        char1_x += vel

    if keys[pygame.K_UP]:
        char1_y -= vel

    if keys[pygame.K_DOWN]:
        char1_y += vel
    # fifth
    # win.blit(backgroud, (0, 0))
    win.fill((0, 0, 0))

# third
    pygame.draw.rect(win, (255, 0, 0), (char1_x, char1_y, char1_width, char1_height))
    pygame.display.update()  # or we could say: pygame.display.flip()
    pygame.time.delay(50)
# second
pygame.quit()
