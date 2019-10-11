#!/usr/bin/env python3

import pygame
pygame.init()

(window_width, window_height) = (500, 500)
win = pygame.display.set_mode((window_width, window_height))

char1_x = 50
char1_y = 250
char1_width = 40
char1_height = 60
vel = 5

isJump = False
jumpCount = 10

pygame.display.set_caption("Jumper")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and char1_x > 0:
        char1_x -= vel

    if keys[pygame.K_RIGHT] and char1_x < window_width - char1_width:
        char1_x += vel

    if not(isJump):
        if keys[pygame.K_UP] and char1_y > 0:
            char1_y -= vel

        if keys[pygame.K_DOWN] and char1_y < window_height - char1_height:
            char1_y += vel

        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            char1_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 0, 0), (char1_x, char1_y, char1_width, char1_height))
    pygame.display.update()  # or we could say: pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
