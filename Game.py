import pygame
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.top = 10
        self.left = 10
        self.cell_size = 30

        self.move_now = 1
        self.cell_dict = {}
        empty_cell = 0
        for i in range(self.width):
            for j in range(self.height):
                cell_temp = i, j
                self.cell_dict[cell_temp] = empty_cell

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        self.x = self.left
        self.y = self.top
        count_cube = int(self.width) * int(self.height)
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(screen, (255, 255, 255, 100), (self.x, self.y, self.cell_size,
                                                                self.cell_size), width=1)
                self.y += self.cell_size
            self.y = self.top
            self.x += self.cell_size

    def get_cell(self, mouse_pos):
        # print(mouse_pos)
        self.x1, self.y1 = mouse_pos
        self.x1 -= self.left
        self.y1 -= self.top
        self.cell_x = self.x1 // self.cell_size
        self.cell_y = self.y1 // self.cell_size
        cell_coords = self.cell_x, self.cell_y
        if self.cell_x >= self.width or self.cell_x < 0:
            cell_coords = 'None'
        if self.cell_y >= self.height or self.cell_y < 0:
            cell_coords = 'None'
        # print(cell_coords)
        return cell_coords

    def on_click(self, cell):
        self.color_red = pygame.Color('Red')
        self.color_blue = pygame.Color('Blue')

        self.cell_pressed = self.get_cell(event.pos)

        self.x_top_cell_pressed = self.left + self.cell_size * self.cell_x + self.width * 10
        self.y_top_cell_pressed = self.top + self.cell_size * self.cell_y + self.height * 10
        self.x_low_cell_pressed = self.left + self.cell_size * (self.cell_x) \
                                  + self.cell_size - self.width * 10
        self.y_low_cell_pressed = self.top + self.cell_size * (self.cell_y) \
                                  + self.cell_size - self.height * 10

        self.x_top_cell_pressed1 = self.left + self.cell_size * (self.cell_x) \
                                   + self.cell_size - self.width * 10
        self.y_top_cell_pressed1 = self.top + self.cell_size * self.cell_y + self.height * 10
        self.x_low_cell_pressed1 = self.left + self.cell_size * (self.cell_x) \
                                   + self.width * 10
        self.y_low_cell_pressed1 = self.top + self.cell_size * (self.cell_y) \
                                   + self.cell_size - self.height * 10

        self.x_center = self.left + (self.cell_size * self.cell_x) + self.cell_size // 2
        self.y_center = self.top + (self.cell_size * self.cell_y) + self.cell_size // 2

        print(self.cell_pressed)
        if self.cell_pressed != 'None':
            if self.cell_dict[self.cell_pressed] == 0:
                self.move_now += 1
                if self.move_now % 2 == 0:
                    self.draw_crest()
                if self.move_now % 2 == 1:
                    self.draw_circ()
        self.side_win = self.check_win()

    def draw_crest(self):
        pygame.draw.line(screen, self.color_red, (self.x_top_cell_pressed, self.y_top_cell_pressed),
                         (self.x_low_cell_pressed, self.y_low_cell_pressed), width=5)

        pygame.draw.line(screen, self.color_red, (self.x_top_cell_pressed1, self.y_top_cell_pressed1),
                         (self.x_low_cell_pressed1, self.y_low_cell_pressed1), width=5)
        self.cell_dict[self.cell_pressed] = 1

    def draw_circ(self):
        pygame.draw.circle(screen, self.color_blue, (self.x_center, self.y_center), 50, width=5)
        self.cell_dict[self.cell_pressed] = 2

    def check_win(self):
        win_side = 0
        if (self.cell_dict[0, 0] == self.cell_dict[1, 0] == self.cell_dict[2, 0] == 1) \
                or (self.cell_dict[0, 0] == self.cell_dict[0, 1] == self.cell_dict[0, 2] == 1) \
                or (self.cell_dict[0, 0] == self.cell_dict[1, 1] == self.cell_dict[2, 2] == 1) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 1] == self.cell_dict[2, 0] == 1) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 2] == self.cell_dict[2, 2] == 1) \
                or (self.cell_dict[2, 2] == self.cell_dict[2, 1] == self.cell_dict[2, 0] == 1):
            print('победa крестиков')
            win_side = 1
            return win_side
        if (self.cell_dict[0, 0] == self.cell_dict[1, 0] == self.cell_dict[2, 0] == 2) \
                or (self.cell_dict[0, 0] == self.cell_dict[0, 1] == self.cell_dict[0, 2] == 2) \
                or (self.cell_dict[0, 0] == self.cell_dict[1, 1] == self.cell_dict[2, 2] == 2) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 1] == self.cell_dict[2, 0] == 2) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 2] == self.cell_dict[2, 2] == 2) \
                or (self.cell_dict[2, 2] == self.cell_dict[2, 1] == self.cell_dict[2, 0] == 2):
            print('победа ноликов')
            win_side = 2
            return win_side

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Крестики нолики')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    board = Board(3, 3)
    board.set_view(50, 10, 150)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        # screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
