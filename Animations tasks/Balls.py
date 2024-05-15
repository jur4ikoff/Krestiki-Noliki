import pygame as pg
import random

SIZE = width, height = 600, 400
BACKGROUND_COLOR = 'white'
FPS = 60


class Ball(pg.sprite.Sprite):
    def __init__(self, r, y, x):
        super().__init__(all_sprites)
        self.radius = r
        self.image = pg.Surface((2 * r, 2 * r), pg.SRCALPHA, 32)
        pg.draw.circle(self.image, "red", (r, r), r)
        self.rect = pg.Rect(x - r, y - r, 2 * r, 2 * r)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if pg.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pg.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx


class Border(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


pg.init()
all_sprites = pg.sprite.Group()
horizontal_borders = pg.sprite.Group()
vertical_borders = pg.sprite.Group()

clock = pg.time.Clock()
screen = pg.display.set_mode(SIZE)
pg.display.set_caption('Столкновение шариков')

Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for i in range(10):
    Ball(20, 100, 100)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(pg.Color(BACKGROUND_COLOR))
    all_sprites.draw(screen)
    all_sprites.update()
    pg.display.flip()
    clock.tick(FPS)
pg.quit()
