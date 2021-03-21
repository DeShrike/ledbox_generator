from group import Group
from path import Path
from ellipse import Ellipse
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def add_long_side(root, extra_offset_y:int = 0):
    width = HORIZONTAL_DIVIDER_LENGTH
    height = DIVIDER_HEIGHT
    side = Group("long_side")
    root.groups.append(side)

    p = Path("side", True)
    p.color = constants.RED
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    add_horz_pins(p, p.last_x() - (GRID_PART_WIDTH / 2) - THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, -PIN_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, PIN_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    add_horz_pins(p, p.last_x() + (GRID_PART_WIDTH / 2) + THICKNESS, p.last_y(), GRID_W, GRID_PART_WIDTH + THICKNESS, PIN_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, -PIN_WIDTH, PIN_SIZE, -1)

    lines = Group("indicatorlines")
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

def add_short_side(root, extra_offset_y:int = 0):
    width = VERTICAL_DIVIDER_LENGTH + (2 * THICKNESS)
    height = DIVIDER_HEIGHT
    side = Group("short_side")
    root.groups.append(side)

    p = Path("side", True)
    p.color = constants.RED
    side.add_path(p)

    # top left
    p.add_node(OFFSETX + 0,     OFFSETY + 0 + extra_offset_y)
    add_horz_pins(p, p.last_x() - (GRID_PART_HEIGHT / 2), p.last_y(), GRID_H, GRID_PART_HEIGHT + THICKNESS, -PIN_WIDTH, PIN_SIZE, 1)

    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0 + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() + (height / 2), 1, 0, -PIN_WIDTH, PIN_SIZE, 1)

    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height + extra_offset_y)
    add_horz_pins(p, p.last_x() + (GRID_PART_HEIGHT / 2), p.last_y(), GRID_H, GRID_PART_HEIGHT + THICKNESS, PIN_WIDTH, PIN_SIZE, -1)
    
    # bottom left
    p.add_node(OFFSETX + 0,     OFFSETY + height + extra_offset_y)
    add_vert_pins(p, p.last_x(), p.last_y() - (height / 2), 1, 0, PIN_WIDTH, PIN_SIZE, -1)

    lines = Group("indicatorlines")
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

def add_button_hole(g, cx:float, cy:float, add_wire_holes:bool, cutout:bool):
    dia = 13
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.MAGENTA)
    g.add_ellipse(e)

    if add_wire_holes:
        e = Ellipse(cx - 2.5, cy - 5, 0.3, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 2.5, cy - 5, 0.3, constants.BLUE)
        g.add_ellipse(e)

        e = Ellipse(cx - 2.5, cy + 5, 0.3, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 2.5, cy + 5, 0.3, constants.BLUE)
        g.add_ellipse(e)

def add_led_hole(g, cx:float, cy:float, add_wire_holes:bool, cutout:bool):
    dia = 6
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.MAGENTA)
    g.add_ellipse(e)

    if add_wire_holes:
        e = Ellipse(cx - 1, cy, 0.2, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 1, cy, 0.2, constants.BLUE)
        g.add_ellipse(e)

def add_circuit_box(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    w = 86
    h = 25

    # Laag 1
    laag1 = Group("laag1")
    root.groups.append(laag1)

    rbox = create_rounded_box(offsetx, offsety, w, h, 6)
    laag1.add_path(rbox)

    lh = add_led_hole(laag1, offsetx + 10, offsety + (h / 2), True, False)
    lh = add_led_hole(laag1, offsetx + 20, offsety + (h / 2), True, False)
    lh = add_led_hole(laag1, offsetx + 30, offsety + (h / 2), True, False)
    lh = add_led_hole(laag1, offsetx + 40, offsety + (h / 2), True, False)

    bh = add_button_hole(laag1, offsetx + 54, offsety + (h / 2), True, False)
    bh = add_button_hole(laag1, offsetx + 72, offsety + (h / 2), True, False)

    # Laag 2
    offsety += h + 10
    laag2 = Group("laag2")
    root.groups.append(laag2)

    rbox = create_rounded_box(offsetx, offsety, w, h, 6)
    laag2.add_path(rbox)

    lh = add_led_hole(laag2, offsetx + 10, offsety + (h / 2), False, True)
    lh = add_led_hole(laag2, offsetx + 20, offsety + (h / 2), False, True)
    lh = add_led_hole(laag2, offsetx + 30, offsety + (h / 2), False, True)
    lh = add_led_hole(laag2, offsetx + 40, offsety + (h / 2), False, True)

    bh = add_button_hole(laag2, offsetx + 54, offsety + (h / 2), False, True)
    bh = add_button_hole(laag2, offsetx + 72, offsety + (h / 2), False, True)

def add_plastic_covers(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    plastic = Group(f"plastic_{extra_offset_x}")
    root.groups.append(plastic)

    w = GRID_PART_WIDTH - 1
    h = GRID_PART_HEIGHT - 1

    rbox = create_rounded_box(offsetx, offsety, w, h, 1)
    plastic.add_path(rbox)

def generate_sides(root):
    spacing = BOX_INNER_DEPTH + 10
    add_long_side(root)
    add_long_side(root, spacing * 1)
    add_short_side(root, spacing * 2)
    add_short_side(root, spacing * 3)
    add_circuit_box(root, 150, 80)
    add_plastic_covers(root, 200, 0)
    add_plastic_covers(root, 200, 40)
    add_plastic_covers(root, 200, 80)
    add_plastic_covers(root, 200, 120)

