import pygame
from constrains import game_width, game_height, get_text_gamemode
import sys
import os
import main as main


def start_main_wnd():
    if __name__ == '__main__':
        app = main.QApplication(sys.argv)
        ex1 = main.MainWindow()
        ex1.show()
        sys.exit(app.exec())


class Game:
    def __init__(self, screen, width, height, mode, field_size):
        # инициализация основных переменных
        self.screen = screen
        self.width = width
        self.height = height
        self.field_size = field_size
        self.mode = mode
        self.cells = [[0] * field_size for i in range(field_size)]
        self.move = 0

        self.processing()

    def processing(self) -> None:
        """Запуск всех функций"""

        message = get_text_gamemode(self.mode)
        self.draw_text(f'{message}    Поле {field_size}x{field_size}', shift_y=10, fontsize=28)
        self.draw_text("Чтобы выйти нажмите ESC", fontsize=20, shift_y=50)
        self.cell_size = (min(self.width, self.height) // (self.field_size + 2))
        self.draw_cells()

    def draw_text(self, message, fontsize=28, shift_y=0):
        font = pygame.font.Font(None, fontsize)
        text = font.render(message, True, (250, 250, 250))
        text_x = self.width // 2 - text.get_width() // 2
        text_y = text.get_height() + shift_y
        screen.blit(text, (text_x, text_y))

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
        i = y // self.cell_size
        j = x // self.cell_size
        if is_cell:
            return i, j
        return None

    def get_click(self, mouse_pos):
        """ Обработка нажатия """
        self.cell = self.get_cell(mouse_pos)
        if self.cell:
            print(self.cell)
        self.on_click()

    def on_click(self):
        pass
    
    
    
    """
    def on_click(self, cell):
        self.color_red = pygame.Color('Red')
        self.color_blue = pygame.Color('Blue')
        self.cell_pressed = cell

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
        pygame.draw.line(self.screen, self.color_red, (self.x_top_cell_pressed, self.y_top_cell_pressed),
                         (self.x_low_cell_pressed, self.y_low_cell_pressed), width=5)

        pygame.draw.line(self.screen, self.color_red, (self.x_top_cell_pressed1, self.y_top_cell_pressed1),
                         (self.x_low_cell_pressed1, self.y_low_cell_pressed1), width=5)
        self.cell_dict[self.cell_pressed] = 1

    def draw_circ(self):
        pygame.draw.circle(self.screen, self.color_blue, (self.x_center, self.y_center), 50, width=5)
        self.cell_dict[self.cell_pressed] = 2

    def check_win(self):
        win_side = 0
        if (self.cell_dict[0, 0] == self.cell_dict[1, 0] == self.cell_dict[2, 0] == 1) \
                or (self.cell_dict[0, 0] == self.cell_dict[0, 1] == self.cell_dict[0, 2] == 1) \
                or (self.cell_dict[0, 0] == self.cell_dict[1, 1] == self.cell_dict[2, 2] == 1) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 1] == self.cell_dict[2, 0] == 1) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 2] == self.cell_dict[2, 2] == 1) \
                or (self.cell_dict[2, 2] == self.cell_dict[2, 1] == self.cell_dict[2, 0] == 1) \
                or (self.cell_dict[0, 1] == self.cell_dict[1, 1] == self.cell_dict[2, 1] == 1) \
                or (self.cell_dict[1, 0] == self.cell_dict[1, 1] == self.cell_dict[1, 2] == 1):
            print('ПОБЕДА')
            self.win_side = 1
            self.base_event()
            draw_status(self.win_side, self.width, self.height, self.screen)

        if (self.cell_dict[0, 0] == self.cell_dict[1, 0] == self.cell_dict[2, 0] == 2) \
                or (self.cell_dict[0, 0] == self.cell_dict[0, 1] == self.cell_dict[0, 2] == 2) \
                or (self.cell_dict[0, 0] == self.cell_dict[1, 1] == self.cell_dict[2, 2] == 2) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 1] == self.cell_dict[2, 0] == 2) \
                or (self.cell_dict[0, 2] == self.cell_dict[1, 2] == self.cell_dict[2, 2] == 2) \
                or (self.cell_dict[2, 2] == self.cell_dict[2, 1] == self.cell_dict[2, 0] == 2) \
                or (self.cell_dict[0, 1] == self.cell_dict[1, 1] == self.cell_dict[2, 1] == 2) \
                or (self.cell_dict[1, 0] == self.cell_dict[1, 1] == self.cell_dict[1, 2] == 2):
            print('ПОРАЖЕНИЕ')
            self.win_side = 2
            self.base_event()
            draw_status(self.win_side, self.width, self.height, self.screen)

        if self.cell_dict[0, 1] != 0 and self.cell_dict[0, 2] != 0 and self.cell_dict[0, 0] != 0 \
                and self.cell_dict[1, 0] != 0 and self.cell_dict[2, 2] != 0 \
                and self.cell_dict[1, 1] != 0 and self.cell_dict[1, 2] != 0 \
                and self.cell_dict[2, 0] != 0 and self.cell_dict[2, 1] != 0:
            print('НИЧЬЯ')
            self.win_side = 3
            self.base_event()
            draw_status(self.win_side, self.width, self.height, self.screen)
    """

    # def base_event(self):
    #     con = sqlite3.connect("data\\bd.sqlite")
    #     cur = con.cursor()
    #
    #     result = cur.execute("""
    # SELECT *
    #                         FROM Base""").fetchall()
    #
    #     print(self.nick)
    #     for i in result:
    #         if i[1] == self.nick:
    #             if self.win_side == 1:
    #                 win = int(i[2])
    #                 win += 1
    #                 cur.execute("""UPDATE Base
    #                             SET Win = ?
    #                             WHERE Nickname = ?""", (win, self.nick))
    #                 con.commit()
    #             if self.win_side == 2:
    #                 lose = int(i[3])
    #                 lose += 1
    #                 cur.execute("""UPDATE Base
    #                             SET Lose = ?
    #                             WHERE Nickname = ?""", (lose, self.nick))
    #                 con.commit()
    #             if self.win_side == 3:
    #                 draw = int(i[4])
    #                 draw += 1
    #                 cur.execute("""UPDATE Base
    #                             SET Draw = ?
    #                             WHERE Nickname = ?""", (draw, self.nick))
    #                 con.commit()
    #                 print(draw)


pygame.init()
pygame.display.set_caption('Крестики нолики')
game_size = game_width, game_height
screen = pygame.display.set_mode(game_size)
mode = 0
field_size = 3
screen.fill((4, 4, 4))

# инициализация класса game
game = Game(screen, game_width, game_height, mode, field_size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.get_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                start_main_wnd()

    pygame.display.flip()
