import random
import pygame

# Function that draws the blocks on the canvas
def block_draw(xPos, yPos, draw_color):
    global block_dic
    rect = pygame.Rect(0, 0, block_size, block_size)
    rect.center = (xPos, yPos)
    pygame.draw.rect(window, block_dic[draw_color], rect)
    

# Tree spawning function
def tree(leaf, trunk_color, leaf_color, xpos, ypos, leaf_preset):
    trunk_size = random.randint(1, 4)
    ypos -= ((trunk_size - 1) * block_size)
    
    # Makes the leaves of the tree
    if leaf:
        ypos -= len(leaf_preset) * block_size
        #block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
        xpos -= block_size * ((len(leaf_preset[0]) - 1) / 2)
        for row in leaf_preset:
            for leafs in row:
                if leafs == 'X':
                    #block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                    block_list.append(leaf_color)
                    #pos_list.append(block_pos)
                    block_draw(xpos, ypos, leaf_color)
                xpos += block_size
            xpos -= block_size * len(row)
            ypos += block_size

        xpos += block_size * ((len(leaf_preset[-1]) - 1) / 2)


    # Makes the truk of the tree
    #block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
    block_list.append(trunk_color)
    #pos_list.append(block_pos)
    for trunk in range(trunk_size):
        block_draw(xpos, ypos, trunk_color)
        block_list.append(trunk_color)
        ypos += block_size
        #block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'

        #pos_list.append(block_pos)


# Makes the bioms and chooses the properties for them
# Options: leaf spawning, leaf color, trunk color, tree spawning, main block, 
biom_list = [[True, 'leaf', 'oak', True, 'grass', [[' ', 'X', ' '],
                                                  ['X', 'X', 'X']]  ],  # GRASS

            [True, 'dark leaf', 'dark oak', True, 'snow', [[' ',' ', 'X', ' ', ' '],
                                                          [' ', 'X', 'X', 'X', ' '],
                                                          ['X','X', 'X', 'X', 'X'],]],  # SNOW

            [False, None, 'cactus', True, 'sand', None],  # DESERT

            [True, 'leaf', 'oak', False, 'stone', None]]    # ROCKY

biom_choice = random.choice(biom_list)
main_block = biom_choice[4]
block_size = 30

block_dic = {'air' : '#3776AB',
             'diorite' : 'gray80',
             'sand' : 'khaki3',
             'dirt' : 'SaddleBrown',
             'stone' : 'cornsilk4',
             'leaf' : 'forestgreen',
             'dark leaf' : 'seagreen',
             'oak' : 'peru',
             'dark oak' : 'chocolate',
             'cactus' : 'darkgreen',
             'grass' : 'green',
             'snow' : 'white'}

# Lists of all of the blocks and their positions
block_list = []
pos_list = []
xcor = 0
ycor = 0
width = 64

# Random Blocks in Stone Layers and normal layers
RL = ['air']  + ['diorite'] * 5 + ['sand'] * 5 + ['dirt'] * 10 * 5 + [main_block] * 25 * 5 + ['stone'] * 25 * 5

# Terrain
map_list = [['PG'] * width for _ in range(5)] + [['RL'] * width] + [['SLR'] * width for _ in range(21)]

# Sets up the scene                    
def sceneMaker():
    pygame.init()
    global window
    window = pygame.display.set_mode((1920, 1080))
    window.fill('#3776AB')
    
    '''
    goto(-700, 340)
    # Draw the border inventory
    color('#C6C6C6')
    begin_fill()
    for _ in range(4):
        fd(48)
        rt(90)
    end_fill()

    # Draw the background inventory
    pencolor('black')
    fillcolor('#8B8B8B')
    begin_fill()
    for _ in range(4):
        fd(44)
        rt(90)
    end_fill()
    '''
def maker():
    global ycor
    global xcor
    block_color = 'air'
    # Set up te scene
    sceneMaker()

    # Draws the block
    # Column
    for x in range(27):
        xcor = block_size / 2
        ycor = 8 * block_size + (x * block_size)

        # Row
        for y in range(width):
            # Goes with the assumption that the block is not air
            air = False

            # Block coordinates
            #block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'

            # Check if the block is from SLR(Stone Layer Random) list and if it is asign the correct block to it
            if map_list[x][y] == 'SLR':
                air_amount = 2
                material_amount = 5
                if x < 26 and y < width - 1:
                    # Procedural generation for caves
                    # Make chance of air spawning big if it is touching another block and lower the block chances
                    if (map_list[x][y - 1] == 'air') or (map_list[x - 1][y] == 'air'):
                        air_amount = int(270 * 3.5)
                        material_amount = 1

                    # Stopping bloks from floating
                    if (map_list[x - 1][y] != 'air') and ('air' in map_list[x - 1][y:]) and ('air' in map_list[x - 1][:y]):
                        air_amount = 0

                SLR = ['air'] * air_amount  + ['diorite'] * material_amount + ['sand'] * material_amount + ['dirt'] * material_amount + ['stone'] * (material_amount * 90)
                map_list[x][y] = random.choice(SLR)
                
                      

            # Check if the block is from RL(Random Layer) list and if it is asign the correct block to it
            elif map_list[x][y] == 'RL':
                map_list[x][y] = random.choice(RL)

            # Procedural generation blocks
            elif map_list[x][y] == 'PG':

                # Chance of a block spawning
                block_chance = 7
                tree_chance = 5
                air_chance = 49
                spawn_chance_list = ['air'] * air_chance + ['T'] * tree_chance + [main_block] * block_chance
                cliff = [main_block] * 9 + ['air']
                
                # Spawns a block if there is one above it
                if map_list[x - 1][y] == main_block or map_list[x - 1][y] == 'T':
                    map_list[x][y] = main_block
                
                # Spawns a block right or left of the block that is spawned by the last function
                elif (y > 0 and map_list[x - 1][y - 1] == main_block) or (y < width - 1 and map_list[x - 1][y + 1] == main_block):
                    map_list[x][y] = random.choice(cliff)

                # If the block is should be spawned normally this gives it a chance of spawning
                else:
                    block_chance = 7 + (3 * x)
                    air_chance = 49 - (3 * x) 
                
                    # Choosing what block(air, tree, main block) should spawn
                    spawn_choice = random.choice(spawn_chance_list)

                    # Spawns trees by chance, biom, position. If the choice is not a tree it continiues as normal
                    if spawn_choice == 'T':
                        if biom_choice[3] == True:
                            if map_list[x - 1][y] != 'air':
                                map_list[x][y] = main_block
                            else:
                                map_list[x][y] = 'T'
                        else:
                            map_list[x][y] = 'air'
                    else:
                        map_list[x][y] = spawn_choice


            # Trees spawning and its properties
            if map_list[x][y] == 'T':
                tree(leaf=biom_choice[0], leaf_color=biom_choice[1], trunk_color=biom_choice[2], xpos=xcor, ypos=ycor, leaf_preset=biom_choice[5])

            # Append the collider(position) to normal blocks    
            elif map_list[x][y] != 'air':
                block_color = map_list[x][y]
                block_list.append(map_list[x][y])
                block_draw(xcor, ycor, block_color)
                #pos_list.append(block_pos)
            xcor += block_size

    pygame.display.update()

