import keyboard
import turtle
import time
from Engine import MapMaker
import sys

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


def control():

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
    build.penup()

    while True:

        # Exit the program
        if keyboard.is_pressed('esc'):
            sys.exit(0)

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




