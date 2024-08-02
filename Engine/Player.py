import pygame
from Engine import MapMaker


player_size = MapMaker.block_size
rect = pygame.Rect(0, 0, player_size, player_size)

x = 300
y = 0

velocity = 0.1 * player_size

def round_multiple(x, base=player_size):
    return base * round(x/base)

#def blockDraw():

def control():
    global x
    global y
    # Inventory object setup)

    keys = pygame.key.get_pressed() 
    if keys:
        
        rect.center = (x, y)
        pygame.draw.rect(MapMaker.window, '#3776AB', rect) 

        if tuple((round_multiple(x), int(y + player_size))) not in MapMaker.pos_list:
                y += velocity

        # if left arrow key is pressed 
        if keys[pygame.K_LEFT]:  
            # decrement in x co-ordinate 
            x -= velocity 
            
        # if left arrow key is pressed 
        if keys[pygame.K_RIGHT]: 
            
            # increment in x co-ordinate 
            x += velocity
                 

        # drawing object on screen which is rectangle here  
        rect.center = (x, y)
        pygame.draw.rect(MapMaker.window, 'red', rect) 
        # it refreshes the window 
        pygame.display.update()  

    '''
    # Restart Jump
    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in MapMaker.pos_list:
        jumped = False

    # Gravity
    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' not in MapMaker.pos_list:
        time.sleep(0.2)
        player.goto(player.xcor(), player.ycor() - 20)
        jumped = True

    # Moving right and assign the watch position
    if keyboard.is_pressed('d'):
        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in MapMaker.pos_list:
            player.goto((player.xcor() + 20), player.ycor())
            time.sleep(0.2)
        position_str = f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)'
        build_destination = player.xcor() + 10, player.ycor() + 10

    # Moving left and assign the watch position
    if keyboard.is_pressed('a'):
        if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in MapMaker.pos_list:
            player.goto((player.xcor() - 20), player.ycor())
            time.sleep(0.2)
        position_str = f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)'
        build_destination = player.xcor() - 30, player.ycor() + 10

    # Assign the upper watch position
    if keyboard.is_pressed('w'):
        position_str = f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)'   
        build_destination= player.xcor() - 10, player.ycor() + 30 

    # Assign the bottom watch position
    if keyboard.is_pressed('s'):
        position_str = f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)'
        build_destination = player.xcor() - 10, player.ycor() - 10



    # Delete block
    if keyboard.is_pressed('F') and not inventory_full:                
        
        # Check the position you are looking at
        build.goto(build_destination)

        # Remove the block from the canvas
        if position_str in MapMaker.pos_list:
            block_choice = MapMaker.block_list[MapMaker.pos_list.index(position_str)]
            del MapMaker.block_list[MapMaker.pos_list.index(position_str)]
            MapMaker.pos_list.remove(position_str)
            inventory_full = True
            build.color('#3776AB')
            block_draw()

        if inventory_full:
            inventory.color(block_choice)
        else:
            inventory.color('#8B8B8B')

    # Build
    if keyboard.is_pressed('E') and inventory_full:
        build.fillcolor(block_choice)
        build.pencolor('black')
        build.penup()

        # Check the position you are looking at
        build.goto(build_destination)
            

        # Check if there is any block at the checked position
        if position_str not in MapMaker.pos_list:

            # Add the block from the inventory to its list and position list
            MapMaker.pos_list.append(position_str)
            MapMaker.block_list.append(block_choice)
        
            # Add the block to the canvas and remove it from the inventory
            block_draw()
            inventory_full = False
            inventory.color('#8B8B8B')

    # Jumping
    if keyboard.is_pressed('space') and not jumped:
        time.sleep(0.1)

        # Check how high can the player jump
        if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in MapMaker.pos_list:
            high = 0
        elif f'({int(player.xcor())}.00,{int(player.ycor() + 40)}.00)' in MapMaker.pos_list:
            high = 1
        else:
            high = 2
        
        # Go up for the x amount
        for jump in range(high):
            time.sleep(0.2)
            player.goto(player.xcor(), player.ycor() + 20)

        jumped = True

    '''


