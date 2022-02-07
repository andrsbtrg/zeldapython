from csv import reader
from os import walk
import pygame

import pygame

def import_csv_layout(path):
    """[summary]

    Args:
        path ([type]): [description]

    Returns:
        [type]: [description]
    """
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    """[summary]

    Args:
        path ([type]): [description]

    """
    surface_list = []

    for _,__,img_files in walk(path): # walk returns ('../graphics/Grass', [], ['grass_1.png', 'grass_2.png', 'grass_3.png'])
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list