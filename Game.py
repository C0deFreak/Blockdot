from Engine import MapMaker
from Engine import Player

# Begins drawing the map
MapMaker.maker()


# Control player
Player.control(MapMaker.pos_list, MapMaker.grass_list, MapMaker.dirt_list, MapMaker.stone_list, MapMaker.sand_list, MapMaker.diorite_list, MapMaker.snow_list, MapMaker.leaf_list, MapMaker.trunk_list, MapMaker.biom_choice[2], MapMaker.biom_choice[1])