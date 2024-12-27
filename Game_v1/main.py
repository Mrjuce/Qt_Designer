from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 60))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x -= self.speed
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_wigth - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed 
        else:
            self.rect.x += self.speed

win_wigth = 700
win_height = 500

window = display.set_mode((win_width, win_height))

display.set_caption("Maze")


background = transform.scale(image.load( "background.jpg"),(win_wigth, win_height))
x1 = 100
y1 = 300

x2 = 300
y2 = 300



run = True
clock = time.Clock()
FPS = 60



































display.update()
clock.tick(FPS)