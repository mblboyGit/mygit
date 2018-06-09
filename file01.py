import pygame
from pygame.locals import *
import sys
import random

WINDOW_HEIGHT = 845
WINDOW_WIDTH = 1200

def run():

    list = []

    x = WINDOW_HEIGHT / 2 - 400
    y = WINDOW_WIDTH / 2 - 350

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    bg_img = pygame.image.load("ball/bk.jpg")
    window.blit(bg_img, (0, 0))

    while True:
        num = random.randint(1, 33)
        if num not in list:
            list.append(num)
        if len(list) == 6:
            break
    list.sort()
    for i in list:
        red_img = pygame.image.load("ball/%d.png" % i)
        window.blit(red_img, (x, y))
        x += 200

    blue_img = pygame.image.load("ball/b%d.png" % random.randint(1, 16))
    window.blit(blue_img, (x - 1000, y + 250))
    print("这就是500万大奖！！")



    pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
                pygame.quit()

            elif event.type == KEYDOWN:

                if event.key == K_SPACE:
                   run()

                elif event.key == K_q:
                    sys.exit()

if __name__ == '__main__':
    run()






