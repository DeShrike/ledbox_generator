from group import Group
from path import Path
from ellipse import Ellipse
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def add_button_hole(g, cx:float, cy:float, add_wire_holes:bool, cutout:bool):
    dia = 14
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.RED)
    g.add_ellipse(e)

    if add_wire_holes:
        e = Ellipse(cx - 2.5, cy - 5.5, 0.7, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 2.5, cy - 5.5, 0.7, constants.BLUE)
        g.add_ellipse(e)

        e = Ellipse(cx - 2.5, cy + 5.5, 0.7, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 2.5, cy + 5.5, 0.7, constants.BLUE)
        g.add_ellipse(e)

def add_led_hole(g, cx:float, cy:float, add_wire_holes:bool, cutout:bool):
    dia = 6
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.RED)
    g.add_ellipse(e)

    if add_wire_holes:
        e = Ellipse(cx - 1, cy, 0.4, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 1, cy, 0.4, constants.BLUE)
        g.add_ellipse(e)

def add_circuit_box(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    w = 86
    h = 22

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
    for ccc in range(2):
        offsety += h + 10
        laag2 = Group(f"laag2_{ccc + 1}")
        root.groups.append(laag2)

        rbox = create_rounded_box(offsetx, offsety, w, h, 6)
        laag2.add_path(rbox)

        lh = add_led_hole(laag2, offsetx + 10, offsety + (h / 2), False, True)
        lh = add_led_hole(laag2, offsetx + 20, offsety + (h / 2), False, True)
        lh = add_led_hole(laag2, offsetx + 30, offsety + (h / 2), False, True)
        lh = add_led_hole(laag2, offsetx + 40, offsety + (h / 2), False, True)

        bh = add_button_hole(laag2, offsetx + 54, offsety + (h / 2), False, True)
        bh = add_button_hole(laag2, offsetx + 72, offsety + (h / 2), False, True)

    # Laag 3: Only holes to be placed on one of the sides
    offsety += h + 10
    laag3 = Group("laag3")
    root.groups.append(laag3)

    lh = add_led_hole(laag3, offsetx + 10, offsety + (h / 2), False, True)
    lh = add_led_hole(laag3, offsetx + 20, offsety + (h / 2), False, True)
    lh = add_led_hole(laag3, offsetx + 30, offsety + (h / 2), False, True)
    lh = add_led_hole(laag3, offsetx + 40, offsety + (h / 2), False, True)

    bh = add_button_hole(laag3, offsetx + 54, offsety + (h / 2), False, True)
    bh = add_button_hole(laag3, offsetx + 72, offsety + (h / 2), False, True)

def add_plastic_covers(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    plastic = Group(f"plastic_{extra_offset_x}_{extra_offset_y}")
    root.groups.append(plastic)

    w = GRID_PART_WIDTH - 1
    h = GRID_PART_HEIGHT - 1

    rbox = create_rounded_box(offsetx, offsety, w, h, 1)
    plastic.add_path(rbox)

def generate_ledsandbuttons(root):
    add_circuit_box(root, 0, 0)
    add_plastic_covers(root, 100, 0)
    add_plastic_covers(root, 100, 40)
    add_plastic_covers(root, 100, 80)
    add_plastic_covers(root, 100, 120)
