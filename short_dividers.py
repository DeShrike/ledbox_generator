from group import Group
from path import Path
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def add_horz_pins_ex(path, x:float, y:float, count:int, spacing:float, data, direction:int, slid_data = None):
    # adds pins on a horizontal line
    # x, y: start point
    # count: numbers of pins
    # spacing: distance between stub centers
    # indent: size of pin (depth)
    # thickness: thickness of pin (width)
    # direction: 1 or -1: x-direction
    for ix in range(count):
        indent = data[ix][0]
        thickness = data[ix][1]

        if slid_data is not None and ix > 0:
            slid_width = slid_data[1]
            slid_depth = slid_data[0]
            dx = spacing / 2
            sx = x + ((dx - (slid_width / 2)) * direction)
            path.add_node(sx, y)
            y += slid_depth
            path.add_node(sx, y)
            sx += slid_width * direction
            path.add_node(sx, y)
            y -= slid_depth
            path.add_node(sx, y)

        x += (spacing - (thickness / 2.0)) * direction
        path.add_node(x, y)
        y += indent
        path.add_node(x, y)
        x += thickness * direction
        path.add_node(x, y)
        y -= indent
        path.add_node(x, y)
        x -= (thickness / 2.0) * direction


def add_short_divider(root, extra_offset_y:int = 0):
    width = VERTICAL_DIVIDER_LENGTH
    height = DIVIDER_HEIGHT
    div = Group("divider")
    root.groups.append(div)

    p = Path("div", True)
    p.flip_xy = True
    p.color = constants.MAGENTA
    div.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    data = [ (-PIN_WIDTH, PIN_SIZE) ] * GRID_H
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
        add_short_divider(root, spacing * i)
