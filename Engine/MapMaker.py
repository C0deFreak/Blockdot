from turtle import *
import random


def block_draw():
    pendown()
    begin_fill()
    for cube in range(4):
        forward(20)
        right(90)
    end_fill()

    forward(20)
    penup()


grass_list = []
dirt_list = []
stone_list = []
diorite_list = []
sand_list = []
snow_list = []
trunk_list = []
leaf_list = []


def tree(leaf, trunk_color, leaf_color):
    trunk_size = random.randint(1, 4)
    penup()
    setheading(90)
    forward(trunk_size * 20)

    if leaf:
        forward(40)
        right(90)
        fillcolor(leaf_color)
        block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
        leaf_list.append(block_pos)
        block_draw()
        back(40)
        right(90)
        forward(20)
        left(90)
        for leafs in range(3):
            block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
            leaf_list.append(block_pos)
            block_draw()
        back(40)
        right(90)
        forward(20)
        left(90)
    if not leaf:
        right(90)
        forward(20)

    fillcolor(trunk_color)
    block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
    trunk_list.append(block_pos)
    for trunk in range(trunk_size):
        block_draw()
        right(90)
        forward(20)
        left(90)
        back(20)
        block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
        trunk_list.append(block_pos)

IsG = 'G'
IsD = 'D'
IsS = 'S'
UbSa = 'Sa'
UbG = 'G'
UbA = ' '

trunk_col = ''
leaf_col = ''
bioms_list = ['grass', 'desert', 'rocky', 'snow']
biom_choice = random.choice(bioms_list)
if biom_choice == 'grass':
    main_block = 'G'
    second_block = 'D'
    rb = 'D'
    trees = True
    leaf_col = 'forestgreen'
    trunk_col = 'peru'

if biom_choice == 'desert':
    main_block = 'Sa'
    second_block = 'Sa'
    rb = 'Sa'
    trees = True
    trunk_col = 'darkgreen'
    IsG = 'Sa'

if biom_choice == 'rocky':
    main_block = 'S'
    second_block = 'S'
    rb = 'S'
    trees = False

if biom_choice == 'snow':
    main_block = 'Sn'
    second_block = 'Sn'
    rb = 'Sn'
    trees = True
    leaf_col = 'seagreen'
    trunk_col = 'chocolate'
    UbSa = 'Sn'
    IsG = 'Sn'


RL = [' ', ' ', ' ', ' ', 'Di', 'Sa', 'S', 'D'] + [rb] * 60

island = random.randint(0,1)
if island == 0:
 IsS, IsD, IsG = ' ', ' ', ' '
else:
    UbG, UbSa, UbA = 'S', 'S', 'S'

# Random hills
G1_list = [' ', main_block, main_block, main_block]
G2_list = [' ', main_block]
G3_list = [' ']
G4_list = [' ', ' ']
G5_list = [' ', ' ', ' ']
tree_list = [' ', 'T', 'T', 'T']
tree_list2 = [' ']
tree_list3 = [' ']
tree_list4 = [' ']
tree_list5 = [' ']

G1 = ' '
G2 = ' '
G3 = ' '
G4 = ' '
G5 = ' '

T1 = ' '
T2 = ' '
T3 = ' '
T4 = ' '
T5 = ' '

G1 = random.choice(G1_list)
T1 = random.choice(tree_list)
if G1 == main_block:
    G2_list.append(main_block)
    if trees:
        tree_list2.append('T')
    else:
        T1 = main_block

    G2 = random.choice(G2_list)
    T2 = random.choice(tree_list2)
    if G2 == main_block:
        G3_list.append(main_block)
        if trees:
            tree_list3.append('T')
            T1 = main_block
        else:
            T1 = main_block
            T2 = main_block

        G3 = random.choice(G3_list)
        T3 = random.choice(tree_list3)
        if G3 == main_block:
            G4_list.append(main_block)
            G1 = second_block
            if trees:
                tree_list4.append('T')
                T1 = second_block
                T2 = main_block
            else:
                T1 = second_block
                T2 = main_block
                T3 = main_block

            G4 = random.choice(G4_list)
            T4 = random.choice(tree_list4)
            if G4 == main_block:
                G5_list.append(main_block)
                G2 = second_block
                if trees:
                    tree_list5.append('T')
                    T1 = second_block
                    T2 = main_block
                    T3 = main_block
                else:
                    T1 = second_block
                    T2 = second_block
                    T3 = main_block
                    T4 = main_block

                G5 = random.choice(G5_list)
                T5 = random.choice(tree_list5)
                if G5 == main_block:
                    G3 = second_block
                    if trees:
                        T1 = second_block
                        T2 = second_block
                        T3 = main_block
                        T4 = main_block
                    else:
                        T1 = second_block
                        T2 = second_block
                        T3 = second_block
                        T4 = main_block
                        T5 = main_block


pos_list = []

# Random Blocks in Stone Layers
SLR = [ ' ', ' ', ' ', ' '] * 1 + ['Di'] + ['Sa'] + ['D'] + ['S'] * 90

