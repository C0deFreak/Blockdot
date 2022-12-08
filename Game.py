from Engine import MapMaker
from Engine import Player

# Begins drawing the map
MapMaker.maker()

# List of positions that are occupied
pos_list = MapMaker.map_blocks_pos()
grass_list = MapMaker.map_blocks_grass()
dirt_list = MapMaker.map_blocks_dirt()
stone_list = MapMaker.map_blocks_stone()
sand_list = MapMaker.map_blocks_sand()
diorite_list = MapMaker.map_blocks_diorite()
snow_list = MapMaker.map_blocks_snow()
leaf_list = MapMaker.map_blocks_leaf()
trunk_list = MapMaker.map_blocks_trunk()
trunk_col = MapMaker.map_trunk_color()
leaf_col = MapMaker.map_leaf_color()

# Control player
Player.control(pos_list, grass_list, dirt_list, stone_list, sand_list, diorite_list, snow_list, leaf_list, trunk_list, trunk_col, leaf_col)
