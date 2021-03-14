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

def add_long_side(root, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH + (2 * THICKNESS)
    height = DIVIDER_HEIGHT
    side = Group("long_side")
    root.groups.append(side)

    p = Path("side", True)
    p.color = constants.RED
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2), p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, -PIN_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, -PIN_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    add_horz_pins(p, p.last_x() + (GRID_PART_WIDTH / 2), p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, PIN_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, PIN_WIDTH, PIN_SIZE, -1)

    lines = Group("indicatorlines")
    side.groups.append(lines)

    for xx in range(1, GRID_W):
        x = xx * (GRID_PART_WIDTH + THICKNESS)
        y = 0 + extra_offset_y
        y2 = DIVIDER_HEIGHT + extra_offset_y
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_a_{xx}")
        lines.add_path(l)
        x += THICKNESS
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_b_{xx}")
        lines.add_path(l)

def add_long_divider(root, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = DIVIDER_HEIGHT
    div = Group("divider")
    root.groups.append(div)

    p = Path("div", True)
    p.color = constants.RED
    div.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, -PIN_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    data = [ (PIN_WIDTH, PIN_SIZE) ] * GRID_W
    data[0] = (-WIRE_DIP_WIDTH, WIRE_DIP_SIZE)
    data[-1] = (-WIRE_DIP_WIDTH, WIRE_DIP_SIZE)
    slid_data = (-SLID_DEPTH, SLID_WIDTH)
    add_horz_pins_ex(p, p.last_x() + (GRID_PART_WIDTH / 2) + THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, data, -1, slid_data)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)

def generate_long_sides(root):
    spacing = BOX_INNER_DEPTH + 10
    add_long_side(root)
    add_long_side(root, spacing * 1)
    add_long_divider(root, spacing * 2)
    add_long_divider(root, spacing * 3)
