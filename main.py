from layer import Layer
from group import Group
from path import Path
from text import Text
from helpers import *
from config  import *

from bottom_plate import generate_bottom_plate
from top_plate import generate_top_plate
from long_dividers import generate_long_dividers
from short_dividers import generate_short_dividers
from sides import generate_sides

def main():

    bottomplate = Layer("Root")
    generate_bottom_plate(bottomplate)
    add_text(bottomplate, "Bottom Plate")
    save(bottomplate, "bottom_plate.svg", "BOTTOMPLATE", PAPER_WIDTH, PAPER_HEIGHT)

    topplate = Layer("Root")
    generate_top_plate(topplate)
    add_text(topplate, "Top Plate")
    save(topplate, "top_plate.svg", "TOPPLATE", PAPER_WIDTH, PAPER_HEIGHT)

    longdividers = Layer("Root")
    generate_long_dividers(longdividers)
    add_text(longdividers, "Long Dividers")
    save(longdividers, "long_dividers.svg", "LONGDIVIDERS", PAPER_WIDTH, PAPER_HEIGHT)

    shortdividers = Layer("Root")
    generate_short_dividers(shortdividers)
    add_text(shortdividers, "Short Dividers")
    save(shortdividers, "short_dividers.svg", "SHORTDIVIDERS", PAPER_WIDTH, PAPER_HEIGHT)

    sides = Layer("Root")
    generate_sides(sides)
    add_text(sides, "Sides")
    save(sides, "sides.svg", "SIDES", PAPER_WIDTH, PAPER_HEIGHT)

if __name__ == "__main__":
    main()
