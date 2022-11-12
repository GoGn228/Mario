import pygame
import os
import sys
import random

pygame.init()
current_path=os.path.dirname(__file__)
os.chdir(current_path)
WIDTH=1200
HEIGHT=800
FPS=60
sc=pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()

from load import *

def game_lvl():
    sc.fill((91, 146, 235))
    earth_group.update(0)
    earth_group.draw(sc)
    center_group.update(0)
    center_group.draw(sc)
    water_group.update(0)
    water_group.draw(sc)
    box_group.update(0)
    box_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    pygame.display.update()

def drawMaps(nameFile):
    maps=[]
    source="game_lvl/" + str(nameFile)
    with open(source, "r") as file:
        for i in range(0, 10):
            maps.append(file.readline().replace("\n", "").split(",")[0:-1])

    pos=[0, 0]
    for i in range(0, len(maps)):
        pos[1] = i *80
        for j in range(0, len(maps[0])):
           pos[0]=80 * j
           if maps[i][j]=="3":
              earth=Earth(earth_image, pos)
              earth_group.add(earth)
              camera_group.add(earth)
           elif maps[i][j]=="2":
              center=Center(center_image, pos)
              center_group.add(center)
              camera_group.add(center)
           elif maps[i][j]=="4":
              water=Water(water_image, pos)
              water_group.add(water)
              camera_group.add(water)
           elif maps[i][j] == "1":
               box = Box(box_image, pos)
               box_group.add(box)
               camera_group.add(box)
           elif maps[i][j]=="5":
              player.rect.x = pos[0]
              player.rect.y = pos[1]


class Earth(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.bottom - player.rect.top) < 20:
                player.jump = False
                player.jump_step = -25
                player.on_earth = False
                player.rect.top += 25
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top
            if (
                        abs(self.rect.bottom - player.rect.bottom) < 8
                        or abs(self.rect.top - player.rect.top) < 50
            ):
                if (
                        player.dir == "left"
                        and abs(self.rect.top - player.rect.top) < 30
                ):
                    player.rect.left = self.rect.right

                if (

                        player.dir == "right"
                        and abs(self.rect.left - player.rect.right) < 30
                ):
                    player.rect.right = self.rect.left

class Center(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

class Water(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

class Box(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, step):
        self.rect.x += step

class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 10
        self.dir = "right"
        self.gravity = 10
        self.jump_step = -25
        self.jump = False
        self.on_earth = True

    def update(self):
        key = pygame.key.get_pressed()
        self.rect.y += self.gravity
        if pygame.sprite.spritecollide(self, earth_group, False):
            self.jump = False
            self.jump_step = -25
            self.on_earth = True
        if key[pygame.K_SPACE] and self.on_earth:
            self.jump = True
        if self.jump:
            self.on_earth = False
            if self.jump_step <= 25:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -25
        if key[pygame.K_d]:
            self.image = player_image
            self.dir = "right"
            self.rect.x += self.speed
            if self.rect.right > 1000:
                self.rect.right = 1000
                camera_group.update(-self.speed)
        if key[pygame.K_a]:
            self.image = player_image_reverse
            self.dir = "left"
            self.rect.x -= self.speed
            if self.rect.left < 200:
                self.rect.left = 200
                camera_group.update(self.speed)








def restart():
    global earth_group, center_group, water_group
    global box_group, player_group, camera_group, player
    earth_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    player=Player(player_image, (0, 0))
    player_group.add(player)

restart()
drawMaps("1.txt")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)