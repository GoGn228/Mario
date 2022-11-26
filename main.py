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
pygame.mixer.music.load('sound/mario.mp3')
pygame.mixer.music.play(-1)
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
    portal_group.update(0)
    portal_group.draw(sc)
    monetka_group.update(0)
    monetka_group.draw(sc)
    enemy_group.update(0)
    enemy_group.draw(sc)
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
           elif maps[i][j]=="9":
              player.rect.x = pos[0]
              player.rect.y = pos[1]
           elif maps[i][j] == "6":
               portal = Portal(portal_image, pos)
               portal_group.add(portal)
               camera_group.add(portal)
           elif maps[i][j] == "5":
               stopenemy = StopEnemy(box_image, pos)
               stopenemy_group.add(stopenemy)
               camera_group.add(stopenemy)
           elif maps[i][j] == "7":
               enemy = Enemy(enemy_1_image, pos)
               enemy_group.add(enemy)
               camera_group.add(enemy)
           if maps[i][j] == "8":
               monetka = Monetka(monetka_image, pos)
               monetka_group.add(monetka)
               camera_group.add(monetka)


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
            if (abs(self.rect.bottom - player.rect.bottom) < 8
                or abs(self.rect.top - player.rect.top) < 50):
                if (player.dir == "left"
                    and abs(self.rect.right - player.rect.left) < 30):
                        player.rect.left = self.rect.right
                if (player.dir == "right"
                    and abs(self.rect.left - player.rect.right) < 30):
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
        if pygame.sprite.spritecollide(self, player_group, False):
            if abs(self.rect.bottom - player.rect.top) < 20:
                player.jump = False
                player.jump_step = -25
                player.on_earth = False
                player.rect.top += 25
            if abs(self.rect.top - player.rect.bottom) < 15:
                player.rect.bottom = self.rect.top
            if (abs(self.rect.bottom - player.rect.bottom) < 8
                or abs(self.rect.top - player.rect.top) < 50):
                if (player.dir == "left"
                    and abs(self.rect.right - player.rect.left) < 30):
                        player.rect.left = self.rect.right
                if (player.dir == "right"
                    and abs(self.rect.left - player.rect.right) < 30):
                        player.rect.right = self.rect.left

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
        if pygame.sprite.spritecollide(self, player_group, False):
            if(abs(self.rect.bottom - player.rect.bottom) < 8
            or abs(self.rect.top - player.rect.top) < 50):
                if (player.dir == "left"
                and abs(player.rect.left - self.rect.right) < 30):
                    player.rect.left = self.rect.right
            if(player.dir == "right"
            and abs(player.rect.right - self.rect.left) < 30):
                player.rect.right = self.rect.left

class Portal(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.image_frames = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
    def update(self, step):
        self.anime = True
        self.rect.x += step
        self.image = portal_image[self.frame]
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS >0.1:
                if self.frame == len(self.image_frames) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

class Monetka(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.score = 0
    def update(self, step):
        self.rect.x += step

class StopEnemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self, step):
        self.rect.x += step

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image[0]
        self.image_frames = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = 1
        self.frame = 0
        self.timer_anime = 0
        self.anime = True
    def update(self, step):
        self.rect.x += step
        if self.dir == 1:
            self.image = self.image_frames[self.frame]
            self.rect.x += self.speed
        elif self.dir == -1:
            self.image = pygame.transform.flip(self.image_frames[self.frame], True, False)
            self.rect.x -= self.speed
        if pygame.sprite.spritecollide(self, stopenemy_group, False):
            self.dir *= -1
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS >0.1:
                if self.frame == len(self.image_frames ) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0

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
        self.hp = 100
        self.score = 0

    def update(self):
        pygame.draw.rect(sc, "black", (self.rect.x - 30, self.rect.y - 30, 100, 20), 2)
        pygame.draw.rect(sc, "red", (self.rect.x - 27, self.rect.y - 27, 96 * (self.hp / 100), 15))
        if pygame.sprite.spritecollide(self, monetka_group, True):
            self.score += 100
        font = pygame.font.SysFont("arial", 40)
        score_font = font.render("SCORE: " + str(self.score), True, "black")
        sc.blit(score_font, (58, 28))
        key = pygame.key.get_pressed()
        self.rect.y += self.gravity
        if pygame.sprite.spritecollide(self, earth_group, False) or pygame.sprite.spritecollide(self, center_group, False):
            self.jump = False
            self.jump_step = -30
            self.on_earth = True
        if key[pygame.K_SPACE] and self.on_earth:
            self.jump = True
        if self.jump:
            self.on_earth = False
            if self.jump_step <= 30:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -30
        if key[pygame.K_d]:
            self.image = player_image
            self.anime = True
            self.dir = "right"
            self.rect.x += self.speed
            if self.rect.right > 800:
                self.rect.right = 800
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
    global portal_group, monetka_group, stopenemy_group, enemy_group
    earth_group = pygame.sprite.Group()
    center_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    box_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    camera_group = pygame.sprite.Group()
    portal_group = pygame.sprite.Group()
    monetka_group = pygame.sprite.Group()
    stopenemy_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
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