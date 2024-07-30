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
biom_list = [[True, 'spring leaf', 'bark', True, 'grass', [[' ', 'X', ' '],
                                                           ['X', 'X', 'X'],
                                                           ['X', 'X', 'X'],]  ],  # SPRING

            [True, 'bark', 'bark', True, 'snow', [[' ', ' ', 'X'],
                                                  ['X', ' ', 'X'],
                                                  ['X', 'X', ' '],]],  # WINTER

            [True, 'summer leaf', 'bark', True, 'summer leaf', [[' ', 'X', ' '],
                                                                ['X', 'X', 'X'],
                                                                ['X', 'X', 'X'],]],  # SUMMER

            [True, 'fall leaf', 'bark', True, 'fall leaf', [[' ', 'X', ' '],
                                                             ['X', 'X', 'X'],
                                                             ['X', 'X', 'X'],]]]    # FALL

biom_choice = random.choice(biom_list)
main_block = biom_choice[4]
block_size = 20

block_dic = {'air' : '#3776AB',
             'diorite' : 'gray80',
             'sand' : 'khaki3',
             'dirt' : 'SaddleBrown',
             'stone' : 'cornsilk4',
             'summer leaf' : '#3D824C',
             'spring leaf' : '#3A8566',
             'fall leaf' : '#9C5522',
             'oak' : 'peru',
             'bark' : 'chocolate',
             'cactus' : 'darkgreen',
             'grass' : 'green',
             'snow' : 'white'}

# Lists of all of the blocks and their positions
block_list = []
pos_list = []
simple_list = []
xcor = 0
ycor = 0
width = 96
height = 48

# Random Blocks in Stone Layers and normal layers
RL = ['air']  + ['diorite'] * 5 + ['sand'] * 5 + ['dirt'] * 10 * 5 + [main_block] * 25 * 5 + ['stone'] * 25 * 5

# Terrain
map_list = [['PG'] * width for _ in range(5)] + [['RL'] * width] + [['SLR'] * width for _ in range(height - 6)]

# Sets up the scene                    
def sceneMaker():
    pygame.init()
    global window
    window = pygame.display.set_mode((1920, 1080))
    window.fill('#3776AB')
    

def simpleMaker():
    for y in range(height):
        simple_list.append([])
        for x in range(width):
            if y < 5:
                if y > 0 and simple_list[y - 1][x] == 'block':

                    simple_list[y].append('block')
                elif y > 0 and (x > 0 and map_list[y - 1][x - 1] == main_block) or (x < width - 1 and map_list[y - 1][x + 1] == main_block):
                    if random.randrange(1, 11) > 9:
                        simple_list[y].append('air')
                    else:
                        simple_list[y].append('block')
                else:
                    if random.randrange(1, 61) > 50:
                        simple_list[y].append('block')
                    else:
                        simple_list[y].append('air')
            else:       
                if random.randrange(1, 467) > 465:
                    simple_list[y].append('air')
                else:
                    simple_list[y].append('block')



def maker():
    global ycor
    global xcor
    block_color = 'air'
    # Set up te scene
    simpleMaker()
    print(simple_list)
    sceneMaker()

    # Draws the block
    # Column
    for y in range(height):
        xcor = block_size / 2
        ycor = 8 * block_size + (y * block_size)

        # Row
        for x in range(width):
            # Goes with the assumption that the block is not air
            air = False

            # Block coordinates
            #block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'

            # Check if the block is from SLR(Stone Layer Random) list and if it is asign the correct block to it
            if map_list[y][x] == 'SLR':
                air_amount = 2
                material_amount = 5
                if y < height - 1 and x < width - 1:
                    # Procedural generation for caves
                    # Make chance of air spawning big if it is touching another block and lower the block chances
                    if (map_list[y][x - 1] == 'air') or (map_list[y - 1][x] == 'air'):
                        air_amount = int(270 * 3.5)
                        material_amount = 1

                    # Stopping bloks from floating
                    if (map_list[y - 1][x] != 'air') and ('air' in map_list[y - 1][x:]) and ('air' in map_list[y - 1][:x]):
                        air_amount = 0

                SLR = ['air'] * air_amount  + ['diorite'] * material_amount + ['sand'] * material_amount + ['dirt'] * material_amount + ['stone'] * (material_amount * 90)
                map_list[y][x] = random.choice(SLR)
                
                      

            # Check if the block is from RL(Random Layer) list and if it is asign the correct block to it
            elif map_list[y][x] == 'RL':
                map_list[y][x] = random.choice(RL)

            # Procedural generation blocks
            elif map_list[y][x] == 'PG':

                # Chance of a block spawning
                block_chance = 10
                tree_chance = 5
                air_chance = 50
                spawn_chance_list = ['air'] * air_chance + ['T'] * tree_chance + [main_block] * block_chance
                cliff = [main_block] * 9 + ['air']
                
                # Spawns a block if there is one above it
                if map_list[y - 1][x] == main_block or map_list[y - 1][x] == 'T':
                    map_list[y][x] = main_block
                
                # Spawns a block right or left of the block that is spawned by the last function
                elif (x > 0 and map_list[y - 1][x - 1] == main_block) or (x < width - 1 and map_list[y - 1][x + 1] == main_block):
                    map_list[y][x] = random.choice(cliff)

                # If the block is should be spawned normally this gives it a chance of spawning
                else:
                    block_chance = 7 + (3 * y)
                    air_chance = 49 - (3 * y) 
                
                    # Choosing what block(air, tree, main block) should spawn
                    spawn_choice = random.choice(spawn_chance_list)

                    # Spawns trees by chance, biom, position. If the choice is not a tree it continiues as normal
                    if spawn_choice == 'T':
                        if biom_choice[3] == True:
                            if map_list[y - 1][x] != 'air':
                                map_list[y][x] = main_block
                            else:
                                map_list[y][x] = 'T'
                        else:
                            map_list[y][x] = 'air'
                    else:
                        map_list[y][x] = spawn_choice


            # Trees spawning and its properties
            if map_list[y][x] == 'T':
                tree(leaf=biom_choice[0], leaf_color=biom_choice[1], trunk_color=biom_choice[2], xpos=xcor, ypos=ycor, leaf_preset=biom_choice[5])

            # Append the collider(position) to normal blocks    
            elif map_list[y][x] != 'air':
                block_color = map_list[y][x]
                block_list.append(map_list[y][x])
                block_draw(xcor, ycor, block_color)
                #pos_list.append(block_pos)
            xcor += block_size

    pygame.display.update()

