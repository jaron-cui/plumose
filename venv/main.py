import test as t

# NIH PROJECT - LOW NOISE MICROPHONES
#   PI: Dr. Ronald N. Miles
# PARAMETERIZED PLUMOSE DESIGN GDS GENERATOR
#   by JARON CUI, JULY/AUGUST 2021

# INFO:     Unfortunately, as I originally intended to use this program on my own, the interesting code in 'test'
#       would likely be a considerable pain to try and understand. This was my first time making a parameterized
#       design generator, so a lot of trial and error was involved, leading to poor practices, such as stuffing
#       massive walls of code into functions for short-term convenience.
#
#       GO TO LINE #60 TO BEGIN EDITING PARAMETERS
#
#           So, I made this main.py file to allow for more user-friendly generation of individual parameterized designs.
#       This file generates GDS files. If you would like to change this, you might be able to get away with rewriting
#       the following functions in test.py:
#
#           add (which adds filled objects to a layer)
#           get_path (which creates filled rectangular segments connecting the points in a list)
#           polygon (which creates filled polygons from a list of points)
#           generate_file (which writes the completed output file)

def fill_params(vals):
    names = ["line_width", "DIAPHRAGM_WIDTH", "DIAPHRAGM_LENGTH",
             "COMB_MIN_LENGTH", "NUM_COMBS", "COMB_WIDTH", "FIN_WIDTH", "COMB_SPACING", "NUM_FRAME_UNIT",
             "FRAME_CURVE_RADIUS", "EDGE_CONNECT_LENGTH", "PAD_BOTTOM_HEIGHT", "OUTSIDE_SPACING", "PAD_WIDTH",
             "PAD_TOP_HEIGHT", "GENERAL_SMOOTH_RADIUS", "NUM_SIDE_BARS", "BACKSIDE_MARGIN"]
    print(str(len(vals)) + " " + str(len(names)))
    params = {}
    for n in range(len(names)):
        params[names[n]] = vals[n]
    return params


def generate_design(params):
    line_width = params["line_width"]
    DIAPHRAGM_WIDTH = params["DIAPHRAGM_WIDTH"]
    DIAPHRAGM_LENGTH = params["DIAPHRAGM_LENGTH"]
    COMB_MIN_LENGTH = params["COMB_MIN_LENGTH"]
    NUM_COMBS = params["NUM_COMBS"]
    COMB_WIDTH = params["COMB_WIDTH"]
    FIN_WIDTH = params["FIN_WIDTH"]
    COMB_SPACING = params["COMB_SPACING"]
    NUM_FRAME_UNIT = params["NUM_FRAME_UNIT"]
    FRAME_CURVE_RADIUS = params["FRAME_CURVE_RADIUS"]
    EDGE_CONNECT_LENGTH = params["EDGE_CONNECT_LENGTH"]
    PAD_BOTTOM_HEIGHT = params["PAD_BOTTOM_HEIGHT"]
    OUTSIDE_SPACING = params["OUTSIDE_SPACING"]
    PAD_WIDTH = params["PAD_WIDTH"]
    PAD_TOP_HEIGHT = params["PAD_TOP_HEIGHT"]
    GENERAL_SMOOTH_RADIUS = params["GENERAL_SMOOTH_RADIUS"]
    NUM_SIDE_BARS = params["NUM_SIDE_BARS"]
    BACKSIDE_MARGIN = params["BACKSIDE_MARGIN"]
    t.make_design(t.COMB, 0, 0, -1, -1, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                  COMB_MIN_LENGTH, NUM_COMBS, COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS,
                  EDGE_CONNECT_LENGTH,
                  PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                  BACKSIDE_MARGIN)


# THESE ARE THE PARAMETERS FOR DESIGNS A AND D
paramsA = fill_params(
    [2.5, 300., 600., 300., int(7), 10., 2.5, 6., int(4), 30., 30., 20., 10., 100., 200., 10., int(8), 50.])
paramsD = fill_params(
    [2.5, 300., 600., 300., int(7), 10., 10., 5., int(4), 30., 50., 20., 10., 100., 200., 10., int(8), 50.])

# EXAMPLE OF EDITED PARAMETERS
paramsCustom = paramsA.copy()
paramsCustom["COMB_SPACING"] = 20.

# swap 'paramsCustom' out with 'paramsA', 'paramsD', or any other custom set of params. reload the file to see changes
# Note: KLayout makes this easy because it automatically detects the rewriting of the file and will ask to reload
generate_design(paramsCustom)

# generate the file or overwrite if already existing with given name
t.generate_file("Parameterized_Plumose.gds")
