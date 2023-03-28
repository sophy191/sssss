from date import *
def is_game_close(): # вернуть необходимость выхода из программы
    return game_close
def display(): # Отрисовать все объекты
    pass
def quit_game(): # Выйти из программы
    quit()
def event():
    global game_close
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_close = True

def simulation():
    pass
def display():
    pygame.draw.rect(dis,(255,255,255),(75,75,50,50))
    pygame.display.update()

