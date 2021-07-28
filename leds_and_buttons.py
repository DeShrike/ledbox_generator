from group import Group
from path import Path
from ellipse import Ellipse
from helpers import *
from config  import *
import constants
from math import radians, cos, sin

HOLESTEP = 2.54
OFFSETX = 10
OFFSETY = 10

def add_button_hole(g, cx:float, cy:float, add_wire_holes:str, cutout:bool, dia:int = 16):
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.RED)
    g.add_ellipse(e)

    if add_wire_holes == "HORIZONTAL":
        e = Ellipse(cx - 5.7, cy - HOLESTEP, 1.6, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 5.7, cy - HOLESTEP, 1.6, constants.BLUE)
        g.add_ellipse(e)

        e = Ellipse(cx - 5.7, cy + HOLESTEP, 1.6, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 5.7, cy + HOLESTEP, 1.6, constants.BLUE)
        g.add_ellipse(e)
    elif add_wire_holes == "VERTICAL":
        e = Ellipse(cx - HOLESTEP, cy - 5.7, 1.6, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + HOLESTEP, cy - 5.7, 1.6, constants.BLUE)
        g.add_ellipse(e)

        e = Ellipse(cx - HOLESTEP, cy + 5.7, 1.6, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + HOLESTEP, cy + 5.7, 1.6, constants.BLUE)
        g.add_ellipse(e)

        """
        p = Path(f"ll{cx}{cy}", constants.RED)
        p.add_node(cx - HOLESTEP, cy - 8)
        p.add_node(cx - HOLESTEP, cy + 8)
        g.add_path(p)
        p = Path(f"lll{cx}{cy}", constants.RED)
        p.add_node(cx + HOLESTEP, cy - 8)
        p.add_node(cx + HOLESTEP, cy + 8)
        g.add_path(p)
        """

def add_led_hole(g, cx:float, cy:float, add_wire_holes:bool, cutout:bool):
    dia = 6
    e = Ellipse(cx, cy, dia / 2, constants.BLUE if cutout else constants.RED)
    g.add_ellipse(e)

    if add_wire_holes == "VERTICAL":
        e = Ellipse(cx, cy - 1, 0.4, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx, cy + 1, 0.4, constants.BLUE)
        g.add_ellipse(e)

        """
        p = Path(f"l{cx}{cy}", constants.RED)
        p.add_node(cx, cy - 8)
        p.add_node(cx, cy + 8)
        g.add_path(p)
        """
    elif add_wire_holes == "HORIZONTAL":
        e = Ellipse(cx - 1, cy, 0.4, constants.BLUE)
        g.add_ellipse(e)
        e = Ellipse(cx + 1, cy, 0.4, constants.BLUE)
        g.add_ellipse(e)


def add_circuit_box(root, extra_offset_x:int, extra_offset_y:int, fastening_hole_dia:int, add_wire_holes_led:str, add_wire_holes_button:str, cutout:bool, button_hole_dia:int = 16, full_cutout:bool = False):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    w = 86
    h = 22

    fastening_extra = 15
    if fastening_hole_dia == 0:
        fastening_extra = 0
    else:
        offsetx += fastening_extra

    # Laag 1
    laag1 = Group(f"add_circuit_box_{offsetx}{offsety}")
    root.groups.append(laag1)

    rbox = create_rounded_box(offsetx - fastening_extra, offsety, w + (fastening_extra * 2), h, 6)
    if not full_cutout:
        rbox.color = constants.RED
    laag1.add_path(rbox)

    lh = add_led_hole(laag1, offsetx + 10 + 0 * HOLESTEP, offsety + (h / 2), add_wire_holes_led, cutout)
    lh = add_led_hole(laag1, offsetx + 10 + 4 * HOLESTEP, offsety + (h / 2), add_wire_holes_led, cutout)
    lh = add_led_hole(laag1, offsetx + 10 + 8 * HOLESTEP, offsety + (h / 2), add_wire_holes_led, cutout)
    lh = add_led_hole(laag1, offsetx + 10 + 12 * HOLESTEP, offsety + (h / 2), add_wire_holes_led, cutout)

    bh = add_button_hole(laag1, offsetx + 10 + 18 * HOLESTEP, offsety + (h / 2), add_wire_holes_button, cutout, button_hole_dia)
    bh = add_button_hole(laag1, offsetx + 10 + 25 * HOLESTEP, offsety + (h / 2), add_wire_holes_button, cutout, button_hole_dia)

    if fastening_hole_dia > 0:
        cx = (offsetx - fastening_extra) + h / 2
        cy = offsety + h / 2
        e = Ellipse(cx, cy, fastening_hole_dia / 2, constants.BLUE)
        laag1.add_ellipse(e)
        cx = (offsetx - fastening_extra) + w + (fastening_extra * 2) - h / 2
        e = Ellipse(cx, cy, fastening_hole_dia / 2, constants.BLUE)
        laag1.add_ellipse(e)

    """
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
    """

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

