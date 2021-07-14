import os
from layer import Layer
from group import Group
from path import Path
from text import Text
from helpers import *
from config  import *

from bottom_plate import generate_bottom_plate
from top_plate import generate_top_plate
from horizontal_dividers import generate_horizontal_dividers
from vertical_dividers import generate_vertical_dividers
from sides import generate_sides
from leds_and_buttons import generate_ledsandbuttons

def main():

    bottomplate = Layer("Root")
    generate_bottom_plate(bottomplate)
    if ADD_TEXT_LEGEND:
        add_text(bottomplate, "Bottom Plate")
    save(bottomplate, os.path.join(OUTPUT_FOLDER, "bottom_plate.svg"), "BOTTOMPLATE", PAPER_WIDTH, PAPER_HEIGHT)

    topplate = Layer("Root")
    generate_top_plate(topplate)
    if ADD_TEXT_LEGEND:
        add_text(topplate, "Top Plate")
    save(topplate, os.path.join(OUTPUT_FOLDER, "top_plate.svg"), "TOPPLATE", PAPER_WIDTH, PAPER_HEIGHT)

    horizontaldividers = Layer("Root")
    generate_horizontal_dividers(horizontaldividers)
    if ADD_TEXT_LEGEND:
        add_text(horizontaldividers, "Horizontal Dividers")
    save(horizontaldividers, os.path.join(OUTPUT_FOLDER, "horizontal_dividers.svg"), "HORIZONTALDIVIDERS", PAPER_WIDTH, PAPER_HEIGHT)

    verticaldividers = Layer("Root")
    generate_vertical_dividers(verticaldividers)
    if ADD_TEXT_LEGEND:
        add_text(verticaldividers, "Vertical Dividers")
    save(verticaldividers, os.path.join(OUTPUT_FOLDER, "vertical_dividers.svg"), "VERICALDIVIDERS", PAPER_WIDTH, PAPER_HEIGHT)

    sides = Layer("Root")
    generate_sides(sides)
    if ADD_TEXT_LEGEND:
        add_text(sides, "Sides")
    save(sides, os.path.join(OUTPUT_FOLDER, "sides_and_foot.svg" if ADD_FOOT else "sides.svg"), "SIDES", PAPER_WIDTH, PAPER_HEIGHT)

    ledsandbuttons = Layer("Root")
    generate_ledsandbuttons(ledsandbuttons)
    if ADD_TEXT_LEGEND:
        add_text(ledsandbuttons, "Leds And Buttons")
    save(ledsandbuttons, os.path.join(OUTPUT_FOLDER, "leds_and_buttons.svg"), "LEDSANDBUTTONS", PAPER_WIDTH, PAPER_HEIGHT)

if __name__ == "__main__":
    main()
