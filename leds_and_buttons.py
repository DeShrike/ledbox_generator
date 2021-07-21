from group import Group
from path import Path
from ellipse import Ellipse
from helpers import *
from config  import *
import constants
from math import radians, cos, sin

OFFSETX = 10
OFFSETY = 10

def add_button_hole(g, cx:float, cy:float, add_wire_holes:bool, cutout:bool, dia:int = 16):
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.RED)
    g.add_ellipse(e)

    if add_wire_holes:
        e = Ellipse(cx - 5.7, cy - 2.5, 1.6, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 5.7, cy - 2.5, 1.6, constants.BLUE)
        g.add_ellipse(e)

        e = Ellipse(cx - 5.7, cy + 2.5, 1.6, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 5.7, cy + 2.5, 1.6, constants.BLUE)
        g.add_ellipse(e)

def add_led_hole(g, cx:float, cy:float, add_wire_holes:bool, cutout:bool):
    dia = 6
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.RED)
    g.add_ellipse(e)

    if add_wire_holes:
        e = Ellipse(cx, cy - 1, 0.4, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx, cy + 1, 0.4, constants.BLUE)
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
        offsety += h + 5
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
    offsety += h + 5
    laag3 = Group("laag3")
    root.groups.append(laag3)

    rbox = create_rounded_box(offsetx, offsety, w, h, 6)
    rbox.color = constants.RED
    laag3.add_path(rbox)

    lh = add_led_hole(laag3, offsetx + 10, offsety + (h / 2), False, True)
    lh = add_led_hole(laag3, offsetx + 20, offsety + (h / 2), False, True)
    lh = add_led_hole(laag3, offsetx + 30, offsety + (h / 2), False, True)
    lh = add_led_hole(laag3, offsetx + 40, offsety + (h / 2), False, True)

    bh = add_button_hole(laag3, offsetx + 54, offsety + (h / 2), False, True)
    bh = add_button_hole(laag3, offsetx + 72, offsety + (h / 2), False, True)

    # Laag 4: Only holes to be placed on one of the sides
    offsety += h + 5
    laag4 = Group("laag4")
    root.groups.append(laag4)

    rbox = create_rounded_box(offsetx, offsety, w, h, 6)
    rbox.color = constants.RED
    laag4.add_path(rbox)

    lh = add_led_hole(laag4, offsetx + 10, offsety + (h / 2), False, True)
    lh = add_led_hole(laag4, offsetx + 20, offsety + (h / 2), False, True)
    lh = add_led_hole(laag4, offsetx + 30, offsety + (h / 2), False, True)
    lh = add_led_hole(laag4, offsetx + 40, offsety + (h / 2), False, True)

    bh = add_button_hole(laag4, offsetx + 54, offsety + (h / 2), False, True, 15)
    bh = add_button_hole(laag4, offsetx + 72, offsety + (h / 2), False, True, 15)

    # Laag 4: Only holes to be placed on one of the sides
    offsety += h + 5
    laag5 = Group("laag5")
    root.groups.append(laag5)

    rbox = create_rounded_box(offsetx, offsety, w, h, 6)
    rbox.color = constants.RED
    laag5.add_path(rbox)

    lh = add_led_hole(laag5, offsetx + 10, offsety + (h / 2), False, True)
    lh = add_led_hole(laag5, offsetx + 20, offsety + (h / 2), False, True)
    lh = add_led_hole(laag5, offsetx + 30, offsety + (h / 2), False, True)
    lh = add_led_hole(laag5, offsetx + 40, offsety + (h / 2), False, True)

    bh = add_button_hole(laag5, offsetx + 54, offsety + (h / 2), False, True, 14)
    bh = add_button_hole(laag5, offsetx + 72, offsety + (h / 2), False, True, 14)

def add_plastic_covers(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    plastic = Group(f"plastic_{extra_offset_x}_{extra_offset_y}")
    root.groups.append(plastic)

    w = GRID_PART_WIDTH - 1
    h = GRID_PART_HEIGHT - 1

    rbox = create_rounded_box(offsetx, offsety, w, h, 1)
    plastic.add_path(rbox)

def add_standoff(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    plastic = Group(f"standoff_{extra_offset_x}_{extra_offset_y}")
    root.groups.append(plastic)

    w = 15
    h = 15

    rbox = create_rounded_box(offsetx, offsety, w, h, 1)
    plastic.add_path(rbox)
    r = 1.55
    e = Ellipse(offsetx + w / 2, offsety + h / 2, r, constants.BLUE)
    plastic.add_ellipse(e)

def add_fan_hole(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    fanhole = Group(f"fanhole_{extra_offset_x}_{extra_offset_y}")
    root.groups.append(fanhole)

    w = 30
    h = 30

    holedistx = 25
    holedisty = 25
    hole_dia = 1.55

    rbox = create_rounded_box(offsetx, offsety, w, h, 2, constants.RED)
    fanhole.add_path(rbox)

    x = (w - holedistx) / 2
    y = (h - holedisty) / 2

    e = Ellipse(offsetx + x,             offsety + y,             hole_dia, constants.BLUE)
    fanhole.add_ellipse(e)
    e = Ellipse(offsetx + x + holedistx, offsety + y,             hole_dia, constants.BLUE)
    fanhole.add_ellipse(e)
    e = Ellipse(offsetx + x,             offsety + y + holedisty, hole_dia, constants.BLUE)
    fanhole.add_ellipse(e)
    e = Ellipse(offsetx + x + holedistx, offsety + y + holedisty, hole_dia, constants.BLUE)
    fanhole.add_ellipse(e)

    cx = w / 2
    cy = h / 2

    r_small = 10 / 2
    r_large = 27 / 2

    def create_wind_hole(angle_from:float, angle_to:float):
        step = radians(3)   # step of 3*
        p = Path(f"windhole_{angle_from}", True)
        p.color = constants.MAGENTA

        gutter_l = radians(3)
        gutter_s = radians(6)

        a = angle_from + gutter_l
        while a <= angle_to - gutter_l:
            x = cos(a) * r_large
            y = sin(a) * r_large
            p.add_node(offsetx + cx + x,     offsety + cy + y)
            a += step

        a = angle_to - gutter_s
        while a >= angle_from + gutter_s:
            x = cos(a) * r_small
            y = sin(a) * r_small
            p.add_node(offsetx + cx + x,     offsety + cy + y)
            a -= step

        return p

    parts = 3
    afrom = 0
    ato = afrom + 360 / parts
    for h in range(parts):
        l = create_wind_hole(radians(afrom), radians(ato))
        fanhole.add_path(l)
        afrom += 360 / parts
        ato = afrom + 360 / parts

def generate_ledsandbuttons(root):
    add_circuit_box(root, 0, 0)

    add_plastic_covers(root, 90, 0)
    add_plastic_covers(root, 90, 35)
    add_plastic_covers(root, 90, 70)
    add_plastic_covers(root, 90, 105)

    add_standoff(root, 125, 0)
    add_standoff(root, 125, 20)
    add_standoff(root, 125, 40)
    add_standoff(root, 125, 60)
    add_standoff(root, 125, 80)
    add_standoff(root, 125, 100)

    add_standoff(root, 145, 0)
    add_standoff(root, 145, 20)
    add_standoff(root, 145, 40)
    add_standoff(root, 145, 60)
    add_standoff(root, 145, 80)
    add_standoff(root, 145, 100)

    add_fan_hole(root, 125, 120)
