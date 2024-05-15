game_width = 800
game_height = 800



def get_text_gamemode(gamemode: int) -> str:
    """Получение текста для вывода на экран, в зависимости от игрового режима"""
    if gamemode == 0:
        return "Игра с другом"
    elif gamemode == 1:
        return "Игра с компьютером"
