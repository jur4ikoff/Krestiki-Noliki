import pygame
import sqlite3
import sys


class Search_stat:
    def __init__(self, surface, width, height, nick):
        self.screen = surface
        self.width = width
        self.height = height
        self.nick = nick
        if self.nick == '':
            self.nick = 'Anonim'
        print(self.nick)
        self.from_base()

    def from_base(self):
        con = sqlite3.connect("data\\bd.sqlite")
        cur = con.cursor()

        result = cur.execute("""SELECT Win, Lose, Draw
                            FROM Base
                            WHERE Nickname = ?""", (self.nick,)).fetchall()
        res = result[0]
        win = res[0]
        lose = res[1]
        draw = res[2]
        text = ["Статистика",
                "",
                "Вы победили: " + str(win) + " раз",
                "Вы проиграли: " + str(lose) + " раз",
                "Матчей сыгранных в ничью: " + str(draw),
                "нажмите на крестик, чтобы выйти"]
        font = pygame.font.Font(None, 40)
        text_coord = self.height / 3
        for line in text:
            string_rendered = font.render(line, 1, pygame.Color('white'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = self.width // 4
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)