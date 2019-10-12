#!/usr/bin/env python3


class my_player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.char1_isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0



(window_width, window_height) = (800, 600)
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jumper")

clock = pygame.time.Clock()


char1_walkRight = []
for i in range(18):
    image_name = 'Monstro/WALK/RIGHT/' + 'skeleton-resizedWALK_' + str(i) + '.png'
    image = pygame.image.load(image_name)
    char1_walkRight.append(image)

char1_walkLeft = []
for i in range(18):
    image_name = 'Monstro/WALK/LEFT/' + 'skeleton-resizedWALK_' + str(i) + '.png'
    image = pygame.image.load(image_name)
    char1_walkLeft.append(image)

char1_idle = []
for i in range(18):
    image_name = 'Monstro/IDLE/' + 'skeleton-resizedIDLE_' + str(i) + '.png'
    image = pygame.image.load(image_name)
    char1_idle.append(image)

backgroud = pygame.image.load('forrest2.png')


def updateWindow():
    global char1_walk_count
    print(char1_walk_count)
    win.blit(backgroud, (0, 0))
    # pygame.draw.rect(win, (255, 0, 0), (char1_x, char1_y, char1_width, char1_height))
    if char1_walk_count + 1 >= 36:
        char1_walk_count = 0
    if char1_right:
        win.blit(char1_walkRight[char1_walk_count//2], (char1_x, char1_y))
        char1_walk_count += 1
    elif char1_left:
        win.blit(char1_walkLeft[char1_walk_count//2], (char1_x, char1_y))
        char1_walk_count += 1
    else:
        print("here")
        win.blit(char1_idle[char1_walk_count//2], (char1_x, char1_y))
        char1_walk_count += 1
    pygame.display.update()


running = True
while running:
    updateWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and char1_x > 0:
        char1_x -= vel
        char1_left = True
        char1_right = False

    elif keys[pygame.K_RIGHT] and char1_x < window_width - char1_width:
        char1_x += vel
        char1_left = False
        char1_right = True

    else:
        char1_left = False
        char1_right = False
        # char1_walk_count = 0

    if not(char1_isJump):
        if keys[pygame.K_SPACE]:
            char1_isJump = True
            char1_left = False
            char1_right = False
            char1_walk_count = 0

    else:
        if jumpCount >= -10:
            char1_y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            char1_isJump = False
    clock.tick(36)

pygame.quit()
