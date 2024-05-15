import pygame
from constrains import game_width, game_height, get_text_gamemode
# from main import run_main_window


class Game:
    def __init__(self, screen, width, height, mode, field_size):
        # инициализация основных переменных
        self.screen = screen
        self.width = width
        self.height = height
        self.field_size = field_size
        self.mode = mode
        self.cells = [[0] * field_size for i in range(field_size)]
        self.move = 1
        self.win = 0

        self.processing()

    def processing(self) -> None:
        """Запуск всех функций"""

        message = get_text_gamemode(self.mode)
        self.draw_text(f'{message}    Поле {self.field_size}x{self.field_size}', shift_y=5, fontsize=36)
        self.draw_text("Чтобы выйти нажмите ESC", fontsize=28, shift_y=50)

        self.cell_size = int(min(self.width, self.height) // (self.field_size + 1.6))
        self.draw_cells()
        self.count = 0

    def draw_text(self, message, fontsize=28, shift_y=0, color=(250, 250, 250)):
        font = pygame.font.Font(None, fontsize)
        text = font.render(message, True, color)
        text_x = self.width // 2 - text.get_width() // 2
        text_y = text.get_height() + shift_y
        self.screen.blit(text, (text_x, text_y))

    def draw_cells(self) -> None:
        """Рендер клеток"""
        x, y = self.start_x, self.start_y = (self.width // 2 - self.cell_size * self.field_size // 2,
                                             self.height // 2 - self.cell_size * self.field_size // 2)
        for i in range(self.field_size):
            for j in range(self.field_size):
                pygame.draw.rect(self.screen, (250, 250, 250),
                                 (x, y, self.cell_size, self.cell_size), self.cell_size // 50)
                x += self.cell_size
            x = self.start_x
            y += self.cell_size

    def get_cell(self, mouse_pos):
        """Получение номера клетки по координатам мышки"""
        is_cell = True
        x, y = mouse_pos

        if x < self.start_x or x > self.start_x + self.cell_size * self.field_size:
            is_cell = False
        if y < self.start_y or y > self.start_y + self.cell_size * self.field_size:
            is_cell = False

        x -= self.start_x
        y -= self.start_y
        x //= self.cell_size
        y //= self.cell_size
        if is_cell:
            return x, y
        return None

    def get_click(self, mouse_pos):
        """ Обработка нажатия """
        self.cell = self.get_cell(mouse_pos)
        if not self.cell:
            return
        pos_x, pos_y = self.cell

        if self.cells[pos_y][pos_x] == 0 and self.win == 0:
            self.on_click(pos_x, pos_y)
        if self.win == -1:
            print("ничья")
            self.draw_text("Ничья", fontsize=40, shift_y=(self.height - 100), color=(0, 250, 0))
        if self.win == 1:
            print("Победил первый игрок")
            self.draw_text("Победил первый игрок", fontsize=40, shift_y=(self.height - 100), color=(250, 0, 0))
        if self.win == 2:
            print("Победил второй игрок")
            self.draw_text("Победил второй игрок", fontsize=40, shift_y=(self.height - 100), color=(0, 0, 250))

    def on_click(self, pos_x, pos_y):
        x = pos_x * self.cell_size + self.cell_size // 2 + self.start_x
        y = pos_y * self.cell_size + self.cell_size // 2 + self.start_y

        if self.move == 1:
            self.draw_cross(x, y)
            self.cells[pos_y][pos_x] = 1
            self.move = 2
        elif self.move == 2:
            self.draw_circle(x, y)
            self.cells[pos_y][pos_x] = 2
            self.move = 1
        res = self.check_win()
        print(res)
        self.count += 1
        if res != 0:
            self.win = res
            return res
        if self.count == self.field_size ** 2:
            self.win = -1
            return -1
        return -1

    def draw_circle(self, x, y):
        color = pygame.Color((0, 0, 255))
        pygame.draw.circle(self.screen, color, (x, y), radius=self.cell_size // 3, width=self.cell_size // 35)

    def draw_cross(self, x, y):
        shift = (self.cell_size ** 2 + self.cell_size ** 2) ** 0.5 // 5
        color = pygame.Color(225, 0, 0)
        pygame.draw.line(self.screen, color, (x, y),
                         (x + shift, y + shift), width=self.cell_size // 35)
        pygame.draw.line(self.screen, color, (x, y),
                         (x + shift, y - shift), width=self.cell_size // 35)
        pygame.draw.line(self.screen, color, (x, y),
                         (x - shift, y + shift), width=self.cell_size // 35)
        pygame.draw.line(self.screen, color, (x, y),
                         (x - shift, y - shift), width=self.cell_size // 35)

    def check_win(self) -> int:
        """Проверка ситуации на поле на победу"""
        res: int = 0
        # проверка горизонталей
        count1, count2 = 0, 0
        for i in range(self.field_size):
            for j in range(self.field_size - 1):
                if self.cells[i][j] == self.cells[i][j + 1]:
                    if self.cells[i][j] == 1:
                        count1 += 1
                    elif self.cells[i][j] == 2:
                        count2 += 1
                else:
                    count2, count1 = 0, 0
            res = self.check_count(count1, count2)
            if res != 0:
                return res

        count1, count2 = 0, 0
        # проверка вертикалей
        for i in range(self.field_size):
            for j in range(self.field_size - 1):
                if self.cells[j][i] == self.cells[j + 1][i]:
                    if self.cells[j][i] == 1:
                        count1 += 1
                    elif self.cells[j][i] == 2:
                        count2 += 1
                else:
                    count2, count1 = 0, 0
            res = self.check_count(count1, count2)
            if res != 0:
                return res

        # проверка главной диагонали
        count1, count2 = 0, 0
        for i in range(self.field_size - 1):
            if self.cells[i][i] == self.cells[i + 1][i + 1]:
                if self.cells[i][i] == 1:
                    count1 += 1
                elif self.cells[i][i] == 2:
                    count2 += 1
            else:
                count2, count1 = 0, 0
            res = self.check_count(count1, count2)
            if res != 0:
                return res

        count1, count2 = 0, 0
        for i in range(0, self.field_size - 1):
            if self.cells[i][self.field_size - i - 1] == self.cells[i + 1][self.field_size - i - 2]:
                if self.cells[i][self.field_size - i - 1] == 1:
                    count1 += 1
                elif self.cells[i][self.field_size - i - 1] == 2:
                    count2 += 1
            else:
                count2, count1 = 0, 0
            res = self.check_count(count1, count2)
            if res != 0:
                return res

        return res

    def check_count(self, count1: int, count2: int) -> int:
        if count1 == self.field_size - 1:
            return 1
        elif count2 == self.field_size - 1:
            return 2

        return 0


# pygame.init()
# pygame.display.set_caption('Крестики нолики')
# game_size = game_width, game_height
# screen = pygame.display.set_mode(game_size)
# mode = 0
# field_size = 4
# screen.fill((4, 4, 4))
#
# # инициализация класса game
# game = Game(screen, game_width, game_height, mode, field_size)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             game.get_click(event.pos)
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False
#                 pygame.quit()
#                 run_main_window()
#
#     pygame.display.flip()
