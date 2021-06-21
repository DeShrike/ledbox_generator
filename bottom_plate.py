from group import Group
from path import Path
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def create_hole(x1:float, y1:float, w:float, h:float, id:str):
    p = Path(id, True)
    p.color = constants.BLUE
    p.add_node(x1, y1)
    p.add_node(x1 + w, y1)
    p.add_node(x1 + w, y1 + h)
    p.add_node(x1, y1 + h)
    return p

def add_outline(root):
    width = HORIZONTAL_DIVIDER_LENGTH + (2 * THICKNESS) + (2 * LIP_WIDTH)
    height = VERTICAL_DIVIDER_LENGTH  + (2 * THICKNESS) + (2 * LIP_WIDTH)
    outline = Group("outline")
    root.groups.append(outline)

    p = create_rounded_box(OFFSETX, OFFSETY, width, height, 6)
    outline.add_path(p)
    
    """
    p = Path("outer_border", True)
    p.color = constants.MAGENTA2
    outline.add_path(p)

    # top left
    p.add_node(OFFSETX + 0, OFFSETY + 0)
    # top right
    p.add_node(OFFSETX + width, OFFSETY + 0)
    # bottom right
    p.add_node(OFFSETX + width, OFFSETY + height)
    # bottom left
    p.add_node(OFFSETX + 0, OFFSETY + height)
    """

def add_indicator_crosses(root):
    crosses = Group("crosses")
    root.groups.append(crosses)
    v_line_length = GRID_PART_HEIGHT / 3
    h_line_length = GRID_PART_WIDTH / 3 
    for xx in range(GRID_W):
        for yy in range(GRID_H):
            cx = xx * (GRID_PART_WIDTH + THICKNESS) + (GRID_PART_WIDTH / 2) + LIP_WIDTH + THICKNESS
            cy = yy * (GRID_PART_HEIGHT + THICKNESS) + (GRID_PART_HEIGHT / 2) + LIP_WIDTH + THICKNESS

            x = cx
            y = cy - (v_line_length / 2)
            v = create_line(OFFSETX + x, OFFSETY + y, OFFSETX + x, OFFSETY + y + v_line_length, f"cross_v_{xx}_{yy}")
            crosses.add_path(v)

            x = cx - (h_line_length / 2)
            y = cy
            h = create_line(OFFSETX + x, OFFSETY + y, OFFSETX + x + h_line_length, OFFSETY + y, f"cross_h_{xx}_{yy}")
            crosses.add_path(h)

def add_indicator_lines(root):
    hlines = Group("horizontal_lines")
    vlines = Group("vertical_lines")
    root.groups.append(vlines)
    root.groups.append(hlines)

    # Vertical Lines
    x = LIP_WIDTH
    line_length = GRID_H * GRID_PART_HEIGHT + ((GRID_H - 1) * THICKNESS)
    for ix in range(GRID_W + 1):
        y = LIP_WIDTH + THICKNESS
        l = create_line(OFFSETX + x, OFFSETY + y, OFFSETX + x, OFFSETY + y + line_length, f"vline_{ix}_a")
        vlines.add_path(l)
        x += THICKNESS
        l = create_line(OFFSETX + x, OFFSETY + y, OFFSETX + x, OFFSETY + y + line_length, f"vline_{ix}_b")
        vlines.add_path(l)
        x += GRID_PART_WIDTH

    # Horizontal Lines
    y = LIP_WIDTH
    line_length = GRID_W * GRID_PART_WIDTH + ((GRID_W - 1) * THICKNESS)
    for ix in range(GRID_H + 1):
        x = LIP_WIDTH + THICKNESS
        l = create_line(OFFSETX + x, OFFSETY + y, OFFSETX + x + line_length, OFFSETY + y, f"hline_{ix}_a")
        hlines.add_path(l)
        y += THICKNESS
        l = create_line(OFFSETX + x, OFFSETY + y, OFFSETX + x + line_length, OFFSETY + y, f"hline_{ix}_b")
        hlines.add_path(l)
        y += GRID_PART_HEIGHT

