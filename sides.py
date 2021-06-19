from group import Group
from path import Path
from helpers import *
from config  import * 
import constants
from itertools import product

OFFSETX = 10
OFFSETY = 10
FLIPXY = True

f1 = (0, 0)
f2 = (0, 0)
f3 = (0, 0)
f4 = (0, 0)

rf1 = (0, 0)
rf2 = (0, 0)
rf3 = (0, 0)
rf4 = (0, 0)

def add_foot_bottom(root, extra_offset_x:int = 0, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = distance(rf3, rf4)
    bottom = Group("foot_bottom")
    root.groups.append(bottom)

    p = Path("foot_bottom_outline", True)
    p.move((extra_offset_x, extra_offset_y))
    p.flip_xy = FLIPXY
    p.color = constants.MAGENTA
    bottom.add_path(p)

    p.add_node(OFFSETX + 0,     OFFSETY + 0)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, PIN_OUT_WIDTH, PIN_SIZE, 1)

    p.add_node(OFFSETX + width, OFFSETY + 0)

    d = distance(f3, f4)
    pincount = int((d - PIN_SIZE) / (2 * PIN_SIZE))
    spacing = d / pincount
    o = spacing / 2
    add_vert_pins(p, p.last_x(), p.last_y() - o, pincount, spacing, PIN_OUT_WIDTH, PIN_SIZE, 1)

    p.add_node(OFFSETX + width, OFFSETY + height)
    
    p.add_node(OFFSETX + 0,     OFFSETY + height)
    add_vert_pins(p, p.last_x(), p.last_y() + o, pincount, spacing, -PIN_OUT_WIDTH, PIN_SIZE, -1)

def add_vent_grid(root, gridsizex, gridsizey, width, height, extra_offset):
    # Add vent hole grid
    grid = Group(f"vent_grid_{gridsizex}_{gridsizey}")
    root.groups.append(grid)

    hh = 4
    hw = 6 # (width / height) * hh
    gutter = 3
    h_extent = (gridsizey * hh) + (gridsizey - 1) * gutter
    w_extent = (gridsizex * hw) + (gridsizex - 1) * gutter
    h_offset =  (height - h_extent) / 2
    w_offset =  (width - w_extent) / 2
    for x, y in product(range(gridsizex), range(gridsizey)):
        xx = x * (hw + gutter) + w_offset
        yy = y * (hh + gutter) + h_offset
        if (x + y) % 2 == 0:
            continue
        hole = create_hole(OFFSETX + xx, OFFSETY + yy, hw, hh, f"vent_hole_{x}_{y}")
        hole.move(extra_offset)
        hole.flip_xy = FLIPXY
        grid.add_path(hole)

def add_foot_top(root, extra_offset_x:int = 0, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = distance(f1, rf2)
    top = Group("foot_top")
    root.groups.append(top)

    p = Path("foot_top_outline", True)
    p.move((extra_offset_x, extra_offset_y))
    p.flip_xy = FLIPXY
    p.color = constants.MAGENTA
    top.add_path(p)

    p.add_node(OFFSETX + 0,     OFFSETY + 0)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, PIN_OUT_WIDTH, PIN_SIZE, 1)

    p.add_node(OFFSETX + width, OFFSETY + 0)

    d = distance(f1, rf2)
    pincount = int((d - PIN_SIZE) / (2 * PIN_SIZE))
    spacing = d / pincount
    o = spacing / 2
    add_vert_pins(p, p.last_x(), p.last_y() - o, pincount, spacing, PIN_OUT_WIDTH, PIN_SIZE, 1)

    p.add_node(OFFSETX + width, OFFSETY + height)
    
    p.add_node(OFFSETX + 0,     OFFSETY + height)
    add_vert_pins(p, p.last_x(), p.last_y() + o, pincount, spacing, -PIN_OUT_WIDTH, PIN_SIZE, -1)

    add_vent_grid(top, 11, 11, width, height, (extra_offset_x, extra_offset_y))

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

    add_vent_grid(side, 11, 3, width, height, (extra_offset_x, extra_offset_y))

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
    global f1, f2, f3, f4, rf2, rf3, rf4
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
        f1 = (OFFSETX + width - FOOT_HEIGHT, OFFSETY + 0)
        f2 = (OFFSETX + width - FOOT_HEIGHT, OFFSETY + 0 - FOOT_SIZE)
        f3 = (OFFSETX + width, OFFSETY + 0 - FOOT_SIZE)
        f4 = (OFFSETX + width, OFFSETY + 0)
        r = Rotation(f1[0], f1[1], -FOOT_ANGLE)
        rf1 = rotate(r, f1[0], f1[1])
        rf2 = rotate(r, f2[0], f2[1])
        rf3 = rotate(r, f3[0], f3[1])
        rf4 = rotate(r, f4[0], f4[1])

        p.add_node(f1[0], f1[1])

        d = distance(f1, rf2)
        pincount = int((d - PIN_SIZE) / (2 * PIN_SIZE))
        spacing = d / pincount
        o = spacing / 2
        add_vert_pins(p, f1[0], f1[1] + o, pincount, spacing, PIN_OUT_WIDTH, PIN_SIZE, -1, r)

        p.add_node(f2[0], f2[1], r)
        
        d = distance(f2, f3)

        add_horz_pins(p, f2[0], f2[1], 1, d / 2, PIN_OUT_WIDTH, PIN_SIZE, 1, r)

        p.add_node(f3[0], f3[1], r)

        d = distance(rf3, rf4)
        pincount = int((d - PIN_SIZE) / (2 * PIN_SIZE))
        spacing = d / pincount
        o = spacing / 2
        add_vert_pins(p, f3[0], f3[1] - o, pincount, spacing, -PIN_OUT_WIDTH, PIN_SIZE, 1, r)

        p.add_node(f4[0], f4[1], r)
        p.add_node(f4[0], f4[1])
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
        add_foot_bottom(root, 0, spacing * 5.5)
        add_foot_top(root, 0, spacing * 9)
