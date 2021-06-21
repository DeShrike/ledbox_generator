###########################
# LedBox Definitions
###########################

# all lengths are in mm

PAPER_WIDTH = 600
PAPER_HEIGHT = 450

# Number of boxes X * Y
GRID_W = 5 # 5 #5 #17
GRID_H = 8 # 8 #8 #13

# Material Thickness
THICKNESS = 3

# Inner size of one box
GRID_PART_WIDTH = 33.3333 - THICKNESS
GRID_PART_HEIGHT = 33.3333 - THICKNESS

PIN_SIZE = 10
PIN_WIDTH = THICKNESS + 0.2    # + 0.2 to more easily insert the pins in the holes
PIN_OUT_WIDTH = THICKNESS * 1.1   # * 1.1 so that the pins stick out a bit

WIRE_DIP_SIZE = 13
WIRE_DIP_WIDTH = THICKNESS * 2

LIP_WIDTH = THICKNESS

# Inner height of box
BOX_INNER_DEPTH = 30
BOX_OUTER_DEPTH = BOX_INNER_DEPTH + (2 * THICKNESS)

DIVIDER_HEIGHT = BOX_INNER_DEPTH
HORIZONTAL_DIVIDER_COUNT = GRID_H - 1
VERTICAL_DIVIDER_COUNT = GRID_W - 1

VERTICAL_DIVIDER_LENGTH = (GRID_PART_HEIGHT * GRID_H) + ((GRID_H - 1) * THICKNESS)
HORIZONTAL_DIVIDER_LENGTH = (GRID_PART_WIDTH * GRID_W) + ((GRID_W - 1) * THICKNESS)

SLID_DEPTH = DIVIDER_HEIGHT / 2
SLID_WIDTH = THICKNESS + 0.5

ADD_FOOT = True
FOOT_SIZE = 120 # 3 * BOX_INNER_DEPTH
FOOT_HEIGHT = 50 # BOX_INNER_DEPTH
# BOTTOM_MARGIN = FOOT_HEIGHT
FOOT_ANGLE = 5	# 5 Degrees

OUTPUT_FOLDER = "./out"
