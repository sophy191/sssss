import pygame
pygame.init()
rect_size = 20
field_size=20
dis = pygame.display.set_mode((400,300))
pygame.display.set_caption('Snake')
game_close = False
c = (183, 89, 222)
black = (0, 0, 0)
snake_direction = 'right'
snake_head = {'x': 0, 'y':0}
clock = pygame.time.Clock()