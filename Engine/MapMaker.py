import random
import pygame


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
grass_layer = 2


def position_map(x=xcor, y=ycor, xOffset=0, yOffset=0):
    if (int(x + xOffset), int(y + yOffset)) not in pos_list:
        pos_list.append((int(x + xOffset), int(y + yOffset)))

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
        xpos -= block_size * ((len(leaf_preset[0]) - 1) / 2)
        for row in leaf_preset:
            for leafs in row:
                if leafs == 'X':
                    block_list.append(leaf_color)
                    block_draw(xpos, ypos, leaf_color)
                    position_map(x=xpos, y=ypos)
                xpos += block_size
            xpos -= block_size * len(row)
            ypos += block_size

        xpos += block_size * ((len(leaf_preset[-1]) - 1) / 2)

    # Makes the truk of the tree
    block_list.append(trunk_color)
    for trunk in range(trunk_size):
        block_draw(xpos, ypos, trunk_color)
        position_map(x=xpos, y=ypos)
        block_list.append(trunk_color)
        ypos += block_size


# Sets up the scene                    
def sceneMaker():
    pygame.init()
    global window
    window = pygame.display.set_mode((1920, 1080))
    window.fill('#3776AB')
    pygame.display.set_caption("Pycraft")
    

def simpleMaker():
    for y in range(height):
        simple_list.append([])
        for x in range(width):
            if y < 5:
                if y > 0 and simple_list[y - 1][x] == 'block':
                    simple_list[y].append('block')
                elif y > 0 and ((x > 0 and simple_list[y - 1][x - 1] == 'block') or (x < width - 1 and simple_list[y - 1][x + 1] == 'block')):
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
    sceneMaker()

    # Draws the block
    # Column
    for y in range(height):
        xcor = 0
        ycor = 8 * block_size + (y * block_size)
        # Row
        for x in range(width):

            # Procedural generation blocks
            if y < 6 and (y - 2 < 0 or simple_list[y - 2][x] == 'air'):
                if simple_list[y][x] == 'block':
                    spawn_chance_list = ['T'] * 1 + [main_block] * 10
                    if random.choice(spawn_chance_list) == 'T' and (y == 0 or simple_list[y - 1][x] == 'air'):
                        simple_list[y][x] = 'T'
                    else:
                        try:
                            if simple_list[y - 1][x] == 'air':
                                position_map(x=xcor, y=ycor)
                            elif simple_list[y][x - 1] == 'air':
                                position_map(x=xcor, y=ycor)
                            elif simple_list[y][x + 1] == 'air':
                                position_map(x=xcor, y=ycor)
                        except:
                            position_map(x=xcor, y=ycor)

                        simple_list[y][x] = main_block
                        

            else:
                air_amount = 2
                material_amount = 5
                if y < height - 1 and 0 < x < width - 1:
                    # Procedural generation for caves
                    # Make chance of air spawning big if it is touching another block and lower the block chances
                    if simple_list[y][x - 1] == 'air' or simple_list[y - 1][x] == 'air' or simple_list[y][x + 1] == 'air' or simple_list[y + 1][x] == 'air':
                        air_amount = int(270 * 3.5)
                        material_amount = 1

                    # Stopping bloks from floating
                    if (simple_list[y - 1][x] != 'air') and ('air' in simple_list[y - 1][x:]) and ('air' in simple_list[y - 1][:x]):
                        air_amount = 0
                    
                    if simple_list[y - 2][x] == 'air' and simple_list[y - 2][x - 1] != 'air' and simple_list[y - 2][x + 1] != 'air':
                        air_amount = 10
                else:
                    position_map(x=xcor, y=ycor)

                if simple_list[y][x] == 'block':
                    SLR = ['air'] * air_amount  + ['diorite'] * material_amount + ['sand'] * material_amount + ['dirt'] * material_amount + ['stone'] * (material_amount * 90)
                    simple_list[y][x] = random.choice(SLR)
                
                if (y < height - 1 and 0 < x < width - 1):
                    if simple_list[y][x] == 'air':
                        if simple_list[y - 1][x] != 'air':
                            position_map(yOffset=-block_size, x=xcor, y=ycor)
                        elif simple_list[y][x - 1] != 'air':
                            position_map(xOffset=-block_size, x=xcor, y=ycor)
                    else:
                        if simple_list[y - 1][x] == 'air':
                            position_map( x=xcor, y=ycor)
                        elif simple_list[y][x - 1] == 'air':
                            position_map(x=xcor, y=ycor)
                        elif simple_list[y][x + 1] == 'air':
                            position_map(x=xcor, y=ycor)

            # Trees spawning and its properties
            if simple_list[y][x] == 'T':
                tree(leaf=biom_choice[0], leaf_color=biom_choice[1], trunk_color=biom_choice[2], xpos=xcor, ypos=ycor, leaf_preset=biom_choice[5])

            # Append the collider(position) to normal blocks    
            elif simple_list[y][x] != 'air':
                block_color = simple_list[y][x]
                block_list.append(simple_list[y][x])
                block_draw(xcor, ycor, block_color)
                #pos_list.append(block_pos)
            xcor += block_size

    pygame.display.update()
    '''
    pygame.time.delay(5000)
    for pos in pos_list:
        block_draw(pos[0], pos[1], 'grass')
    '''

