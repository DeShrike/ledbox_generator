from group import Group
from path import Path
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def add_vertical_divider(root, extra_offset_y:int = 0):
    width = VERTICAL_DIVIDER_LENGTH
    height = DIVIDER_HEIGHT
    div = Group(f"vertical_divider_{extra_offset_y}")
    root.groups.append(div)

    p = Path("vert_div_outline", True)
    p.flip_xy = True
    p.color = constants.MAGENTA
    div.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    data = [ (-PIN_OUT_WIDTH, PIN_SIZE) ] * GRID_H
    slid_data = (SLID_DEPTH, SLID_WIDTH)
    add_horz_pins_ex(p, p.last_x() - (GRID_PART_HEIGHT / 2) - THICKNESS, p.last_y(), GRID_H, GRID_PART_HEIGHT + THICKNESS, data, 1, slid_data)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    data = [ (-WIRE_DIP_WIDTH, WIRE_DIP_SIZE) ] * GRID_H
    add_horz_pins_ex(p, p.last_x() + (GRID_PART_HEIGHT / 2) + THICKNESS, p.last_y(), GRID_H, GRID_PART_HEIGHT + THICKNESS, data, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)

def generate_vertical_dividers(root):
    spacing = BOX_INNER_DEPTH + 4
    for i in range(VERTICAL_DIVIDER_COUNT):
        add_vertical_divider(root, spacing * i)