# Terrain
map_list = [[' '] * 70] * 8 + [
            [' ', ' ', ' ', ' ', ' ', G5, T5, ' ', ' ', ' ', G5, G4, G4, G5, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', G5, G5, G5, ' ', ' ', ' ', ' ', ' ', G5, G4, G5, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', G5, G5, T3, G4, G5, ' ', G5, G4, G3, G3, G4, G4, G5, ' ', ' ', ' ', ' ', ' ', G5, T5, ' ', ' ', ' ', ' ', G5, G4, G4, G3, G3, G4, G5, G5, G4, G4, G3, G3, G3, T4, G5, G5, G5, ' ', G5, G4, G5, ' ', ' ', ' ', ' ', ' ', G5, G5, G4, G4, G4, G3, G4, T5, G5, ' ', ' ', ' ', G5, G4, G5, ' ', ' ', ' ', ' '],
            [T5, G5, G5, G4, G4, G3, G3, T2, G5, G4, G3, G2, G2, G3, G4, G4, G4, G5, T3, G5, G5, G4, G3, G4, G5, G5, G4, G3, G3, T3, G3, G2, G2, G3, G4, T2, G2, G2, G2, G2, G2, G3, G3, G4, G5, G4, G3, G4, G5, G5, G4, G3, G3, G3, G2, G2, G2, G2, G2, G3, G4, G5, G5, G4, G4, G3, G4, G5, ' ', ' ', ' ', ' '],
            [G3, G3, G3, G3, G3, G3, G2, G2, G2, G2, G1, G1, G1, G1, G1, G2, G2, G3, G2, G3, G3, T1, G2, G3, G4, G2, G2, G2, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G2, G3, G3, G2, G2, G3, G4, T1, G2, G2, G2, G2, G1, G1, G1, G1, G1, G1, G1, G2, G3, G3, G2, G2, G3, G4, G5, ' ', ' '],
            [T1, G1, G1, G1, G1, G1, G1, G1, G1, G1, random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), random.choice(RL), G1, G1, G1, G1, G1, G1, G1, G1, G1, G1],
            ['RL'] * 70,
            * [['SLR'] * 70 for _ in range(21)]]   
                    


def maker():
    # Sets up the scene
    bgcolor('#3776AB')
    setup(width=1.0, height=1.0)
    hideturtle()
    speed(0)
    setheading(0)

    penup()
    goto(-700, 340)
    pendown()
    color('#C6C6C6')
    begin_fill()
    for slot in range(4):
        fd(48)
        rt(90)
    end_fill()
    penup()
    goto(-699, 339)
    pencolor('black')
    fillcolor('#8B8B8B')
    pendown()
    begin_fill()
    for slot1 in range(4):
        fd(44)
        rt(90)
    end_fill()

    setheading(0)
    pencolor('black')
    pensize(0)

    # Draws the block
    # Column
    for x in range(34):
        penup()
        goto(-700, (280 - (x * 20)))
        pendown()

        # Row
        for y in range(70):
            # Checks if the block is air or not
            air = False

            # Check if the block is from SLR(Stone Layer Random) list and if it is asign the correct block to it
            if map_list[x][y] == 'SLR':
                map_list[x][y] =  random.choice(SLR)

            # Check if the block is from RL(Random Layer) list and if it is asign the correct block to it
            if map_list[x][y] == 'RL':
                map_list[x][y] =  random.choice(RL)

            # Grass
            if map_list[x][y] == 'G':
                fillcolor('green')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)
                grass_list.append(block_pos)

            # Dirt
            elif map_list[x][y] == 'D':
                fillcolor('SaddleBrown')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)
                dirt_list.append(block_pos)

            # Stone
            elif map_list[x][y] == 'S':
                fillcolor('cornsilk4')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)
                stone_list.append(block_pos)

            # Diorite
            elif map_list[x][y] == 'Di':
                fillcolor('gray80')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)
                diorite_list.append(block_pos)

            # Sand
            elif map_list[x][y] == 'Sa':
                fillcolor('khaki3')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)
                sand_list.append(block_pos)

            # Snow
            elif map_list[x][y] == 'Sn':
                fillcolor('white')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)
                snow_list.append(block_pos)

            # Trees
            elif map_list[x][y] == 'T':
                if biom_choice == 'grass':
                    tree(leaf=True, leaf_color='forestgreen', trunk_color='peru')

                if biom_choice == 'desert':
                    tree(leaf=False, leaf_color='forestgreen', trunk_color='darkgreen')

                if biom_choice == 'rocky':
                    tree(leaf=True, leaf_color='forestgreen', trunk_color='peru')

                if biom_choice == 'snow':
                    tree(leaf=True, leaf_color='seagreen', trunk_color='chocolate')

            # Air
            elif map_list[x][y] == ' ':
                air = True
                penup()
                forward(20)
                pendown()

            # Skips this step if the block is air
            if not air:
                block_draw()


