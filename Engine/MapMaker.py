from turtle import *

pos_list = []


def maker(map_list):
    # Sets up the scene
    bgcolor('#3776AB')
    setup(width=1.0, height=1.0)
    hideturtle()
    speed(0)
    setheading(0)
    pencolor('black')

    # Draws the block
    # Row
    for x in range(20):
        penup()
        goto(-735, (205 - (x * 21)))
        pendown()

        # Column
        for y in range(70):
            # Checks if the block is air or not
            air = False

            # Grass
            if map_list[x][y] == 'G':
                fillcolor('green')
                block_pos = f'({round((xcor() + 10), 0)}0,{round((ycor() - 10), 0)}0)'
                pos_list.append(block_pos)

            # Dirt
            if map_list[x][y] == 'D':
                fillcolor('SaddleBrown')
                block_pos = f'({round((xcor() + 10), 0)}0,{round((ycor() - 10), 0)}0)'
                pos_list.append(block_pos)

            # Stone
            elif map_list[x][y] == 'S':
                fillcolor('cornsilk4')
                block_pos = f'({round((xcor() + 10), 0)}0,{round((ycor() - 10), 0)}0)'
                pos_list.append(block_pos)

            elif map_list[x][y] == 'Di':
                fillcolor('gray80')
                block_pos = f'({round((xcor() + 10), 0)}0,{round((ycor() - 10), 0)}0)'
                pos_list.append(block_pos)

            elif map_list[x][y] == 'Sa':
                fillcolor('khaki3')
                block_pos = f'({round((xcor() + 10), 0)}0,{round((ycor() - 10), 0)}0)'
                pos_list.append(block_pos)

            # Air
            elif map_list[x][y] == ' ':
                air = True
                penup()
                forward(21)
                pendown()

            # Skips this step if the block is air
            if not air:
                begin_fill()
                for cube in range(4):
                    forward(21)
                    right(90)
                end_fill()

                forward(21)


def map_blocks_pos():
    return pos_list
