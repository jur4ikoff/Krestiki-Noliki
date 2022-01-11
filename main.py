import sys
import pygame
import os
import Game as game
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog
from PyQt5.QtWidgets import QCheckBox, QLabel, QLineEdit, QVBoxLayout, QGridLayout
import sqlite3
import datetime as dt
from PyQt5.QtWidgets import QTableWidgetItem, QDialog

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def start_screen():
    FPS = 144
    clock = pygame.time.Clock()
    intro_text = ["   ЗАСТАВКА", "",
                  "Правила игры",
                  "ваша задача закрыть все клетки,",
                  "по вертикали или горизонтали или диагонали",
                  "Для начала нажмите на пробел"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 40)
    text_coord = height // 3
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = width // 4
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


class AboutWindow(QWidget):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText('Игроки по очереди ставят на свободные клетки поля 3×3 знаки.'
                          'Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или'
                          ' диагонали, выигрывает. Первый ход делает игрок, ставящий крестики'
                          'Обычно по завершении партии выигравшая сторона зачёркивает чертой свои'
                          ' три знака (нолика или крестика), составляющих сплошной ряд.')
        self.layout().addWidget(self.info)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_menu.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton_2.clicked.connect(self.btn2)
        self.pushButton.clicked.connect(self.nick_proceed)
        self.def_text = 'Ваш никнейм:'
        self.nick = self.lineEdit.text()
        print(self.nick)
    def about(self):
        self.about_window.show()


    def btn2(self):
        self.enm = 1
        self.start_game()

    def nick_proceed(self):
        self.nick = self.lineEdit.text()
        if self.nick == '':
            self.nick = 'Anonim'
        self.label_5.setText(self.def_text + ' ' + self.nick)
        print(self.nick)
        con = sqlite3.connect("data\\bd.sqlite")
        cur = con.cursor()

        result = cur.execute("""SELECT Nickname
                    FROM Base""").fetchall()
        if self.nick not in result:
            pass

        #for elem in result:
        #    pass

    def start_game(self):
        if __name__ == '__main__':
            pygame.init()
            pygame.display.set_caption('Крестики нолики')
            size = width, height = 1280, 720
            screen = pygame.display.set_mode(size)
            board = game.Board(3, 3, screen, self.enm, self.nick)
            board.set_view(50, 10, 150)
            running = True
            MainWindow.hide(self)
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        MainWindow.show(self)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        board.get_click(event.pos)
                # screen.fill((0, 0, 0))
                board.render(screen)
                pygame.display.flip()


def main_wnd():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MainWindow()
        ex.show()
        sys.exit(app.exec())


if __name__ == '__main__':
    running = True
    start_screen()
    main_wnd()

    # player, level_x, level_y = generate_level(load_level(name_lvl))
    while running:
        a = None
        ev = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pass
        pygame.display.flip()
        screen.fill((255, 255, 255))
    pygame.quit()

# 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
