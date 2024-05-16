import pygame
import random

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
SKY = (100, 200, 237)
GROUND = (140, 80, 35)
GRASS = (40, 200, 40)
RED = (255, 0, 0)
FPS = 60
GROUND_LEVEL = HEIGHT - 200


class Cabin(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(car)
        self.image = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, RED, (x1, y1, x2, y2))

        self.rect = pygame.Rect(x1, y1, x1 + x2, y1 + y2)
        # self.vx = random.randint(-5, 5)
        # self.vy = random.randrange(-5, 5)

    def update(self):
        pass
        # print(1)


class Ball(pygame.sprite.Sprite):
    def __init__(self, r, y, x):
        super().__init__(car)
        self.radius = r
        self.image = pygame.Surface((2 * r, 2 * r), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, GRASS, (r, r), r)
        self.rect = pygame.Rect(x - r, y - r, 2 * r, 2 * r)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        pass
        # self.rect.move_ip(self.vx, self.vy)


pygame.init()
car = pygame.sprite.Group()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Столкновение шариков')

Cabin(400, GROUND_LEVEL - 250, 200, 200)
Ball(20, 100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color(SKY))
    pygame.draw.circle(screen, (200, 200, 0), (200, 200), radius=100)
    pygame.draw.rect(screen, GROUND, pygame.Rect(0, GROUND_LEVEL, WIDTH, 200))
    pygame.draw.rect(screen, GRASS, pygame.Rect(0, GROUND_LEVEL, WIDTH, 20))
    car.draw(screen)
    car.update()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
