
from pygame import *
from random import randint 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]:
            self.rect.x += self.speed
    def shoot(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15)
        bullets.add(bullet)
            

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()

bullets = sprite.Group()









lost = 0
class Enemy(GameSprite):
    
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
            global lost
        if self.rect.y >=500:
            self.rect.x = randint(5,635)
            self.rect.y = 0
            lost = lost + 1










win_width = 700
win_height = 500
window = display.set_mode(
    (win_width, win_height)
)
display.set_caption("галактия")
background = transform.scale(
    image.load("universe-2742113_1280.jpg"),
    (win_width, win_height)
)
game = True

FPS = 60
clock = time.Clock()
window.blit(background,(0,0))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
rocket = Player('rocket.png',310,390,10)

monsters1 = Enemy('ufo.png',randint(5,635),0,randint(1,4))
monsters2 = Enemy('ufo.png',randint(5,635),0,randint(1,4))
monsters3 = Enemy('ufo.png',randint(5,635),0,randint(1,4))
monsters4 = Enemy('ufo.png',randint(5,635),0,randint(1,4))
monsters5 = Enemy('ufo.png',randint(5,635),0,randint(1,4))
monsters = sprite.Group()
monsters.add(monsters1)
monsters.add(monsters2)
monsters.add(monsters3)
monsters.add(monsters4)
monsters.add(monsters5)

font.init()
font2 = font.SysFont('Arial', 36)
font1 =  font.SysFont('Arial',72)
score = 0
finish = False
while game:
    if not finish:
        window.blit(background,(0,0))
        rocket.update()
        rocket.reset()
        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        

        text_lose = font2.render('Пропущено:' + str(lost),True,(255,255,255))  
        window.blit(text_lose,(10,50))

        text_lose = font2.render('Убиты:' + str(score),True,(255,255,255))  
        window.blit(text_lose,(10,80))
        
        text_lose = font2.render('Vlados Classicgreat:' + str(score),True,(255,255,255))  
        window.blit(text_lose,(420,50))

        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    rocket.shoot()

        collides = sprite.groupcollide(monsters,bullets,True,True)
        for c in collides:
            score += 1
            monster = Enemy("ufo.png",randint(80,620),0,randint(1,5))
            monsters.add(monster)
        if sprite.spritecollide(rocket,monsters,False) or lost >= 3 :
            popusk = font1.render('Проигрыш:',True,(255,255,255))       
            finish = True

        if score >=10:
            molodec = font1.render('ты выйграл:',True,(255,255,255))         
            game = True


    display.update()
    clock.tick(FPS)
