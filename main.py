from layer import Layer
from group import Group
from path import Path
from text import Text
from helpers import *
import config
import constants

from bottom_plate import generate_bottom_plate
from top_plate import generate_top_plate
from long_sides import generate_long_sides
from short_sides import generate_short_sides

def main():

    bottomplate = Layer("Root")
    generate_bottom_plate(bottomplate)
    add_text(bottomplate, "Bottom Plate")
    save(bottomplate, "bottom_plate.svg", "BOTTOMPLATE", 610, 450)

    topplate = Layer("Root")
    generate_top_plate(topplate)
    add_text(topplate, "Top Plate")
    save(topplate, "top_plate.svg", "TOPPLATE", 610, 450)

    longsides = Layer("Root")
    generate_long_sides(longsides)
    add_text(longsides, "Long Sides")
    save(longsides, "long_sides.svg", "LONGSIDES", 610, 450)

    shortsides = Layer("Root")
    generate_short_sides(shortsides)
    add_text(shortsides, "Short Sides")
    save(shortsides, "short_sides.svg", "SHORTSIDES", 610, 450)

if __name__ == "__main__":
    main()
