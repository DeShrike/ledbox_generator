from group import Group
from path import Path
from text import Text
import constants
import math

#######################################################################################
# Helpers
#######################################################################################

def rotate_point(cx:float, cy:float, px:float, py:float, angle:float):
    radians = angle / 360 * 2 * math.pi
    s = math.sin(radians);
    c = math.cos(radians);

    # translate to origin
    rx = px - cx
    ry = py - cy

    # rotate
    xnew = rx * c - ry * s
    ynew = rx * s + ry * c

    # translate back
    xnew += cx
    ynew += cy
    
    return (xnew, ynew)

def create_line(x1:float, y1:float, x2:float, y2:float, id:str):
    p = Path(id, False)
    p.color = constants.RED
    p.add_node(x1, y1)
    p.add_node(x2, y2)
    return p

def create_hole(x1:float, y1:float, w:float, h:float, id:str):
    p = Path(id, True)
    p.color = constants.GREEN
    p.add_node(x1, y1)
    p.add_node(x1 + w, y1)
    p.add_node(x1 + w, y1 + h)
    p.add_node(x1, y1 + h)
    return p

def add_rounded_corner(path, x:float, y:float, r:float, corner:str):
    if corner == "TL":
        start_angle = math.pi + (math.pi / 2)
        end_angle = math.pi / 2 + (math.pi / 2)
        cx = x + r
        cy = y + r
    elif corner == "TR":
        start_angle = math.pi / 2 + (math.pi / 2)
        end_angle = 0 + (math.pi / 2)
        cx = x - r
        cy = y + r
    elif corner == "BR":
        start_angle = 0 + (math.pi / 2)
        end_angle = -math.pi / 2 + (math.pi / 2)
        cx = x - r
        cy = y - r
    elif corner == "BL":
        start_angle = -math.pi / 2 + (math.pi / 2)
        end_angle = -math.pi + (math.pi / 2)
        cx = x + r
        cy = y - r

    a = start_angle
    steps = 8
    step = (math.pi / 2) / steps
    while a > end_angle:
        xx = math.sin(a) * r + cx
        yy = math.cos(a) * r + cy
        path.add_node(xx, yy)
        a -= step

    a = end_angle
    xx = math.sin(a) * r + cx
    yy = math.cos(a) * r + cy
    path.add_node(xx, yy)

def create_rounded_box(x:int, y: int, w:int, h:int, rounding:int = 3, color:str = constants.MAGENTA):
    p = Path(f"rounded_box_{x}_{y}", True)
    p.color = color

    add_rounded_corner(p, x + 0, y + 0, rounding, "TL")
    #p.add_node(x + 0, y + 0 + rounding)
    #p.add_node(x + 0 + rounding, y + 0)

    add_rounded_corner(p, x + w, y + 0, rounding, "TR")
    #p.add_node(x + w - rounding, y + 0)
    #p.add_node(x + w, y + 0 + rounding)

    add_rounded_corner(p, x + w, y + h, rounding, "BR")
    #p.add_node(x + w, y + h - rounding)
    #p.add_node(x + w - rounding, y + h)

    add_rounded_corner(p, x + 0, y + h, rounding, "BL")
    #p.add_node(x + 0 + rounding, y + h)
    #p.add_node(x + 0, y + h - rounding)

    return p

def add_vert_pins(path, x:float, y:float, count:int, spacing:float, indent:float, thickness:float, direction:int):
    # adds pins on a vertical line
    # x, y: start point
    # count: numbers of pins
    # spacing: distance between pin centers
    # indent: size of pin
    # thickness: thickness of pin
    # direction: 1 or -1: y-direction
    for _ in range(count):
        y += (spacing - (thickness / 2.0)) * direction
        path.add_node(x, y)
        x += indent
        path.add_node(x, y)
        y += thickness * direction
        path.add_node(x, y)
        x -= indent
        path.add_node(x, y)
        y -= (thickness / 2.0) * direction

def add_horz_pins(path, x:float, y:float, count:int, spacing:float, indent:float, thickness:float, direction:int):
    # adds pins on a horizontal line
    # x, y: start point
    # count: numbers of pins
    # spacing: distance between stub centers
    # indent: size of pin
    # thickness: thickness of pin
    # direction: 1 or -1: x-direction
    for _ in range(count):
        x += (spacing - (thickness / 2.0)) * direction
        path.add_node(x, y)
        y += indent
        path.add_node(x, y)
        x += thickness * direction
        path.add_node(x, y)
        y -= indent
        path.add_node(x, y)
        x -= (thickness / 2.0) * direction

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

def add_text(root, name:str):
    g = Group("legend")
    root.groups.append(g)
    t = Text(50, 40, constants.BLACK,   name)
    g.texts.append(t)
    t = Text(50, 45, constants.RED,     "Red: Etch")
    g.texts.append(t)
    t = Text(50, 50, constants.BLUE,    "Blue: Cut")
    g.texts.append(t)
    t = Text(50, 55, constants.GREEN,   "Green: Cut")
    g.texts.append(t)
    t = Text(50, 60, constants.MAGENTA, "Magenta: Cut")
    g.texts.append(t)

def save(root, filename, id, w:int, h:int):
    print(f"Writing file {filename}")
    with open(filename, "w") as fd:
        header = constants.SVG_START
        header = header.replace("{{FILENAME}}", filename)
        header = header.replace("{{ID}}", id)
        header = header.replace("{{PAPERWIDTH}}", str(w))
        header = header.replace("{{PAPERHEIGHT}}", str(h))
        fd.write(header)
        root.write_to_file(fd)
        fd.write(constants.SVG_END)
