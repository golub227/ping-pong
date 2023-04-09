from pygame import*
font.init()

window = display.set_mode((700, 500))             
display.set_caption('ping pong')

sprite1 = transform.scale(image.load('i.webp'), (100, 100))
sprite2 = transform.scale(image.load('i.webp'), (100, 100))
speed = 10

x1 = 130
y1 = 110

x2 = 320
y2 = 50
game = True
clock = time.Clock()
FPS = 70

from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



while game:
    for e in event.get():      
        if e.type == QUIT:
            game = False


display.update()
clock.tick(FPS)


















'''from pygame import *

window = display.set_mode((700, 500))             
display.set_caption('Догонялки')
background = transform.scale(image.load('background.png'), (700, 500))

sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))
speed = 10

x1 = 130
y1 = 110

x2 = 320
y2 = 50
game = True
clock = time.Clock()
FPS = 70

while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))


    for e in event.get():
        if e.type == QUIT:
            game = False

        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= speed
        if keys_pressed[K_RIGHT] and x1 < 595:
            x1 += speed
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= speed
        if keys_pressed[K_DOWN] and y1 < 395:
            y1 += speed


        if keys_pressed[K_a] and x1 > 5:
            x2 -= speed
        if keys_pressed[K_d] and x1 < 595:
            x2 += speed
        if keys_pressed[K_w] and y1 > 5:
            y2 -= speed
        if keys_pressed[K_s] and y1 < 395:
            y2 += speed

    
    
    display.update()
    clock.tick(FPS)'''
   
















































