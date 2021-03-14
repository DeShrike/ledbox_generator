from group import Group
from path import Path
from text import Text
import constants

#######################################################################################
# Helpers
#######################################################################################

def create_line(x1:int, y1:int, x2:int, y2:int, id:str):
    p = Path(id, False)
    p.color = constants.MAGENTA
    p.add_node(x1, y1)
    p.add_node(x2, y2)
    return p

def create_hole(x1:int, y1:int, w:int, h:int, id:str):
    p = Path(id, True)
    p.color = constants.GREEN
    p.add_node(x1, y1)
    p.add_node(x1 + w, y1)
    p.add_node(x1 + w, y1 + h)
    p.add_node(x1, y1 + h)
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

def add_text(root, name:str):
    g = Group("legend")
    root.groups.append(g)
    t = Text(50, 40, constants.BLACK,   name)
    g.texts.append(t)
    t = Text(50, 45, constants.RED,     "Red: Cut")
    g.texts.append(t)
    t = Text(50, 50, constants.GREEN,   "Green: Cut")
    g.texts.append(t)
    t = Text(50, 55, constants.BLUE,    "Blue: Cut")
    g.texts.append(t)
    t = Text(50, 60, constants.MAGENTA, "Magenta: Etch")
    g.texts.append(t)

def save(root, filename, id, w:int, h:int):
    with open(filename, "w") as fd:
        header = constants.SVG_START
        header = header.replace("{{FILENAME}}", filename)
        header = header.replace("{{ID}}", id)
        header = header.replace("{{PAPERWIDTH}}", str(w))
        header = header.replace("{{PAPERHEIGHT}}", str(h))
        fd.write(header)
        root.write_to_file(fd)
        fd.write(constants.SVG_END)
