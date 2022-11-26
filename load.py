import pygame
earth_image = pygame.image.load("image/blocks/earth.png").convert_alpha()
center_image = pygame.image.load("image/blocks/center.png").convert_alpha()
water_image = pygame.image.load("image/blocks/water.png").convert_alpha()
box_image = pygame.image.load("image/blocks/box.png").convert_alpha()
player_image = pygame.image.load("image/player/mario.png").convert_alpha()
player_image_reverse = pygame.image.load("image/player/mario_reverse.png").convert_alpha()
stop_image = pygame.image.load("image/blocks/stop.png").convert_alpha()
enemy_1_image = [pygame.image.load("image/enemy/goomba.png").convert_alpha(),
                 pygame.image.load("image/enemy/goomba2.png").convert_alpha()]
enemy_2_image = pygame.image.load("image/enemy/2/1.png").convert_alpha()
enemy_3_image = pygame.image.load("image/enemy/3/1.png").convert_alpha()
enemy_4_image = pygame.image.load("image/enemy/4/1.png").convert_alpha()
portal_image = [pygame.image.load("image/portal/Portal_100x100px1.png").convert_alpha(),
                pygame.image.load("image/portal/Portal_100x100px2.png").convert_alpha(),
                pygame.image.load("image/portal/Portal_100x100px3.png").convert_alpha()]
monetka_image = pygame.image.load("image/item/coin.png").convert_alpha()