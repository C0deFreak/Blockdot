import keyboard
import turtle
import time

build = turtle.Pen()
build.hideturtle()
build.speed(0)


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
    block_choice = 'SaddleBrown'
    corrupt = []

    while True:
        position_list.sort()
        corrupt.sort()

        # Restart Jump
        if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in position_list:
            jumped = False

        # Gravity
        if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' not in position_list:
            time.sleep(0.2)
            player.goto(player.xcor(), player.ycor() - 20)
            jumped = True

        # Corrupt Portal
        if position_list == corrupt:
            turtle.clear()
            build.clear()

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

        # Choose block
        if keyboard.is_pressed('ctrl'):
            if watching == 'w':
                if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in position_list:
                    if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in leaf_list:
                        block_choice = 'black'

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

            if watching == 'a':
                if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in position_list:
                    if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in corrupt:
                        block_choice = 'black'

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

            if watching == 's':
                if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in position_list:
                    if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in corrupt:
                        block_choice = 'black'

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

            if watching == 'd':
                if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in position_list:
                    if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in corrupt:
                        block_choice = 'black'

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

        # Delete block
        if keyboard.is_pressed('delete'):
            if watching == 'w':
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() + 30)
                if f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')

            if watching == 'a':
                build.penup()
                build.goto(player.xcor() - 30, player.ycor() + 10)
                if f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')

            if watching == 's':
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() - 10)
                if f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')

            if watching == 'd':
                build.penup()
                build.goto(player.xcor() + 10, player.ycor() + 10)
                if f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' in position_list:
                    position_list.remove(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')

            build.color('#3776AB')
            block_draw()

        # Build
        if keyboard.is_pressed('enter'):
            build.fillcolor(block_choice)
            build.pencolor('black')

            if watching == 'w' and f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() + 30)
                position_list.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')
                corrupt.append(f'({int(player.xcor())}.00,{int(player.ycor() + 20)}.00)')
                block_draw()

            if watching == 'a' and f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 30, player.ycor() + 10)
                position_list.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')
                corrupt.append(f'({int(player.xcor() - 20)}.00,{int(player.ycor())}.00)')
                block_draw()

            if watching == 's' and f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() - 10, player.ycor() - 10)
                position_list.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')
                corrupt.append(f'({int(player.xcor())}.00,{int(player.ycor() - 20)}.00)')
                block_draw()

            if watching == 'd' and f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)' not in position_list:
                build.penup()
                build.goto(player.xcor() + 10, player.ycor() + 10)
                position_list.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')
                corrupt.append(f'({int(player.xcor() + 20)}.00,{int(player.ycor())}.00)')
                block_draw()

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




