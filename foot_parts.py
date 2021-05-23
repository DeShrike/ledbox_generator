from group import Group
from path import Path
from helpers import *
from config  import *
import constants

OFFSETX = 10
OFFSETY = 10

def add_bottom(root):
    side = Group("foot_bottom")
    root.groups.append(side)

def add_top(root):
    side = Group("foot_top")
    root.groups.append(side)

def add_back(root):
    side = Group("foot_back")
    root.groups.append(side)

def generate_foot_parts(root):
    global OFFSETX, OFFSETY
    add_bottom(root)
    add_top(root)
    add_back(root)
