import keyboard
import turtle
import time

build = turtle.Pen()
build.hideturtle()
build.speed(0)


# This part draws a square that is a block
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
    player = turtle.Pen()
    player.penup()
    player.goto(-10, 210)
    player.speed(0)
    player.shapesize(1)
    player.shape('square')
    player.color('red')
    player.showturtle()
    jumped = False
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

        # Moving right
        if keyboard.is_pressed('d'):
            if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in position_list:
                player.goto((player.xcor() + 20), player.ycor())
                time.sleep(0.2)
            watching = 'd'

        # Moving left
        if keyboard.is_pressed('a'):
            if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in position_list:
                player.goto((player.xcor() - 20), player.ycor())
                time.sleep(0.2)
            watching = 'a'

        if keyboard.is_pressed('w'):
            watching = 'w'

        if keyboard.is_pressed('s'):
            watching = 's'


        # Delete block
        if keyboard.is_pressed('F') and not inventory_full:
            if watching == 'w':
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() + 30)
                if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in position_list:
                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in leaf_list:
                        block_choice = leaf_col

                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in grass_list:
                        block_choice = 'green'

                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in dirt_list:
                        block_choice = 'SaddleBrown'

                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in stone_list:
                        block_choice = 'cornsilk4'

                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in sand_list:
                        block_choice = 'khaki3'

                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in diorite_list:
                        block_choice = 'gray80'

                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in snow_list:
                        block_choice = 'white'

                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in trunk_list:
                        block_choice = trunk_col

                    position_list.remove(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')
                    inventory_full = True
                    build.color('#3776AB')
                    block_draw()


            if watching == 'a':
                build.penup()
                build.goto(player.xcor() - 30, player.ycor() + 10)
                if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in position_list:

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in grass_list:
                        block_choice = 'green'

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in dirt_list:
                        block_choice = 'SaddleBrown'

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in stone_list:
                        block_choice = 'cornsilk4'

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in sand_list:
                        block_choice = 'khaki3'

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in diorite_list:
                        block_choice = 'gray80'

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in snow_list:
                        block_choice = 'white'

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in trunk_list:
                        block_choice = trunk_col

                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in leaf_list:
                        block_choice = leaf_col

                    position_list.remove(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')
                    inventory_full = True
                    build.color('#3776AB')
                    block_draw()



            if watching == 's':
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() - 10)
                if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in position_list:
                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in grass_list:
                        block_choice = 'green'

                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in dirt_list:
                        block_choice = 'SaddleBrown'

                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in stone_list:
                        block_choice = 'cornsilk4'

                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in sand_list:
                        block_choice = 'khaki3'

                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in diorite_list:
                        block_choice = 'gray80'

                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in snow_list:
                        block_choice = 'white'

                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in trunk_list:
                        block_choice = trunk_col

                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in leaf_list:
                        block_choice = leaf_col

                    position_list.remove(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')
                    inventory_full = True
                    build.color('#3776AB')
                    block_draw()



            if watching == 'd':
                build.penup()
                build.goto(player.xcor() + 10, player.ycor() + 10)
                if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in position_list:
                    if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in position_list:

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in grass_list:
                            block_choice = 'green'

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in dirt_list:
                            block_choice = 'SaddleBrown'

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in stone_list:
                            block_choice = 'cornsilk4'

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in sand_list:
                            block_choice = 'khaki3'

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in diorite_list:
                            block_choice = 'gray80'

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in snow_list:
                            block_choice = 'white'

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in trunk_list:
                            block_choice = trunk_col

                        if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in leaf_list:
                            block_choice = leaf_col

                    position_list.remove(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')
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

            if watching == 'w' and f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() + 30)
                position_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == 'green':
                    grass_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == 'SaddleBrown':
                    dirt_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == 'cornsilk4':
                    stone_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == 'khaki3':
                    sand_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == 'gray80':
                    diorite_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == 'white':
                    snow_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == trunk_col:
                    trunk_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                if block_choice == leaf_col:
                    leaf_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

                block_draw()
                inventory_full = False
                inventory.color('#8B8B8B')

            if watching == 'a' and f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 30, player.ycor() + 10)
                position_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'green':
                    grass_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'SaddleBrown':
                    dirt_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'cornsilk4':
                    stone_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'khaki3':
                    sand_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'gray80':
                    diorite_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'white':
                    snow_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == trunk_col:
                    trunk_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                if block_choice == leaf_col:
                    leaf_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

                block_draw()
                inventory_full = False
                inventory.color('#8B8B8B')

            if watching == 's' and f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() - 10)
                position_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == 'green':
                    grass_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == 'SaddleBrown':
                    dirt_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == 'cornsilk4':
                    stone_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == 'khaki3':
                    sand_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == 'gray80':
                    diorite_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == 'white':
                    snow_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == trunk_col:
                    trunk_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                if block_choice == leaf_col:
                    leaf_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

                block_draw()
                inventory_full = False
                inventory.color('#8B8B8B')

            if watching == 'd' and f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() + 10, player.ycor() + 10)
                position_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'green':
                    grass_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'SaddleBrown':
                    dirt_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'cornsilk4':
                    stone_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'khaki3':
                    sand_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'gray80':
                    diorite_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == 'white':
                    snow_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == trunk_col:
                    trunk_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                if block_choice == leaf_col:
                    leaf_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

                block_draw()
                inventory_full = False
                inventory.color('#8B8B8B')

        # Jumping
        if keyboard.is_pressed('space') and not jumped:
            time.sleep(0.1)
            if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in position_list:
                high = 0
            elif f'({int(player.xcor())}.00,{int(player.ycor() + 40)}.00)' in position_list:
                high = 1
            else:
                high = 2

            for jump in range(high):
                time.sleep(0.2)
                player.goto(player.xcor(), player.ycor() + 20)

            jumped = True




