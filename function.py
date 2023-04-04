from date import *
def is_game_close(): # вернуть необходимость выхода из программы
    return game_close
def quit_game(): # Выйти из программы
    quit()
def event():
    global game_close
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_close = True

def simulation():
    if snake_direction == 'right':
        snake_head['x'] += 1

def drawSneakHead():
    pygame.draw.rect(dis, c, (snake_head['x']*10, snake_head['y']*10, 10, 10))

def display():
    drawSneakHead()
    pygame.display.update()
    dis.fill(black)
    clock.tick(5)

