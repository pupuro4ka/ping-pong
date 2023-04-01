from pygame import *
from time import sleep

font.init()
font = font.SysFont('Arial', 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (255,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (255,0,0))

# базовый класс 2D - спрайт для любой игры
# описывает исключительно внешний вид спрайта (персонажа)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed


rocket1 = Player('racket.png', 30, 200, 4, 50, 150)
rocket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)
# переменные вектора мяча
speed_x=3
speed_y=3

BACK = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пинг-Понг')

run = True
finish = False
clock = time.Clock()

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(BACK)

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        rocket1.reset()
        rocket2.reset()
        ball.reset()
# отсюда по конец коментария: если хочешь поиграть с другом, или чтобы программа играла сама в себя.
        #rocket1.update_l()
        #rocket2.update_r()
        rocket1.rect.y = ball.rect.y - 75
# здесь конец коментария.
        rocket2.rect.y = ball.rect.y - 75

        if ball.rect.y > win_height -50 or ball.rect.y < 0:
            speed_y *= -1

        if  sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1.

        if ball.rect.x < 0:
            window.blit(lose1, (200,200))
            display.update()
            sleep = (2)
            finish = True

        if ball.rect.x > win_width - 50:
            window.blit(lose2, (200,200))
            display.update()
            sleep = (2)
            finish = True

    display.update()
    clock.tick(60)