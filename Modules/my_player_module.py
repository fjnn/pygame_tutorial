#!/usr/bin/env python3

import pygame


class my_player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = []
        self.walkLeft = []
        self.idle = []

    def appearance(self, walk_right_images, walk_left_images, idle_images):
        for i in range(18):
            image_name = walk_right_images + str(i) + '.png'
            image = pygame.image.load(image_name)
            self.walkRight.append(image)

        for i in range(18):
            image_name = walk_left_images + str(i) + '.png'
            image = pygame.image.load(image_name)
            self.walkLeft.append(image)

        for i in range(18):
            image_name = idle_images + str(i) + '.png'
            image = pygame.image.load(image_name)
            self.idle.append(image)

    def draw_char(self, win):
        if self.walkCount + 1 >= 36:
            self.walkCount = 0
        if self.right:
            win.blit(self.walkRight[self.walkCount//2], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            win.blit(self.walkLeft[self.walkCount//2], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.idle[self.walkCount//2], (self.x, self.y))
            self.walkCount += 1
