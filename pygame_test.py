import pygame
from sys import exit
from random import randint, choice

from pygame.sprite import Group

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (110,200))
        self.rect = self.image.get_rect(midbottom = (200,700))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 700:
            self.gravity = -26

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 700:
            self.rect.bottom = 700
    
    def update(self):
        self.player_input()
        self.apply_gravity()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        if type == 'car':
            self.image = pygame.image.load('car.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (225,69))
            y_pos = 700
        else:
            self.image = pygame.image.load('charles_leg.jpg').convert()
            self.image = pygame.transform.scale(self.image, (120,145))
            y_pos = 480
        self.rect =  self.image.get_rect(midbottom = (randint(1700,2000),y_pos))
    
    def update(self):
        self.rect.x -= 8
        self.destroy()
    
    def destroy(self):
        if self.rect.x <= -200:
            self.kill()


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_sfc = good_font.render(str(current_time), False, (0,0,0))
    score_rect = score_sfc.get_rect(center = (800, 200))
    screen.blit(score_sfc, score_rect)

"""def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 8

            if obstacle_rect.bottom == 700:
                screen.blit(car_sfc,obstacle_rect)
            else:
                screen.blit(charles_sfc,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -200]

        return obstacle_list
    else:
        return []"""
    
"""def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True
"""
def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    else:
        return True

pygame.init()
size = (1600, 900)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('sicko moding time')
clock = pygame.time.Clock()
good_font = pygame.font.Font('Aaargh.ttf',50)
game_active = False
start_time = 0

#groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

#background and that
bkg_sfc = pygame.image.load('sky.jpg').convert()
bkg_sfc = pygame.transform.scale(bkg_sfc, (1600,900))
grd_sfc = pygame.image.load('ground.jpg').convert()
grd_sfc = pygame.transform.scale(grd_sfc, (1600, 500))

#stuff stuff
name_sfc = good_font.render('Sicko mode Gameing  time', False, (64,64,64))
name_rect = name_sfc.get_rect(center = (800, 120))

#enemy stuf
"""charles_def_size = (120,145)

charles_sfc = pygame.image.load('charles_leg.jpg').convert_alpha()
charles_sfc = pygame.transform.scale(charles_sfc, charles_def_size)

car_sfc = pygame.image.load('car.png').convert_alpha()
car_sfc = pygame.transform.scale(car_sfc, (225,69))

obstacle_rect_list = []"""

#player stuff
player_sfc = pygame.image.load('player.png').convert_alpha()
player_sfc = pygame.transform.scale(player_sfc, (110,200))
"""player_rect = player_sfc.get_rect(midbottom = (200,700))
player_gravity = 0
"""
#intro scrn
game_name = good_font.render('Sicko Mode gam', False, (0,0,128))
game_name_rect = game_name.get_rect(center = (800, 300))

game_message = good_font.render('pressing space = jumping', False, (0,0,128))
game_mess_rect = game_message.get_rect(center = (800, 700))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1600)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if game_active:
            """if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player_rect.bottom >= 700:
                        player_gravity = -26"""
        if not game_active and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacle_timer and game_active:
            obstacle_group.add(Obstacle(choice(['charles', 'car', 'car', 'car', 'car', 'car'])))
            """if randint(0,3):
                obstacle_rect_list.append(car_sfc.get_rect(midbottom = (randint(1700,2000),700)))
            else:
                obstacle_rect_list.append(charles_sfc.get_rect(midbottom = (randint(1700,2000),480)))"""

    
    if game_active:
        #surroundings
        screen.blit(bkg_sfc,(0,0))
        screen.blit(grd_sfc,(0,700))
        screen.blit(name_sfc, name_rect)
        display_score()

        #player
        """player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 700:
            player_rect.bottom = 700
        screen.blit(player_sfc, player_rect)"""
        player.draw(screen)
        player.update()

        #obstacle movers
        obstacle_group.draw(screen)
        obstacle_group.update()
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        game_active = collision_sprite()
        #game_active = collisions(player_rect, obstacle_rect_list)


    else:
        screen.fill((153,51,0))
        screen.blit(game_name, game_name_rect)
        screen.blit(player_sfc, (750,450))
        screen.blit(game_message, game_mess_rect)
        """obstacle_rect_list.clear()
        player_rect.midbottom = (200,700)"""

    pygame.display.update()
    clock.tick(60)
