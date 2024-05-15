from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from constrains import WIDTH, HEIGHT, game_width, game_height
from PyQt6 import uic
from game import Game
import sys
import pygame
import os
import warnings

warnings.filterwarnings('ignore')


def load_image(name):
    """Загрузка изображения"""
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        surface = pygame.Surface((200, 200))
        surface.fill((0, 0, 0))
        return surface
    image = pygame.image.load(fullname)
    return image


def render_intro_text(screen, text):
    """Рендер текста на заставке"""
    font = pygame.font.Font(None, 36)
    text_coord = HEIGHT // 3
    for line in text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = WIDTH // (WIDTH // 125)
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def run_start_screen():
    """Запуск заставки"""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    intro_text = ["                     Крестики Нолики",
                  "",
                  "                       Правила игры",
                  "        ваша задача закрыть все клетки,",
                  "по вертикали, горизонтали или диагонали",
                  "  Для начала нажмите на любую клавишу"]

    # установка фона
    fon = pygame.transform.scale(load_image('background.png'), (WIDTH, HEIGHT))
    fon.set_alpha(50)
    screen.fill((0, 0, 0, 100))
    screen.blit(fon, (0, 0))

    render_intro_text(screen, intro_text)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                running = False
        pygame.display.flip()
    pygame.quit()


def run_main_window():
    """Запуск главного окна"""
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data/menu.ui', self)
        self.initUI()

    def initUI(self):
        """base settings"""
        self.setFixedSize(WIDTH, HEIGHT)
        self.size = 3
        self.AboutMenu.triggered.connect(self.show_author_info)
        self.comboBox.currentTextChanged.connect(self.on_combobox_activated)
        self.runButton.clicked.connect(self.start_game)

    def on_combobox_activated(self, text):
        """Получение информации с comboBox"""
        self.size = int(text)

    def show_author_info(self):
        """Вывод информации об авторе"""
        author_info = ("                           Выполнил Попов Ю.А. ИУ7-22Б\n"
                       "Игроки по очереди ставят на крестик или нолик на свободную клетку. Игрок, первым выстроивший"
                       "в ряд свои фигуры по вертикали, горизонтали или диагонали, выигрывает."
                       "Первый ход делает игрок, ставящий "
                       "крестики.")
        QMessageBox.information(self, 'Информация', author_info)

    def start_game(self):
        """Запуск игры в отдельном процессе"""
        self.hide()

        pygame.init()
        pygame.display.set_caption('Крестики нолики')
        game_size = game_width, game_height
        screen = pygame.display.set_mode(game_size)
        mode = 0
        screen.fill((4, 4, 4))

        # инициализация класса game
        game = Game(screen, game_width, game_height, mode, self.size)
        running = True
        # self.show()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.get_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.flip()
        pygame.quit()
        self.show()
        #


if __name__ == '__main__':
    """Общий запуск"""
    run_start_screen()
    run_main_window()
