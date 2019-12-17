import pygame
import random
import time

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

laserSound = pygame.mixer.Sound("sounds/laser.ogg")

pygame.mixer.music.load("sounds/bgMusic.ogg")
pygame.mixer.music.play(-1,0.0)

black = (0, 0, 0)
white = (255, 255, 255)
space = (0, 76, 153)
silver = (192, 192, 192)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./small/enemy.png').convert()
        self.image.set_colorkey(white)

        self.rect = self.image.get_rect()

    def update(self): 
        global left
        global right
        if self.rect.x <= 0:
            left = 1
            right = 0
        if self.rect.x+55 >= game_display_width:
            right = 1
            left = 0

        if left == 1 and right == 0:
                self.rect.x += 1 
        if right == 1 and left == 0:
                self.rect.x -= 1 
       


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./small/1.png').convert()
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

    def update(self):         # enemy movements
        self.rect.x += 3
        if enemy.rect.x > game_display_width:
            self.rect.y = 30
            self.rect.x = 0

class Enemy2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./small/6.png').convert()
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

    def update(self):         # enemy movements
        self.rect.x += 2
        if enemy2.rect.x > game_display_width:
            self.rect.y = 90
            self.rect.x = 0

class Enemy3(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('./small/3.png').convert()
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

    def update(self):         # enemy movements
        self.rect.x += 4
        if enemy1.rect.x > game_display_width:
            self.rect.y = 30
            self.rect.x = 0


class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('./small/5.png').convert()
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

    def update(self):                  # player movements

        event = pygame.key.get_pressed()
        if event[pygame.K_LEFT]:
            self.rect.x -= 5
        if event[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= game_display_width - 70:
            self.rect.x = game_display_width - 70

class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./small/bullet5.png').convert()
        self.image.set_colorkey(white)
        # self.image = pygame.Surface([6, 25])
        # self.image.fill(white)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 15

class EBullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./small/bullet3.png').convert()
        self.image.set_colorkey(white)
        # self.image = pygame.Surface([6, 25])
        # self.image.fill(white)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 10

class E2Bullet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./small/bullet5.png').convert()
        self.image.set_colorkey(white)
        # self.image = pygame.Surface([6, 25])
        # self.image.fill(white)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 10


pygame.init()

game_display_width = 510
game_display_height = 635
object_width = 50
background = pygame.image.load('./small/b2.jpg')
title = pygame.image.load('./small/m2.PNG')
game_display = pygame.display.set_mode([game_display_width, game_display_height])
font = pygame.font.Font('./small/Algerian Regular.ttf', 25)


def end_game():
    pygame.quit()
    quit()


def display_background():
    game_display.blit(background, (0, 0)) 


def text_sizer(surf, text, size, x, y):
    font = pygame.font.Font('./small/Algerian Regular.ttf', 30)
    textsurf = font.render(text, True, silver)
    textrect = textsurf.get_rect()
    textrect.midtop = (x, y)
    surf.blit(textsurf, textrect)

def unpause():
    global pause
    pause=False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                end_game()
            if event.key == pygame.K_q:
                end_game()
            if event.key == pygame.K_RETURN:
                unpause()
        
        pygame.draw.rect(game_display,black,(40,420,430,90))
   
        text_sizer(game_display, " Hit  [ENTER]  to Continue !!! ", 40, game_display_width / 2,game_display_height / 1.5)
        text_sizer(game_display, " Hit  [Q]      to Quit  !!!", 40, game_display_width / 2,(game_display_height / 1.35)) 
        pygame.display.update()
        clock.tick(15)

def game_intro():
    game_display.blit(title, (0, 0)) 
    start = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    return
                if event.key == pygame.K_q:
                    end_game()
                if event.type == pygame.QUIT:
                    end_game()
            else:
                text_sizer(game_display, " Hit  [ENTER]  to Begin !!! ", 40, game_display_width / 2,
                           game_display_height / 1.5)
                text_sizer(game_display, " Hit  [Q]      to Quit  !!!", 40, game_display_width / 2,
                           (game_display_height / 1.35))
                text_sizer(game_display, " Use [UP] to Shoot Bullets  !!!", 40, game_display_width / 2,
                           (game_display_height / 1.22))
                text_sizer(game_display, " Use  [LEFT] & [RIGHT] to Move  !!!", 40, game_display_width / 2,
                           (game_display_height / 1.11))
                pygame.display.update()

 

def scored(count):
    font = pygame.font.Font('./small/Algerian Regular.ttf', 25)
    text = font.render("SCORE : " + str(count), True, white)
    game_display.blit(text, (0, 0))


all_sprites_list = pygame.sprite.Group()

block_list = pygame.sprite.Group()

bullet_list = pygame.sprite.Group()

Ebullet_list = pygame.sprite.Group()


player_list = pygame.sprite.Group()

main_enemy_list = pygame.sprite.Group()
main_enemy_list1 = pygame.sprite.Group()

player = Player()
player_list.add(player)
all_sprites_list.add(player)

enemy = Enemy()
all_sprites_list.add(enemy)
main_enemy_list.add(enemy)

pause = False
done = False

clock = pygame.time.Clock()

left=1
right=0
score = 0
cap = 0
cap1 = 0
player.rect.y = 570
enemy.rect.y = 30
shoot = 4
shoot1 = 3
shoot2 = 2
game_intro()

for i in range(15):
    block = Block()

    block.rect.x = random.randrange(game_display_width - 30)
    block.rect.y = random.randrange(100, 450)

    block_list.add(block)
    all_sprites_list.add(block)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        if event.key==pygame.K_p:
            pause=True
            paused()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.Sound.play(laserSound)
                bullet = Bullet()
                bullet2 = Bullet()
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                bullet2.rect.x = player.rect.x + 55
                bullet2.rect.y = player.rect.y

                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                all_sprites_list.add(bullet2)
                bullet_list.add(bullet2)

        if player.rect.x < 0:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.rect.x = 0

        if player.rect.x + object_width > game_display_width:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.rect.x = 450

    if shoot % 59 == 0 and cap<3:
        bullet3 = EBullet()
        bullet3.rect.x = enemy.rect.x
        bullet3.rect.y = enemy.rect.y + 55

        all_sprites_list.add(bullet3)
        Ebullet_list.add(bullet3)

    shoot = random.randint(0,100)

    all_sprites_list.update()

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    for b in bullet_list:
        hit_list = pygame.sprite.spritecollide(b, main_enemy_list, False)
        if cap == 3:
            remv_list = pygame.sprite.spritecollide(b, main_enemy_list, True)
       

        for elem in hit_list:
            bullet_list.remove(b)
            all_sprites_list.remove(b)
            score += 5
            cap += 1

        if bullet.rect.y < -10:
            bullet_list.remove(b)
            all_sprites_list.remove(b)

    for eb in Ebullet_list:
        player_hit_list = pygame.sprite.spritecollide(eb, player_list, True)

        for k in player_hit_list:
            Ebullet_list.remove(eb)
            all_sprites_list.remove(eb)


        if eb.rect.y > 640:
            Ebullet_list.remove(eb)
            all_sprites_list.remove(eb)

        if len(player_hit_list) != 0:
            game_display.fill(black)
            text_sizer(game_display, " YOU LOSE !!! ", 40, game_display_width / 2,
                           game_display_height / 2)
            pygame.display.update()
            pygame.time.wait(1000)
            end_game()

    game_display.fill(black)
    display_background()
    all_sprites_list.draw(game_display)
    scored(score)

    pygame.display.update()

    clock.tick(60)
    if score == 35:
        game_display.fill(black)
        text_sizer(game_display, " LEVEL 1   COMPLETE !!! ", 40, game_display_width / 2,
                   game_display_height / 2)
        pygame.display.update()
        pygame.time.wait(1000)
        game_display.fill(black)
        text_sizer(game_display, " LEVEL 2    BEGIN !!! ", 40, game_display_width / 2,
                   game_display_height / 2)
        pygame.display.update()
        pygame.time.wait(1000)
        done = True
        all_sprites_list.remove(bullet_list)
        all_sprites_list.remove(Ebullet_list)
         
        

score = 0
cap=0

enemy1 = Enemy3()
all_sprites_list.add(enemy1)
main_enemy_list.add(enemy1)


enemy2 = Enemy2()
all_sprites_list.add(enemy2)
main_enemy_list1.add(enemy2)
enemy1.rect.y = 30
enemy2.rect.y = 110

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        if event.key==pygame.K_p:
            pause=True
            paused()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.Sound.play(laserSound)
                bullet = Bullet()
                bullet2 = Bullet()
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
                bullet2.rect.x = player.rect.x + 55
                bullet2.rect.y = player.rect.y

                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                all_sprites_list.add(bullet2)
                bullet_list.add(bullet2)

        if player.rect.x < 0:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.rect.x = 0

        if player.rect.x + object_width > game_display_width:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.rect.x = 450

    if shoot1 % 59 == 0 and cap != 1:
        bullet3 = EBullet()
        bullet3.rect.x = enemy1.rect.x
        bullet3.rect.y = enemy1.rect.y + 55

        all_sprites_list.add(bullet3)
        Ebullet_list.add(bullet3)
 
    if shoot2 % 59 == 0 and cap1 != 1:
        bullet4 = E2Bullet()
        bullet4.rect.x = enemy2.rect.x
        bullet4.rect.y = enemy2.rect.y + 55

        all_sprites_list.add(bullet4)
        Ebullet_list.add(bullet4)

    shoot1 = random.randint(0,100)
    shoot2 = random.randint(0,100)
    all_sprites_list.update()

    '''for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)'''

    for b in bullet_list:
        hit_list2 = pygame.sprite.spritecollide(b, main_enemy_list, False)
        if cap == 3:
            remv_list = pygame.sprite.spritecollide(b, main_enemy_list, True)
       

        for elem in hit_list2:
            bullet_list.remove(b)
            all_sprites_list.remove(b)
            score += 5
            cap += 1

        if bullet.rect.y < -10:
            bullet_list.remove(b)
            all_sprites_list.remove(b)

    '''for b in bullet_list:
        hit_list2 = pygame.sprite.spritecollide(b, main_enemy_list, True)        

        for elem in hit_list2:
            bullet_list.remove(b)
            all_sprites_list.remove(b)
            score += 5
            cap = 1 
       

        if bullet.rect.y < -10:
            bullet_list.remove(b)
            all_sprites_list.remove(b)'''

    for bu in bullet_list:
        hit_list3 = pygame.sprite.spritecollide(b, main_enemy_list1, True)        

        for elem in hit_list2:
            bullet_list.remove(b)
            all_sprites_list.remove(b)
            score += 5
            cap1 = 1  
       

        if bullet.rect.y < -10:
            bullet_list.remove(b)
            all_sprites_list.remove(b)

    for eb2 in Ebullet_list:
        player_hit_list2 = pygame.sprite.spritecollide(eb2, player_list, True)

        for k in player_hit_list2:
            Ebullet_list.remove(eb2)
            all_sprites_list.remove(eb2)


        if eb2.rect.y > 640:
            Ebullet_list.remove(eb2)
            all_sprites_list.remove(eb2)

        if len(player_hit_list2) != 0:
            game_display.fill(black)
            text_sizer(game_display, " YOU LOSE !!! ", 40, game_display_width / 2,
                           game_display_height / 2)
            pygame.display.update()
            pygame.time.wait(1000)
            end_game()

    game_display.fill(black)
    display_background()
    all_sprites_list.draw(game_display)
    scored(score)

    pygame.display.update()

    clock.tick(60)
    if score >= 20:
        game_display.fill(black)
        text_sizer(game_display, " LEVEL 2   COMPLETE !!! ", 40, game_display_width / 2,
                   game_display_height / 2)
        text_sizer(game_display, " YOU   WON  !!!", 40, game_display_width / 2,
                           (game_display_height / 1.35))
        pygame.display.update()
        pygame.time.wait(1000)
        end_game()


pygame.quit()