def add_side_pin_holes(root, is_bottom_plate:bool):
    pholes = Group("side_pin_holes")
    root.groups.append(pholes)

    delta = (PIN_WIDTH - THICKNESS) / 2  # To compensate for the fact that PIN_WIDTH is thicker than THICKNESS

    # Top & Bottom
    for xx in range(GRID_W):
        y = LIP_WIDTH - delta
        x = LIP_WIDTH + (xx * (THICKNESS + GRID_PART_WIDTH)) + THICKNESS + ((GRID_PART_WIDTH - PIN_SIZE) / 2)
        h = create_hole(OFFSETX + x, OFFSETY + y, PIN_SIZE, PIN_WIDTH, f"pinhole_top_{xx}")
        pholes.add_path(h)
        y = LIP_WIDTH + VERTICAL_DIVIDER_LENGTH + THICKNESS - delta
        h = create_hole(OFFSETX + x, OFFSETY + y, PIN_SIZE, PIN_WIDTH, f"pinhole_bottom_{xx}")
        pholes.add_path(h)

    # Left & Right
    pinholecount = GRID_H - 2 if ADD_FOOT and is_bottom_plate else GRID_H
    for yy in range(pinholecount):
        x = LIP_WIDTH - delta
        y = LIP_WIDTH + (yy * (THICKNESS + GRID_PART_HEIGHT)) + THICKNESS + ((GRID_PART_HEIGHT - PIN_SIZE) / 2)
        h = create_hole(OFFSETX + x, OFFSETY + y, PIN_WIDTH, PIN_SIZE, f"pinhole_left_{yy}")
        pholes.add_path(h)
        x = LIP_WIDTH + HORIZONTAL_DIVIDER_LENGTH + THICKNESS - delta
        h = create_hole(OFFSETX + x, OFFSETY + y, PIN_WIDTH, PIN_SIZE, f"pinhole_right_{yy}")
        pholes.add_path(h)

    if ADD_FOOT and is_bottom_plate:
        # Create holes for footside
        speling = 0.02
        x = LIP_WIDTH - delta
        y = VERTICAL_DIVIDER_LENGTH  + (1 * THICKNESS) + (1 * LIP_WIDTH) - FOOT_HEIGHT                       + THICKNESS - (FOOT_HEIGHT * speling)
        h = create_hole(OFFSETX + x, OFFSETY + y, PIN_WIDTH, FOOT_HEIGHT * (1 + speling), f"backhole_left")
        pholes.add_path(h)
        x = LIP_WIDTH + HORIZONTAL_DIVIDER_LENGTH + THICKNESS - delta
        h = create_hole(OFFSETX + x, OFFSETY + y, PIN_WIDTH, FOOT_HEIGHT * (1 + speling), f"backhole_right_{yy}")
        pholes.add_path(h)

def add_center_horizontal_pin_holes(root, no_firstandlast_hole:bool = False):
    choles = Group("horizontal_center_pin_holes")
    root.groups.append(choles)

    delta = (PIN_WIDTH - THICKNESS) / 2  # To compensate for the fact that PIN_WIDTH is thicker than THICKNESS

    # Center
    for yy in range(1, GRID_H):

        y = LIP_WIDTH + (yy * (THICKNESS + GRID_PART_HEIGHT)) - delta
        for xx in range(GRID_W):
            if no_firstandlast_hole and (xx == 0 or xx == GRID_W - 1):
                continue

            x = LIP_WIDTH + (xx * (THICKNESS + GRID_PART_WIDTH)) + THICKNESS + ((GRID_PART_WIDTH - PIN_SIZE) / 2)
            h = create_hole(OFFSETX + x, OFFSETY + y, PIN_SIZE, PIN_WIDTH, f"h_pinhole_center_{xx}_{yy}")
            choles.add_path(h)

def add_center_vertical_pin_holes(root):
    choles = Group("vertical_center_pin_holes")
    root.groups.append(choles)

    delta = (PIN_WIDTH - THICKNESS) / 2  # To compensate for the fact that PIN_WIDTH is thicker than THICKNESS

    # Center
    for xx in range(1, GRID_W):
        x = LIP_WIDTH + (xx * (THICKNESS + GRID_PART_WIDTH)) - delta
        for yy in range(GRID_H):
            y = LIP_WIDTH + (yy * (THICKNESS + GRID_PART_HEIGHT)) + THICKNESS + ((GRID_PART_HEIGHT - PIN_SIZE) / 2)
            h = create_hole(OFFSETX + x, OFFSETY + y, PIN_WIDTH, PIN_SIZE, f"v_pinhole_left_{xx}_{yy}")
            choles.add_path(h)

def generate_bottom_plate(root):
    add_outline(root)
    add_indicator_lines(root)
    add_indicator_crosses(root)
    add_side_pin_holes(root, True)
    add_center_horizontal_pin_holes(root, True)
