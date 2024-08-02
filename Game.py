from Engine import MapMaker
from Engine import Player
import pygame

# Begins drawing the map

MapMaker.maker()
# Indicates pygame is running 
run = True
  
# infinite loop  
while run: 
    # creates time delay of 10ms  
    pygame.time.delay(10) 
      
    # iterate over the list of Event objects   
    # that was returned by pygame.event.get() method.   
    for event in pygame.event.get(): 
          
        # if event object type is QUIT   
        # then quitting the pygame   
        # and program both.   
        if event.type == pygame.QUIT: 
              
            # it will make exit the while loop  
            run = False
    
    Player.control()

pygame.quit()