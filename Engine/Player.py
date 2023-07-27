import keyboard
import turtle
import time

build = turtle.Pen()
build.hideturtle()
build.speed(0)


# Draw a square (block) on the canvas
def block_draw():
    build.pendown()
    build.begin_fill()
    for cube in range(4):
        build.forward(20)
        build.right(90)
    build.end_fill()

    build.forward(20)
    build.penup()


def control(position_list, grass_list, dirt_list, stone_list, sand_list, diorite_list, snow_list, leaf_list, trunk_list, trunk_col, leaf_col):

    # Player object setup
    player = turtle.Pen()
    player.penup()
    player.goto(-10, 210)
    player.speed(0)
    player.shapesize(1)
    player.shape('square')
    player.color('red')
    player.showturtle()
    jumped = False

    # Inventory object setup
    block_choice = ''
    inventory = turtle.Pen()
    inventory.shape('square')
    inventory.color('#8B8B8B')
    inventory.shapesize(1.5)
    inventory.penup()
    inventory.goto(-677, 317)
    inventory_full = False

    while True:
        position_list.sort()

        # Restart Jump
        if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in position_list:
            jumped = False

        # Gravity
        if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' not in position_list:
            time.sleep(0.2)
            player.goto(player.xcor(), player.ycor() - 20)
            jumped = True

        # Moving right and assign the watch position
        if keyboard.is_pressed('d'):
            if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in position_list:
                player.goto((player.xcor() + 20), player.ycor())
                time.sleep(0.2)
            watching = 'd'

        # Moving left and assign the watch position
        if keyboard.is_pressed('a'):
            if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in position_list:
                player.goto((player.xcor() - 20), player.ycor())
                time.sleep(0.2)
            watching = 'a'

        # Assign the upper watch position
        if keyboard.is_pressed('w'):
            watching = 'w'

        # Assign the bottom watch position
        if keyboard.is_pressed('s'):
            watching = 's'


        # Delete block
        if keyboard.is_pressed('F') and not inventory_full:
            build.penup()

            # Check the position you are looking at
            if watching == 'w':
                build.goto(player.xcor() - 10, player.ycor() + 30)
                position_str = f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)'        

            if watching == 'a':
                build.goto(player.xcor() - 30, player.ycor() + 10)
                position_str = f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)'

            if watching == 's':
                build.goto(player.xcor() - 10, player.ycor() - 10)
                position_str = f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)'

            if watching == 'd':
                build.goto(player.xcor() + 10, player.ycor() + 10)
                position_str = f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)'
                    
            # Append the correct block to the inventory
            if position_str in leaf_list:
                block_choice = leaf_col
            elif position_str in grass_list:
                block_choice = 'green'
            elif position_str in dirt_list:
                block_choice = 'SaddleBrown'
            elif position_str in stone_list:
                block_choice = 'cornsilk4'
            elif position_str in sand_list:
                block_choice = 'khaki3'
            elif position_str in diorite_list:
                block_choice = 'gray80'
            elif position_str in snow_list:
                block_choice = 'white'
            elif position_str in trunk_list:
                block_choice = trunk_col

            # Remove the block from the canvas
            if position_str in position_list:
                position_list.remove(position_str)
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
            if watching == 'w':
                build.goto(player.xcor() - 10, player.ycor() + 30)
                position_str = f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)'

            if watching == 'a':
                build.goto(player.xcor() - 30, player.ycor() + 10)
                position_str = f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)'

            if watching == 's':
                build.goto(player.xcor() - 10, player.ycor() - 10)
                position_str = f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)'

            if watching == 'd':
                build.goto(player.xcor() + 10, player.ycor() + 10)
                position_str = f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)'

            # Check if there is any block at the checked position
            if position_str not in position_list:

                # Add the block from the inventory to its list and position list
                position_list.append(position_str)
                if block_choice == 'green':
                    grass_list.append(position_str)
                if block_choice == 'SaddleBrown':
                    dirt_list.append(position_str)
                if block_choice == 'cornsilk4':
                    stone_list.append(position_str)
                if block_choice == 'khaki3':
                    sand_list.append(position_str)
                if block_choice == 'gray80':
                    diorite_list.append(position_str)
                if block_choice == 'white':
                    snow_list.append(position_str)
                if block_choice == trunk_col:
                    trunk_list.append(position_str)
                if block_choice == leaf_col:
                    leaf_list.append(position_str)
                
                # Add the block to the canvas and remove it from the inventory
                block_draw()
                inventory_full = False
                inventory.color('#8B8B8B')

        # Jumping
        if keyboard.is_pressed('space') and not jumped:
            time.sleep(0.1)

            # Check how high can the player jump
            if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in position_list:
                high = 0
            elif f'({int(player.xcor())}.00,{int(player.ycor() + 40)}.00)' in position_list:
                high = 1
            else:
                high = 2
            
            # Go up for the x amount
            for jump in range(high):
                time.sleep(0.2)
                player.goto(player.xcor(), player.ycor() + 20)

            jumped = True




