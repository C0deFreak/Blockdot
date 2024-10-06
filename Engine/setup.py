import pygame

collision_map = {}
window_width, window_height = 1080, 1920
window = pygame.display.set_mode((window_height, window_width))
nothing_color = 'black'

# Sets up the scene                    
def sceneMaker(color='black', title='Game'):
    global window, nothing_color
    pygame.init()

    nothing_color = color
    
    window.fill(color)
    pygame.display.set_caption(title)
    pygame.display.update()
