from group import Group
from path import Path
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def add_horizontal_divider(root, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = DIVIDER_HEIGHT
    div = Group(f"horizontal_divider_{extra_offset_y}")
    root.groups.append(div)

    p = Path(f"hor_div_outline_", True)
    p.color = constants.MAGENTA
    div.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, -PIN_OUT_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y(), 1, height / 2, -WIRE_DIP_WIDTH, WIRE_DIP_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    data = [ (PIN_OUT_WIDTH, PIN_SIZE) ] * GRID_W
    #data[0] = (-WIRE_DIP_WIDTH, WIRE_DIP_SIZE)
    #data[-1] = (-WIRE_DIP_WIDTH, WIRE_DIP_SIZE)
    slid_data = (-SLID_DEPTH, SLID_WIDTH)
    add_horz_pins_ex(p, p.last_x() + (GRID_PART_WIDTH / 2) + THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, data, -1, slid_data)

    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y(), 1, height / 2, WIRE_DIP_WIDTH, WIRE_DIP_SIZE, -1)

def generate_horizontal_dividers(root):
    spacing = BOX_INNER_DEPTH + (PIN_OUT_WIDTH * 3)
    for i in range(HORIZONTAL_DIVIDER_COUNT):
        add_horizontal_divider(root, spacing * i)
