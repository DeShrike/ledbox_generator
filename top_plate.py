from group import Group
from path import Path
from helpers import *
from config  import *
import constants
from bottom_plate import add_outline, add_indicator_lines, add_side_pin_holes
from bottom_plate import add_center_horizontal_pin_holes, add_center_vertical_pin_holes

OFFSETX = 10
OFFSETY = 10

def create_hole(x1:int, y1:int, w:int, h:int, id:str):
    p = Path(id, True)
    p.color = constants.GREEN
    p.add_node(x1, y1)
    p.add_node(x1 + w, y1)
    p.add_node(x1 + w, y1 + h)
    p.add_node(x1, y1 + h)
    return p

def generate_top_plate(root):
    add_outline(root)
    add_indicator_lines(root)
    add_side_pin_holes(root)
    add_center_horizontal_pin_holes(root)
    add_center_vertical_pin_holes(root)

    bholes = Group("big_holes")
    root.groups.append(bholes)

    holew = GRID_PART_WIDTH - (2 * LIP_WIDTH)
    holeh = GRID_PART_HEIGHT - (2 * LIP_WIDTH)
    for xx in range(GRID_W):
        for yy in range(GRID_H):
            x = (xx * (GRID_PART_WIDTH + THICKNESS)) + LIP_WIDTH + THICKNESS + LIP_WIDTH
            y = (yy * (GRID_PART_HEIGHT + THICKNESS)) + LIP_WIDTH + THICKNESS + LIP_WIDTH
            hole = create_hole(OFFSETX + x, OFFSETY + y, holew, holeh, f"bhole_{x}_{y}")
            bholes.add_path(hole)
