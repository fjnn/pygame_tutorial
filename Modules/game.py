#!/usr/bin/env python3

import pygame
from my_player_module import my_player

pygame.init()

(window_width, window_height) = (800, 600)
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Two Player")
backgroud = pygame.image.load('../Animation_Sprites/forrest2.png')
clock = pygame.time.Clock()


def updateWindow():
    win.blit(backgroud, (0, 0))
    greenDragon.draw_char(win)
    redDragon.draw_char(win)
    pygame.display.update()


greenDragon = my_player(50, 450, 39, 72)
redDragon = my_player(70, 450, 39, 72)
greenDragon.appearance('../Animation_Sprites/Monstro/WALK/RIGHT/skeleton-resizedWALK_', '../Animation_Sprites/Monstro/WALK/LEFT/skeleton-resizedWALK_', '../Animation_Sprites/Monstro/IDLE/skeleton-resizedIDLE_')
redDragon.appearance('../Animation_Sprites/Monstro/WALK/RIGHT/skeleton-coloredWALK_', '../Animation_Sprites/Monstro/WALK/LEFT/skeleton-coloredWALK_', '../Animation_Sprites/Monstro/IDLE/skeleton-coloredIDLE_')
running = True
while running:
    updateWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and greenDragon.x > 0:
        greenDragon.x -= greenDragon.vel
        greenDragon.left = True
        greenDragon.right = False

    elif keys[pygame.K_RIGHT] and greenDragon.x < window_width - greenDragon.width:
        greenDragon.x += greenDragon.vel
        greenDragon.left = False
        greenDragon.right = True

    if keys[pygame.K_a] and redDragon.x > 0:
        redDragon.x -= redDragon.vel
        redDragon.left = True
        redDragon.right = False

    elif keys[pygame.K_s] and redDragon.x < window_width - redDragon.width:
        redDragon.x += redDragon.vel
        redDragon.left = False
        redDragon.right = True

    else:
        greenDragon.left = False
        greenDragon.right = False
        redDragon.left = False
        redDragon.right = False

    if not(greenDragon.isJump):
        if keys[pygame.K_SPACE]:
            greenDragon.isJump = True
            greenDragon.left = False
            greenDragon.right = False
            greenDragon.walk_count = 0
    else:
        if greenDragon.jumpCount >= -10:
            greenDragon.y -= (greenDragon.jumpCount * abs(greenDragon.jumpCount)) * 0.5
            greenDragon.jumpCount -= 1
        else:
            greenDragon.jumpCount = 10
            greenDragon.isJump = False

    if not(redDragon.isJump):
        if keys[pygame.K_h]:
            redDragon.isJump = True
            redDragon.left = False
            redDragon.right = False
            redDragon.walk_count = 0
    else:
        if redDragon.jumpCount >= -10:
            redDragon.y -= (redDragon.jumpCount * abs(redDragon.jumpCount)) * 0.5
            redDragon.jumpCount -= 1
        else:
            redDragon.jumpCount = 10
            redDragon.isJump = False
    clock.tick(36)

pygame.quit()
