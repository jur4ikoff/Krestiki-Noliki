import pygame
import random
import os, sys

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = pygame.transform.scale(image, (50, 50))
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("data.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1,
                                   random.randrange(3) - 1)


all_sprites = pygame.sprite.Group()

bomb_image = load_image("data.png")
for _ in range(10):
    Bomb(all_sprites)

running = True
while running:
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    pygame.display.flip()
