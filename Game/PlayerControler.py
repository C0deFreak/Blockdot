import pygame

def control(player):
    keys = pygame.key.get_pressed() 
    if keys:
        
        if keys[pygame.K_LEFT]:  
            player.move(-20)

        if keys[pygame.K_RIGHT]: 
            player.move(20)
