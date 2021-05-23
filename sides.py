from group import Group
from path import Path
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def add_horizontal_side(root, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = DIVIDER_HEIGHT
    side = Group("horizontal_side")
    root.groups.append(side)

    p = Path("horizontal_side_outline", True)
    p.color = constants.MAGENTA
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, -PIN_OUT_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, PIN_OUT_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    add_horz_pins(p, p.last_x() + (GRID_PART_WIDTH / 2) + THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, PIN_OUT_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, -PIN_OUT_WIDTH, PIN_SIZE, -1)

    lines = Group("indicatorlines_horizontal_side")
    side.groups.append(lines)

    for xx in range(1, GRID_W):
        x = xx * (GRID_PART_WIDTH + THICKNESS) - THICKNESS
        y = 0 + extra_offset_y
        y2 = DIVIDER_HEIGHT + extra_offset_y
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_a_{xx}")
        lines.add_path(l)
        x += THICKNESS
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_b_{xx}")
        lines.add_path(l)

def add_vertical_side(root, extra_offset_y:int = 0):
    width = VERTICAL_DIVIDER_LENGTH + (2 * THICKNESS)
    height = DIVIDER_HEIGHT
    side = Group("vertical_side")
    root.groups.append(side)

    p = Path("vertical_side_outline", True)
    p.color = constants.MAGENTA
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    add_horz_pins(p, p.last_x() - (GRID_PART_HEIGHT / 2), p.last_y(), GRID_H, GRID_PART_HEIGHT + THICKNESS, -PIN_OUT_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, -PIN_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    add_horz_pins(p, p.last_x() + (GRID_PART_HEIGHT / 2), p.last_y(), GRID_H, GRID_PART_HEIGHT + THICKNESS, PIN_OUT_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, PIN_WIDTH, PIN_SIZE, -1)

    lines = Group("indicatorlines_vertical_side")
    side.groups.append(lines)

    for xx in range(1, GRID_H):
        x = xx * (GRID_PART_HEIGHT + THICKNESS)
        y = 0 + extra_offset_y
        y2 = DIVIDER_HEIGHT + extra_offset_y
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_a_{xx}")
        lines.add_path(l)
        x += THICKNESS
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_b_{xx}")
        lines.add_path(l)


def generate_sides(root):
    spacing = BOX_INNER_DEPTH + 10
    add_vertical_side(root)
    add_vertical_side(root, spacing * 1)
    add_horizontal_side(root, spacing * 2)
    add_horizontal_side(root, spacing * 3)

