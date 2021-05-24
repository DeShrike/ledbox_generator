from group import Group
from path import Path
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10
FLIPXY = True

f1 = (0, 0)
f2 = (0, 0)
f3 = (0, 0)
f4 = (0, 0)

def add_back(root, extra_offset_x:int = 0, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = FOOT_HEIGHT
    side = Group("back_side")
    root.groups.append(side)

    p = Path("back_side_outline", True)
    p.move((extra_offset_x, extra_offset_y))
    p.flip_xy = FLIPXY
    p.color = constants.MAGENTA
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, -PIN_OUT_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0)
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, PIN_OUT_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height)
    add_horz_pins(p, p.last_x() + (GRID_PART_WIDTH / 2) + THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, PIN_OUT_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, -PIN_OUT_WIDTH, PIN_SIZE, -1)

def add_horizontal_side(root, extra_offset_x:int = 0, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = DIVIDER_HEIGHT
    side = Group("horizontal_side")
    root.groups.append(side)

    p = Path("horizontal_side_outline", True)
    p.move((extra_offset_x, extra_offset_y))
    p.flip_xy = FLIPXY
    p.color = constants.MAGENTA
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, -PIN_OUT_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0)
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, PIN_OUT_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height)
    add_horz_pins(p, p.last_x() + (GRID_PART_WIDTH / 2) + THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, PIN_OUT_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, -PIN_OUT_WIDTH, PIN_SIZE, -1)

    lines = Group("indicatorlines_horizontal_side")
    side.groups.append(lines)

    for xx in range(1, GRID_W):
        x = xx * (GRID_PART_WIDTH + THICKNESS) - THICKNESS
        y = 0
        y2 = DIVIDER_HEIGHT
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_a_{xx}")
        l.move((extra_offset_x, extra_offset_y))
        l.flip_xy = FLIPXY
        lines.add_path(l)
        x += THICKNESS
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_b_{xx}")
        l.move((extra_offset_x, extra_offset_y))
        l.flip_xy = FLIPXY
        lines.add_path(l)

def add_vertical_side(root, extra_offset_x:int = 0, extra_offset_y:int = 0):
    global f1, f2, f3, f4
    width = VERTICAL_DIVIDER_LENGTH + (2 * THICKNESS)
    height = DIVIDER_HEIGHT
    side = Group("vertical_side")
    root.groups.append(side)

    p = Path("vertical_side_outline", True)
    p.move((extra_offset_x, extra_offset_y))
    p.flip_xy = FLIPXY
    p.color = constants.MAGENTA
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0)
    pincount = GRID_H if not ADD_FOOT else GRID_H - 2
    add_horz_pins(p, p.last_x() - (GRID_PART_HEIGHT / 2), p.last_y(), pincount, GRID_PART_HEIGHT + THICKNESS, -PIN_OUT_WIDTH, PIN_SIZE, 1)

    # top right
    if ADD_FOOT:
        cx = OFFSETX + width - FOOT_HEIGHT
        cy = OFFSETY + 0
        f1 = (cx, cy)
        p.add_node(cx, cy)

        px = OFFSETX + width - FOOT_HEIGHT
        py = OFFSETY + 0 - FOOT_SIZE
        rotated = rotate_point(cx, cy, px, py, -FOOT_ANGLE)
        px = rotated[0]
        py = rotated[1]
        cx = OFFSETX + width
        cy = OFFSETY + 0 - FOOT_SIZE
        rotated = rotate_point(cx, cy, px, py, -FOOT_ANGLE)

        f2 = (rotated[0], rotated[1])
        p.add_node(rotated[0], rotated[1])

        cx = OFFSETX + width
        cy = OFFSETY + 0
        px = OFFSETX + width
        py = OFFSETY + 0 - FOOT_SIZE
        rotated = rotate_point(cx, cy, px, py, -FOOT_ANGLE)

        f3 = (rotated[0], rotated[1])
        p.add_node(rotated[0], rotated[1])

        f4 = (cx, cy)
        p.add_node(cx, cy)
    else:
        p.add_node(OFFSETX + width, OFFSETY + 0)
    
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, -PIN_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height)
    add_horz_pins(p, p.last_x() + (GRID_PART_HEIGHT / 2), p.last_y(), GRID_H, GRID_PART_HEIGHT + THICKNESS, PIN_OUT_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, PIN_WIDTH, PIN_SIZE, -1)

    lines = Group("indicatorlines_vertical_side")
    side.groups.append(lines)

    for xx in range(1, GRID_H):
        x = xx * (GRID_PART_HEIGHT + THICKNESS)
        y = 0
        y2 = DIVIDER_HEIGHT
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_a_{xx}")
        l.move((extra_offset_x, extra_offset_y))
        l.flip_xy = FLIPXY
        lines.add_path(l)
        x += THICKNESS
        l = create_line(OFFSETY + x, OFFSETY + y, OFFSETX + x, OFFSETY + y2, f"line_b_{xx}")
        l.move((extra_offset_x, extra_offset_y))
        l.flip_xy = FLIPXY
        lines.add_path(l)


def generate_sides(root):
    spacing = BOX_INNER_DEPTH + 10
    add_horizontal_side(root, 0, spacing * 0)
    add_horizontal_side(root, 0, spacing * 1)
    add_vertical_side(root, 0, spacing * 3.5)
    add_vertical_side(root, spacing * 1.5, spacing * 4.5)
    if ADD_FOOT:
        add_back(root, 0, spacing * 2)
