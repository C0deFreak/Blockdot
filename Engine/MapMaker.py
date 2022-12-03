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


def tree():
    trunk_size = random.randint(1, 4)
    penup()
    setheading(90)
    forward((trunk_size * 20) + 40)
    right(90)
    fillcolor('forestgreen')
    block_draw()
    back(40)
    right(90)
    forward(20)
    left(90)
    for leafs in range(3):
        block_draw()
    back(40)
    right(90)
    forward(20)
    left(90)
    fillcolor('peru')
    for trunk in range(trunk_size):
        block_draw()
        right(90)
        forward(20)
        left(90)
        back(20)


pos_list = []
# Random Blocks in Stone Layers
SLR = ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', ' ', ' ', ' ', ' ', 'Di', 'Sa', 'D', 'S', 'S']

# Random Blocks in Dirt Layers
DLR = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',  ' ', ' ', ' ', ' ', 'Di', 'Sa', 'S']

# Random hills
G1_list = [' ', 'G', 'G', 'G']
G2_list = [' ', 'G']
G3_list = [' ']
G4_list = [' ', ' ']
G5_list = [' ', ' ', ' ']
tree_list = [' ', 'T', 'T', 'T']
tree_list2 = [' ']
tree_list3 = [' ']
tree_list4 = [' ']
tree_list5 = [' ']

G1 = random.choice(G1_list)
T1 = random.choice(tree_list)
if G1 == 'G':
    G2_list.append('G')
    tree_list2.append('T')
    T2 = ' '
    T3 = ' '
    T4 = ' '
    T5 = ' '

G2 = random.choice(G2_list)
T2 = random.choice(tree_list2)
if G2 == 'G':
    G3_list.append('G')
    tree_list3.append('T')
    T1 = 'G'
    T3 = ' '
    T4 = ' '
    T5 = ' '

G3 = random.choice(G3_list)
T3 = random.choice(tree_list3)
if G3 == 'G':
    G4_list.append('G')
    G1 = 'D'
    tree_list4.append('T')
    T1 = 'D'
    T2 = 'G'
    T4 = ' '
    T5 = ' '

G4 = random.choice(G4_list)
T4 = random.choice(tree_list4)
if G4 == 'G':
    G5_list.append('G')
    G2 = 'D'
    tree_list5.append('T')
    T1 = 'D'
    T2 = 'D'
    T3 = 'G'
    T5 = ' '


G5 = random.choice(G5_list)
T5 = random.choice(tree_list5)
if G5 == 'G':
    G3 = 'D'
    T1 = 'D'
    T2 = 'D'
    T3 = 'D'
    T4 = 'G'


# Terrain
map_list = [[' ', ' ', ' ', ' ', ' ', G5, T5, ' ', ' ', ' ', G5, G4, G4, G5, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', G5, G5, G5, ' ', ' ', ' ', ' ', ' ', G5, G4, G5, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', G5, G5, T3, G4, G5, ' ', G5, G4, G3, G3, G4, G4, G5, ' ', ' ', ' ', ' ', ' ', G5, T5, ' ', ' ', ' ', ' ', G5, G4, G4, G3, G3, G4, G5, G5, G4, G4, G3, G3, G3, T4, G5, G5, G5, ' ', G5, G4, G5, ' ', ' ', ' ', ' ', ' ', G5, G5, G4, G4, G4, G3, G4, T5, G5, ' ', ' ', ' ', G5, G4, G5, ' ', ' ', ' ', ' '],
            [T5, G5, G5, G4, G4, G3, G3, T2, G5, G4, G3, G2, G2, G3, G4, G4, G4, G5, T3, G5, G5, G4, G3, G4, G5, G5, G4, G3, G3, T3, G3, G2, G2, G3, G4, T2, G2, G2, G2, G2, G2, G3, G3, G4, G5, G4, G3, G4, G5, G5, G4, G3, G3, G3, G2, G2, G2, G2, G2, G3, G4, G5, G5, G4, G4, G3, G4, G5, ' ', ' ', ' ', ' '],
            [G3, G3, G3, G3, G3, G3, G2, G2, G2, G2, G1, G1, G1, G1, G1, G2, G2, G3, G2, G3, G3, T1, G2, G3, G4, G2, G2, G2, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G2, G3, G3, G2, G2, G3, G4, T1, G2, G2, G2, G2, G1, G1, G1, G1, G1, G1, G1, G2, G3, G3, G2, G2, G3, G4, G5, ' ', ' '],
            [T1, G1, G1, G1, G1, G1, G1, G1, G1, G1, random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, G1, random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), G1, G1, G1, G1, G1, G1, G1, G1, G1, G1],
            [random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR), random.choice(DLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)],
            [random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR), random.choice(SLR)]
            ]


def maker():
    # Sets up the scene
    bgcolor('#3776AB')
    setup(width=1.0, height=1.0)
    hideturtle()
    speed(0)
    setheading(0)
    pencolor('black')
    pensize(0)

    # Draws the block
    # Row
    for x in range(26):
        penup()
        goto(-700, (200 - (x * 20)))
        pendown()

        # Column
        for y in range(70):
            # Checks if the block is air or not
            air = False

            # Grass
            if map_list[x][y] == 'G':
                fillcolor('green')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)

            # Dirt
            if map_list[x][y] == 'D':
                fillcolor('SaddleBrown')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)

            # Stone
            elif map_list[x][y] == 'S':
                fillcolor('cornsilk4')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)

            # Diorite
            elif map_list[x][y] == 'Di':
                fillcolor('gray80')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)

            # Sand
            elif map_list[x][y] == 'Sa':
                fillcolor('khaki3')
                block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
                pos_list.append(block_pos)

            # Trees
            elif map_list[x][y] == 'T':
                tree()

            # Air
            elif map_list[x][y] == ' ':
                air = True
                penup()
                forward(20)
                pendown()

            # Skips this step if the block is air
            if not air:
                block_draw()


def map_blocks_pos():
    return pos_list
