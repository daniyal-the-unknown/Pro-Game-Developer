import pgzrun
import random

WIDTH = 500
HEIGHT = 500

GRAVITY = 2000

color1 = random.randint(0, 255)
color2 = random.randint(0, 255)
color3 = random.randint(0, 255)

class Ball:

    def __init__(self, intial_x, intial_y):

        self.x = intial_x
        self.y = intial_y

        self.vx = 200

        self.vy = 0

        self.radius = 30

    def draw(self):

        pos = (self.x, self.y)

        screen.draw.filled_circle(pos, self.radius, (color1, color2, color3))

ball = Ball(200, 200)

def draw():

    screen.clear()

    ball.draw()

def update(dt):

    uy = ball.vy

    ball.vy += GRAVITY * dt

    ball.y += (uy + ball.vy) * 0.5 * dt

    ball.x += ball.vx * dt

    if ball.y > HEIGHT - ball.radius:

        ball.y = HEIGHT - ball.radius

        ball.vy = -ball.vy * 0.9

    if ball.y < ball.radius:

        ball.y = ball.radius

        ball.vy = -ball.vy

    if ball.x > WIDTH - ball.radius:

        ball.x = WIDTH - ball.radius 

        ball.vx = -ball.vx

    if ball.x < ball.radius:

        ball.x = ball.radius

        ball.vx = -ball.vx

def on_key_down(key):

    if key == keys.SPACE:

        ball.vy = -500

pgzrun.go()

