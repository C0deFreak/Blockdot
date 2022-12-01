from Engine import MapMaker
from Engine import Player

# Begins drawing the map
MapMaker.maker()

# List of positions that are occupied
pos_list = MapMaker.map_blocks_pos()

# Control player
Player.control(position_list=pos_list)
