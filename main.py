from Engine.setup import sceneMaker
from Engine import static_objects, dynamic_objects
from Game.PlayerControler import control
import pygame

sceneMaker()

# ON START (called once)
square = static_objects.Rectangle(height=100)
player = dynamic_objects.DynamicRectangle(50, 50, 'red', [250, 250])



# GAME LOOP (called every 10ms)
run = True

while run: 
    pygame.time.delay(10) 
    pygame.display.update()

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False


    # YOUR FUNCTIONS
    control(player=player)


            

pygame.quit()