def add_mini_standoffs(root, extra_offset_x:int, extra_offset_y:int):
    offsetx = OFFSETX + extra_offset_x
    offsety = OFFSETY + extra_offset_y

    plastic = Group(f"mini_standoff_{extra_offset_x}_{extra_offset_y}")
    root.groups.append(plastic)

    w = 18
    h = 4

    for x in range(10):
        hole = create_rounded_box(offsetx, offsety, w, h, 1)
        # hole = create_hole(offsetx, offsety, w, h, f"mini_standoff_{offsetx}")
        hole.color = constants.BLUE
        plastic.add_path(hole)
        offsety += 10

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
    spacing = 25
    ey = 0
    add_circuit_box(root, 0, ey, 3.1, None, None, True, 14, False)
    ey += spacing
    add_circuit_box(root, 0, ey, 3.1, None, None, True, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey,   6, None, None, True, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey, 3.1, None, None, True, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey,   6, None, None, True, 16, True)

    # ey += spacing
    # add_circuit_box(root, 0, ey,   0, "HORIZONTAL", "HORIZONTAL", False, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey,   0, "VERTICAL",   "VERTICAL",   False, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey,   0, "VERTICAL",   "HORIZONTAL", False, 16, True)
    # ey += spacing
    # add_circuit_box(root, 0, ey,   0, "HORIZONTAL", "VERTICAL",   False, 16, True)


    # ey += spacing
    # add_circuit_box(root, 0, ey, 3.1, "HORIZONTAL", "HORIZONTAL", False, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey, 3.1, "VERTICAL",   "VERTICAL",   False, 16, True)
    # ey += spacing
    # add_circuit_box(root, 0, ey, 3.1, "VERTICAL",   "HORIZONTAL", False, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey, 3.1, "HORIZONTAL", "VERTICAL",   False, 16, True)


    # ey += spacing
    # add_circuit_box(root, 0, ey,   6, "HORIZONTAL", "HORIZONTAL", False, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey,   6, "VERTICAL",   "VERTICAL",   False, 16, True)
    # ey += spacing
    # add_circuit_box(root, 0, ey,   6, "VERTICAL",   "HORIZONTAL", False, 16, True)
    ey += spacing
    add_circuit_box(root, 0, ey,   6, "HORIZONTAL", "VERTICAL",   False, 16, True)

    """
    add_circuit_box(root, 0, 120, 0, False, True, 16)
    add_circuit_box(root, 0, 150, 0, False, True, 16)

    add_circuit_box(root, 0, 180, 0, False, True, 15)
    add_circuit_box(root, 0, 210, 0, False, True, 14)
    """

    """
    add_plastic_covers(root, 90, 0)
    add_plastic_covers(root, 90, 35)
    add_plastic_covers(root, 90, 70)
    add_plastic_covers(root, 90, 105)
    """

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

    add_mini_standoffs(root, 95, 125)

    add_fan_hole(root, 125, 120)
