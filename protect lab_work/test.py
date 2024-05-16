import pygame
import sys

WIDTH = 800
HEIGHT = 800
WHITE = (255, 255, 255)
SKY = (100, 200, 237)
GROUND = (140, 80, 35)
GRASS = (40, 200, 40)
RED = (255, 0, 0)
FPS = 60
GROUND_LEVEL = HEIGHT - 200


class AnimatedShapes:
    def __init__(self, screen):
        self.width, self.height = WIDTH, HEIGHT
        self.screen = screen

        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.cabin_width, self.cabin_height = 150, 250
        self.cabin_x, self.cabin_y = 400, GROUND_LEVEL - 300
        self.cabin_speed = -1

        self.circle_radius = 25
        self.circle_x, self.circle_y = 450, GROUND_LEVEL - 25
        self.circle_speed = -1

        self.body_width, self.body_height = 250, 100
        self.body_x, self.body_y = self.cabin_x + self.cabin_width, GROUND_LEVEL - 150
        self.body_speed = -1

        self.box_width, self.box_height = 50, 50
        self.box_x, self.box_y = 600, GROUND_LEVEL - 200
        self.box_speed = 1

    def update(self):
        self.cabin_x += self.cabin_speed
        self.circle_x += self.circle_speed
        self.body_x += self.body_speed

        # print(self.body_x, self)
        if self.body_x + self.body_width < self.box_x and self.box_y < GROUND_LEVEL -50:
            self.box_y += self.box_speed

    def draw(self):
        pygame.draw.rect(self.screen, self.black, (self.cabin_x, self.cabin_y, self.cabin_width, self.cabin_height))
        pygame.draw.circle(self.screen, self.black, (self.circle_x, self.circle_y), self.circle_radius)
        pygame.draw.circle(self.screen, self.black, (self.circle_x + 280, self.circle_y), self.circle_radius)
        pygame.draw.rect(self.screen, self.black,
                         (self.body_x, self.body_y, self.body_width, self.body_height))
        pygame.draw.rect(self.screen, self.black, (self.box_x, self.box_y, self.box_width, self.box_height))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Грузовичок")
    animated_shapes = AnimatedShapes(screen)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color(SKY))
        pygame.draw.circle(screen, (200, 200, 0), (125, 125), radius=100)
        pygame.draw.rect(screen, GROUND, pygame.Rect(0, GROUND_LEVEL, WIDTH, 200))
        pygame.draw.rect(screen, GRASS, pygame.Rect(0, GROUND_LEVEL, WIDTH, 20))
        animated_shapes.update()
        animated_shapes.draw()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
