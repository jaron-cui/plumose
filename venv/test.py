import pya
import math

# RECOMMENDATION: REFER TO main.py INSTEAD

layout = pya.Layout()

# Define constants

global line_width
global DIAPHRAGM_WIDTH
global DIAPHRAGM_LENGTH
global COMB_MIN_LENGTH
global NUM_COMBS
global COMB_WIDTH
global FIN_WIDTH
global COMB_SPACING
global NUM_FRAME_UNIT
global FRAME_CURVE_RADIUS

global EDGE_CONNECT_LENGTH
global PAD_BOTTOM_HEIGHT
global OUTSIDE_SPACING
global PAD_WIDTH
global PAD_TOP_HEIGHT
global GENERAL_SMOOTH_RADIUS
global NUM_SIDE_BARS

DIAPHRAGM_WIDTH = 300.
DIAPHRAGM_LENGTH = 600.
COMB_MIN_LENGTH = 300.
NUM_COMBS = int(7)
COMB_WIDTH = 10.
FIN_WIDTH = 2.5
COMB_SPACING = 5.
NUM_FRAME_UNIT = int(4)
FRAME_CURVE_RADIUS = 30.

EDGE_CONNECT_LENGTH = 30.
PAD_BOTTOM_HEIGHT = 20.
OUTSIDE_SPACING = 10.
PAD_WIDTH = 100.
PAD_TOP_HEIGHT = 100.
GENERAL_SMOOTH_RADIUS = 10.
NUM_SIDE_BARS = int(8)
'''
DIAPHRAGM_WIDTH = 300.
DIAPHRAGM_LENGTH = 600.
COMB_MIN_LENGTH = 300.
NUM_COMBS = int(4)
COMB_WIDTH = 12.
FIN_WIDTH = 12.
COMB_SPACING = 15.


'''
COMB = layout.create_cell("COMB")
combs = layout.layer(11, 0)
disc = layout.layer(10, 0)
d = layout.create_cell("d")
out = layout.layer(9, 0)
OUT = layout.create_cell("OUT")
CHIP = layout.create_cell("CHIP")
layer_map = {COMB: out, d: disc, OUT: out, CHIP: out
             }  # , FIN: combs, FRAME_UNIT: diaphragm}


def um(n):
    return n * 1000


def add(cell, object):
    cell.shapes(layer_map[cell]).insert(object)


def arr_to_points(xo, yo, arr):
    translated = []
    for point in arr:
        translated.append(pya.Point(um(point[0] + xo), um(point[1] + yo)))
    return translated


def polygon(xo, yo, points):
    return pya.SimplePolygon(arr_to_points(xo, yo, points))


def get_path(xo, yo, points, line_width):
    path = pya.Path(arr_to_points(xo, yo, points), um(line_width))
    path.end_ext = um(line_width) / 2
    path.bgn_ext = um(line_width) / 2
    return path


def get_arc(xo, yo, xs, ys, r, sub, a1, a2, line_width):
    points = []
    div = (a2 - a1) / sub
    for n in range(sub + 1):
        x = r * math.cos(a1 + n * div) * xs
        y = r * math.sin(a1 + n * div) * ys
        points.append([x, y])
    return get_path(xo, yo, points, line_width)


def make_pixart(dest, xo, yo, scale, pixels):
    width = len(pixels[0])
    height = len(pixels)
    for y in range(height):
        for x in range(width):
            if (pixels[y][x] == 1):
                xi = x * scale + xo
                yi = yo - y * scale
                add(dest, polygon(xi, yi, [[0, 0], [0, scale], [scale, scale], [scale, 0]]))


nt = lambda grid: lambda dest, xo, yo, scale: make_pixart(dest, xo, yo, scale, grid)
n0 = nt([[0, 1, 1, 1, 0],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 1, 1, 1, 0]])
n1 = nt([[0, 0, 1, 0, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 1, 1, 0]])
n2 = nt([[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 1, 1, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]])
n3 = nt([[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 1, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 0]])
n4 = nt([[0, 0, 0, 1, 0],
         [0, 0, 1, 1, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 0, 0, 1, 0]])
n5 = nt([[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 0]])
n6 = nt([[0, 0, 1, 1, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 0]])
n7 = nt([[1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 1, 0, 0, 0]])
n8 = nt([[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 0]])
n9 = nt([[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0]])
numbers = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]
lA = nt([[0, 0, 1, 0, 0],
         [0, 1, 0, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1]])
lB = nt([[1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1]])
lC = nt([[0, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 1, 1, 1, 0]])
lD = nt([[1, 1, 1, 1, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 0]])
lE = nt([[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1]])
lF = nt([[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 1, 1, 1, 0],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0],
         [1, 0, 0, 0, 0]])


def make_label(dest, xo, yo, starting, number, box_only):
    if (starting == -1):
        return
    width = 560
    height = 320
    digits = []
    for digit in str(number):
        digits.append(numbers[int(digit)])
    if box_only:
        add(dest, polygon(xo, yo, [[0, 0], [-width, 0], [-width, height], [0, height]]))
        return
    add(dest, get_path(xo, yo, [[0, 0], [-width, 0], [-width, height], [0, height], [0, 0]], 4.))
    scale = 15
    for n in range(len(digits) + 1):
        character = [lA, lB, lC, lD, lE, lF][(number - starting) % 6]
        if (n < len(digits)):
            character = digits[n]
        character(dest, xo - width + 54 + n * 95, yo + height - 120, scale)


def make_design(dest, xo, yo, starting, num, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_MIN_LENGTH, NUM_COMBS,
                COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS, EDGE_CONNECT_LENGTH,
                PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                BACKSIDE_MARGIN):
    def addmag(x, d):
        if x > 0:
            return x + d
        else:
            return x - d

    def submag(x, d):
        return addmag(x, -d)

    def maxmag(a, b):
        if abs(b) > abs(a):
            return b
        else:
            return a

    # FIN = layout.create_cell("FIN")
    # FRAME_UNIT = layout.create_cell("FRAME_UNIT")

    # diaphragm = layout.layer(10, 0)

    # top = layout.layer(1, 0)

    # adjusting parameters to neater values
    DIAPHRAGM_LENGTH = math.ceil((DIAPHRAGM_LENGTH - COMB_WIDTH * 2) / NUM_COMBS) * NUM_COMBS + COMB_WIDTH * 2

    def path(xo, yo, points):
        return get_path(xo, yo, points, line_width)

    def arc(xo, yo, xs, ys, r, sub, a1, a2):
        return get_arc(xo, yo, xs, ys, r, sub, a1, a2, line_width)

    '''
    def path(points):
        return path(0, 0, points)'''

    '''def instance(cell, x, y):
        return pya.CellInstArray()'''

    def comb_interval(scale):
        return (abs(scale) * (DIAPHRAGM_LENGTH - COMB_WIDTH)) / (NUM_COMBS - 1)

    COMB_INTERVAL = (DIAPHRAGM_LENGTH - COMB_WIDTH) / (NUM_COMBS - 1)
    FIN_LENGTH = COMB_INTERVAL - COMB_WIDTH - COMB_SPACING * 2
    FIN_INTERVAL = 2 * FIN_WIDTH + 2 * COMB_SPACING

    # create FIN cell
    def make_fin(dest, xo, yo, xs, ys):
        x = (FIN_WIDTH / 2) * xs
        y = (FIN_LENGTH / 2) * ys
        if xs < 0:
            x += line_width / 2
        else:
            x -= line_width / 2
        if ys < 0:
            y += line_width / 2
        else:
            y -= line_width / 2
        if FIN_WIDTH == line_width:
            add(dest, path(xo, yo, [[x, y], [x, -y]]))
        else:
            add(dest, path(xo, yo, [[x, y], [x, -y], [-x, -y], [-x, y], [x, y]]))

    COMB_LENGTH = (math.ceil(COMB_MIN_LENGTH / FIN_INTERVAL) * FIN_INTERVAL - line_width / 2)

    # create COMB cell
    def make_comb(dest, xo, yo, xs, ys):
        x = (COMB_LENGTH + line_width / 2) * xs
        if xs < 0:
            x += line_width / 2
        else:
            x -= line_width / 2
        y = COMB_WIDTH / 2 * ys
        if ys < 0:
            y += line_width / 2
        else:
            y -= line_width / 2
        add(dest, path(xo, yo, [[0, y], [x, y], [x, -y], [0, -y]]))
        for n in range(math.ceil(COMB_MIN_LENGTH / FIN_INTERVAL)):
            x = (FIN_INTERVAL * (n + 1) - FIN_WIDTH / 2) * xs + xo
            y = yo
            make_fin(dest, x, y, xs, ys)

    def make_end_comb(dest, xo, yo, xs, ys):
        def make_end_fin(dest, xo, yo, xs, ys):
            x = (FIN_WIDTH / 2) * xs
            y = (FIN_LENGTH / 2) * ys
            y2 = COMB_WIDTH / 2 * ys
            if xs < 0:
                x += line_width / 2
            else:
                x -= line_width / 2
            if ys < 0:
                y += line_width / 2
                y2 += line_width / 2
            else:
                y -= line_width / 2
                y2 -= line_width / 2
            if FIN_WIDTH == line_width:
                add(dest, path(xo, yo, [[x, y], [x, -y2]]))
            else:
                add(dest, path(xo, yo, [[x, y], [x, -y2], [-x, -y2], [-x, y], [x, y]]))

        x = (COMB_LENGTH + line_width / 2) * xs
        if xs < 0:
            x += line_width / 2
        else:
            x -= line_width / 2
        y = COMB_WIDTH / 2 * ys
        if ys < 0:
            y += line_width / 2
        else:
            y -= line_width / 2
        add(dest, path(xo, yo, [[0, y], [x, y], [x, -y], [0, -y]]))
        for n in range(math.ceil(COMB_MIN_LENGTH / FIN_INTERVAL)):
            x = (FIN_INTERVAL * (n + 1) - FIN_WIDTH / 2) * xs + xo
            y = yo
            make_end_fin(dest, x, y, xs, ys)

    def make_comb_column(dest, xo, yo, xs, ys):
        x1 = addmag((COMB_LENGTH + COMB_SPACING) * xs, line_width) + xo
        x2 = (COMB_LENGTH + COMB_SPACING + COMB_WIDTH) * xs + xo
        # generate the diaphragm combs
        for n in range(NUM_COMBS):
            x = xo
            y = (comb_interval(xs) * n - DIAPHRAGM_LENGTH / 2 + COMB_WIDTH / 2) * ys + yo
            make_comb(dest, x, y, xs, ys)
            # adding lip support
            rad = addmag(submag(COMB_INTERVAL, COMB_WIDTH) * ys, line_width)
            yi = y - rad / 2
            interval = rad / (NUM_SIDE_BARS - 1)
            for m in range(1, NUM_SIDE_BARS):
                yc = m * interval
                add(dest, path(0, yi, [[x1, yc], [x2, yc]]))

        # generate the ending combs
        x = addmag((COMB_LENGTH + FIN_INTERVAL / 2 - FIN_WIDTH) * xs, line_width / 2)
        y = (comb_interval(xs) * -.5 - DIAPHRAGM_LENGTH / 2 + COMB_WIDTH / 2) * ys
        make_end_comb(dest, x + xo, y + yo, -xs, ys)
        make_end_comb(dest, x + xo, yo - y, -xs, -ys)
        # add lip support
        x1 = addmag(x, line_width / 2) + xo
        x2 = addmag(x, COMB_WIDTH * abs(xs) - line_width / 2) + xo
        yoff = submag(COMB_WIDTH / 2 * ys, line_width / 2)
        add(dest, path(0, y + yo, [[x1, yoff], [x2, yoff]]))
        add(dest, path(0, y + yo, [[x1, -yoff], [x2, -yoff]]))
        add(dest, path(0, yo - y, [[x1, yoff], [x2, yoff]]))
        add(dest, path(0, yo - y, [[x1, -yoff], [x2, -yoff]]))

        # generate the receiving combs
        for n in range(NUM_COMBS - 1):
            y = (comb_interval(xs) * (n + .5) - DIAPHRAGM_LENGTH / 2 + COMB_WIDTH / 2) * ys + yo
            make_comb(dest, x + xo, y, -xs, ys)
            # add lip support
            x1 = addmag(x, line_width / 2) + xo
            x2 = addmag(x, COMB_WIDTH * abs(xs) - line_width / 2) + xo
            add(dest, path(0, y, [[x1, yoff], [x2, yoff]]))
            add(dest, path(0, y, [[x1, -yoff], [x2, -yoff]]))

    def make_diaphragm_outline(dest, xo, yo, xs, ys):
        # make diaphragm outline
        x = DIAPHRAGM_WIDTH / 2 * xs
        y = DIAPHRAGM_LENGTH / 2 * ys
        if xs < 0:
            x += line_width / 2
        else:
            x -= line_width / 2
        if ys < 0:
            y += line_width / 2
        else:
            y -= line_width / 2
        add(dest, path(xo, yo, [[x, y], [x, -y], [-x, -y], [-x, y], [x, y]]))

    w = DIAPHRAGM_WIDTH / 2 - COMB_WIDTH
    yr = DIAPHRAGM_LENGTH - COMB_WIDTH * 2 + line_width
    h = yr / NUM_FRAME_UNIT

    def make_support_box(dest, xo, yo, xs, ys):
        sub = 10
        x = w * xs
        y = h * ys

        # construct frame
        add(dest, path(xo, yo, [[0, 0], [0, y], [x, y], [x, 0], [0, 0]]))
        # construct corner arcs
        add(dest, arc(xo, yo, xs, ys, FRAME_CURVE_RADIUS, sub, 0, math.pi / 2))
        add(dest, arc(xo, y + yo, xs, ys, FRAME_CURVE_RADIUS, sub, -math.pi / 2, 0))
        add(dest, arc(x + xo, y + yo, xs, ys, FRAME_CURVE_RADIUS, sub, math.pi, math.pi * 3 / 2))
        add(dest, arc(x + xo, yo, xs, ys, FRAME_CURVE_RADIUS, sub, math.pi / 2, math.pi))

        dx = FRAME_CURVE_RADIUS / math.sqrt(2) * xs
        dy = FRAME_CURVE_RADIUS / math.sqrt(2) * ys
        add(dest, path(xo, yo, [[dx, dy], [x - dx, y - dy]]))
        add(dest, path(xo, yo, [[dx, y - dy], [x - dx, dy]]))

    def make_diaphragm_structure(dest, xo, yo, xs, ys):
        x = submag(COMB_WIDTH * xs * xs, line_width / 2)
        y = submag(DIAPHRAGM_LENGTH / 2 * ys, line_width / 2)
        add(dest, path(xo, yo, [[-x, y], [-x, -y]]))
        add(dest, path(xo, yo, [[x, y], [x, -y]]))

        add(dest, path(xo, yo, [[0, y], [0, -y]]))

        x2 = 0

        def frame_unit_corner(a):
            return (DIAPHRAGM_LENGTH / 2 - COMB_WIDTH - a * h) * ys + line_width / 2

        for n in range(NUM_FRAME_UNIT):
            y = frame_unit_corner(n + 1)
            # make right side structural supports
            make_support_box(dest, x + xo, y + yo, 1, 1)
            # make left side structural supports
            make_support_box(dest, xo - x, y + yo, -1, 1)
            # make arc connectors
            rad = FRAME_CURVE_RADIUS * ys
            add(dest, path(xo, yo, [[-x, y + rad], [x, y + rad]]))
            add(dest, path(xo, yo, [[-x, frame_unit_corner(n) - rad], [x, frame_unit_corner(n) - rad]]))
            # make frame unit connectors
            x2 = DIAPHRAGM_WIDTH / 2 * xs - line_width / 2
            add(dest, path(xo, yo, [[-x2, y], [x2, y]]))
        y = frame_unit_corner(0)
        add(dest, path(xo, yo, [[-x2, y], [x2, y]]))

        # add edge connectors for arcs
        length = COMB_WIDTH * xs - line_width

        def add_edge_connectors(x, y):
            add(dest, path(xo, yo, [[x, y], [x, y + length]]))
            add(dest, path(xo, yo, [[x, -y], [x, -y - length]]))
            add(dest, path(xo, yo, [[-x, y], [-x, y + length]]))
            add(dest, path(xo, yo, [[-x, -y], [-x, -y - length]]))

        add_edge_connectors((COMB_WIDTH + FRAME_CURVE_RADIUS) * xs - line_width / 2, y)
        add_edge_connectors((DIAPHRAGM_WIDTH / 2 - FRAME_CURVE_RADIUS) * xs - line_width / 2, y)

    def make_pad(dest, xo, yo, xs, ys):
        x = xo
        y = addmag(EDGE_CONNECT_LENGTH * ys, line_width / 2) + yo
        add(dest, path(0, 0, [[x, yo], [x, y]]))
        xrad = GENERAL_SMOOTH_RADIUS * xs
        yrad = GENERAL_SMOOTH_RADIUS * ys
        sub = 7

        # add smoothing arcs
        y2 = submag(yrad, line_width / 2) + yo
        add(dest, arc(x - xrad, y2, xs, ys, GENERAL_SMOOTH_RADIUS, sub, math.pi * 3 / 2, math.pi * 2))
        add(dest, arc(x + xrad, y2, -xs, ys, GENERAL_SMOOTH_RADIUS, sub, math.pi * 3 / 2, math.pi * 2))
        add(dest, arc(x - xrad, y - yrad, xs, -ys, GENERAL_SMOOTH_RADIUS, sub, math.pi * 3 / 2, math.pi * 2))
        add(dest, arc(x + xrad, y - yrad, -xs, -ys, GENERAL_SMOOTH_RADIUS, sub, math.pi * 3 / 2, math.pi * 2))

        # create pad outline
        w = submag(PAD_WIDTH / 2 * xs, line_width / 2)
        h = submag(PAD_BOTTOM_HEIGHT * ys, line_width)
        add(dest, path(x, y, [[-w, h], [w, h]]))
        add(dest, path(x, y, [[-w, h], [w, 0]]))
        add(dest, path(x, y, [[-w, 0], [w, h]]))
        add(dest, path(x, y, [[-w, 0], [w, 0], [w, h], [-w, h], [-w, 0]]))

        # create pad solid
        w = addmag(w, line_width / 2)
        b = addmag(h, line_width / 2)
        h = submag((PAD_BOTTOM_HEIGHT + PAD_TOP_HEIGHT) * ys, line_width / 2)

        add(dest, polygon(x, y, [[-w, b], [w, b], [w, h], [-w, h], [-w, b]]))

    def make_external_apparatus_corner(dest, xo, yo, xs, ys):
        # making pad peripheral boxes X changed - no peripheral boxes
        x = (PAD_WIDTH / 2 + OUTSIDE_SPACING) * xs
        y = OUTSIDE_SPACING * ys
        x2 = DIAPHRAGM_WIDTH / 2 * xs
        y2 = (EDGE_CONNECT_LENGTH + PAD_BOTTOM_HEIGHT + PAD_TOP_HEIGHT) * ys
        # making reception wings
        xin = addmag((COMB_LENGTH + DIAPHRAGM_WIDTH / 2 + COMB_SPACING) * xs, line_width / 2)
        xout1 = (DIAPHRAGM_LENGTH / 2 + EDGE_CONNECT_LENGTH + PAD_BOTTOM_HEIGHT + PAD_TOP_HEIGHT) * xs
        xout2 = xin + PAD_TOP_HEIGHT * xs
        xout = maxmag(xout1, xout2) * 1.2
        yin = addmag((COMB_INTERVAL / 2 + OUTSIDE_SPACING) * ys, line_width / 2)
        yjunction = -DIAPHRAGM_LENGTH / 2 * ys
        add(dest, polygon(xo, yo, [[xout, yin], [x2, yin], [x2, y], [x, y], [x, y2], [xout, y2], [xout, yin]]))
        # side reception wing
        xin2 = addmag(xin, COMB_WIDTH)
        y3 = submag(yin - OUTSIDE_SPACING * ys, line_width / 2)
        add(dest, polygon(xo, yo, [[xin2, yjunction], [xin2, y3], [xout, y3], [xout, yjunction]]))
        # add lip
        xinp = addmag(xin, line_width / 2)
        xin2p = submag(xin2, line_width / 2)
        y3p = submag(y3, line_width / 2)
        yjuncp = addmag(yjunction, line_width / 2)
        add(dest, path(xo, yo, [[xinp, y3p], [xinp, yjuncp]]))
        add(dest, path(xo, yo, [[xin2p, yjuncp], [xin2p, y3p]]))

    def make_external_apparatus(dest, xo, yo, xs, ys):
        x = xo
        y = DIAPHRAGM_LENGTH / 2 * ys
        make_pad(dest, x, y + yo, 1, 1)
        make_pad(dest, x, yo - y, 1, -1)
        make_external_apparatus_corner(dest, x, y + yo, xs, ys)
        make_external_apparatus_corner(dest, x, y + yo, -xs, ys)
        make_external_apparatus_corner(dest, x, yo - y, xs, -ys)
        make_external_apparatus_corner(dest, x, yo - y, -xs, -ys)

    make_comb_column(dest, DIAPHRAGM_WIDTH / 2 + xo, yo, 1, 1)
    make_comb_column(dest, -DIAPHRAGM_WIDTH / 2 + xo, yo, -1, 1)
    make_diaphragm_outline(dest, xo, yo, 1, 1)
    make_diaphragm_structure(dest, xo, yo, 1, 1)
    make_external_apparatus(dest, xo, yo, 1, 1)
    make_label(dest, xo + chip_width / 2 - 150, yo - chip_height / 2 + 150, starting, num, True)


def make_alignment_corner(x, y, xs, ys):
    add(COMB, (polygon(x, y, [[0, 0], [96 * xs, 0], [96 * xs, 38 * ys], [92 * xs, 38 * ys], [92 * xs, 78 * ys],
                              [88 * xs, 78 * ys], [88 * xs, 88 * ys], [78 * xs, 88 * ys], [78 * xs, 92 * ys],
                              [38 * xs, 92 * ys], [38 * xs, 96 * ys], [0 * xs, 96 * ys]])))


def make_backside_corner(dest, xo, yo, xs, ys, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_WIDTH,
                         EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, COMB_INTERVAL, PAD_WIDTH, COMB_LENGTH, COMB_SPACING):
    margin = BACKSIDE_MARGIN

    y0 = (DIAPHRAGM_LENGTH / 2 + EDGE_CONNECT_LENGTH + PAD_BOTTOM_HEIGHT + margin) * ys
    y1 = (DIAPHRAGM_LENGTH / 2 + COMB_WIDTH + margin) * ys
    y2 = y1 + COMB_INTERVAL / 2 * ys

    x0 = (PAD_WIDTH / 2 + OUTSIDE_SPACING + margin) * xs
    x1 = (DIAPHRAGM_WIDTH / 2 - margin) * xs
    x2 = (DIAPHRAGM_WIDTH / 2 + COMB_LENGTH + COMB_SPACING + COMB_WIDTH + margin) * xs
    if abs(x1) <= abs(x0):
        add(dest, polygon(xo, yo, [[0, 0], [0, y0], [x1, y0], [x1, y2], [x2, y2], [x2, 0]]))
    else:
        add(dest, polygon(xo, yo, [[0, 0], [0, y0], [x0, y0], [x0, y1], [x1, y1], [x1, y2], [x2, y2], [x2, 0]]))


def make_backside(dest, xo, yo, xs, ys, FIN_WIDTH, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_WIDTH,
                  EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, NUM_COMBS, PAD_WIDTH, COMB_MIN_LENGTH, COMB_SPACING,
                  line_width):
    '''FIN_INTERVAL = 2 * FIN_WIDTH + 2 * COMB_SPACING
    COMB_LENGTH = (math.ceil(COMB_MIN_LENGTH / FIN_INTERVAL) * FIN_INTERVAL - line_width / 2)
    COMB_INTERVAL = (DIAPHRAGM_LENGTH - COMB_WIDTH) / (NUM_COMBS - 1)
    def corner(xs, ys):
        make_backside_corner(dest, xo, yo, xs, ys, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_WIDTH, EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, COMB_INTERVAL, PAD_WIDTH, COMB_LENGTH, COMB_SPACING)
    corner(xs, ys)
    corner(xs, -ys)
    corner(-xs, ys)
    corner(-xs, -ys)'''


chip_height = 3600
chip_width = 4600


def make_6set(xo, yo, start_num):
    w = chip_width * 2
    h = chip_height * 1.5
    add(CHIP, get_path(xo, yo, [[0, h], [w, h], [w, -h], [0, -h], [0, h]], 3.))
    x = xo + chip_width / 2
    y = yo + chip_height

    # DESIGN A
    line_width = 2.5
    DIAPHRAGM_WIDTH = 300.
    DIAPHRAGM_LENGTH = 600.
    COMB_MIN_LENGTH = 300.
    NUM_COMBS = int(7)
    COMB_WIDTH = 10.
    FIN_WIDTH = 2.5
    COMB_SPACING = 6.
    NUM_FRAME_UNIT = int(4)
    FRAME_CURVE_RADIUS = 30.

    EDGE_CONNECT_LENGTH = 30.
    PAD_BOTTOM_HEIGHT = 20.
    OUTSIDE_SPACING = 10.
    PAD_WIDTH = 100.
    PAD_TOP_HEIGHT = 200.
    GENERAL_SMOOTH_RADIUS = 10.
    NUM_SIDE_BARS = int(8)
    BACKSIDE_MARGIN = 50
    make_design(CHIP, x, y, start_num, start_num, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_MIN_LENGTH,
                NUM_COMBS,
                COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS, EDGE_CONNECT_LENGTH,
                PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                BACKSIDE_MARGIN)
    make_backside(COMB, x, y, 1, 1, FIN_WIDTH, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_WIDTH,
                  EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, NUM_COMBS, PAD_WIDTH, COMB_MIN_LENGTH, COMB_SPACING,
                  line_width)

    # DESIGN C
    line_width = 3.
    DIAPHRAGM_WIDTH = 300.
    DIAPHRAGM_LENGTH = 600.
    COMB_MIN_LENGTH = 300.
    NUM_COMBS = int(7)
    COMB_WIDTH = 10.
    FIN_WIDTH = 3.
    COMB_SPACING = 5.
    NUM_FRAME_UNIT = int(4)
    FRAME_CURVE_RADIUS = 30.

    EDGE_CONNECT_LENGTH = 100.
    PAD_BOTTOM_HEIGHT = 20.
    OUTSIDE_SPACING = 10.
    PAD_WIDTH = 100.
    PAD_TOP_HEIGHT = 200.
    GENERAL_SMOOTH_RADIUS = 10.
    NUM_SIDE_BARS = int(8)
    make_design(CHIP, x, y - 3600, start_num, start_num + 2, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                COMB_MIN_LENGTH,
                NUM_COMBS, COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS, EDGE_CONNECT_LENGTH,
                PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                BACKSIDE_MARGIN)
    make_backside(COMB, x, y - 3600, 1, 1, FIN_WIDTH, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_WIDTH,
                  EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, NUM_COMBS, PAD_WIDTH, COMB_MIN_LENGTH, COMB_SPACING,
                  line_width)

    # DESIGN E
    line_width = 3.
    DIAPHRAGM_WIDTH = 300.
    DIAPHRAGM_LENGTH = 600.
    COMB_MIN_LENGTH = 300.
    NUM_COMBS = int(7)
    COMB_WIDTH = 10.
    FIN_WIDTH = 11.
    COMB_SPACING = 5.
    NUM_FRAME_UNIT = int(4)
    FRAME_CURVE_RADIUS = 30.

    EDGE_CONNECT_LENGTH = 100.
    PAD_BOTTOM_HEIGHT = 20.
    OUTSIDE_SPACING = 10.
    PAD_WIDTH = 100.
    PAD_TOP_HEIGHT = 200.
    GENERAL_SMOOTH_RADIUS = 10.
    NUM_SIDE_BARS = int(8)
    make_design(CHIP, x, y - 2 * 3600, start_num, start_num + 4, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                COMB_MIN_LENGTH,
                NUM_COMBS, COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS, EDGE_CONNECT_LENGTH,
                PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                BACKSIDE_MARGIN)
    make_backside(COMB, x, y - 2 * 3600, 1, 1, FIN_WIDTH, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                  COMB_WIDTH,
                  EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, NUM_COMBS, PAD_WIDTH, COMB_MIN_LENGTH, COMB_SPACING,
                  line_width)

    # DESIGN B
    line_width = 3.
    DIAPHRAGM_WIDTH = 300.
    DIAPHRAGM_LENGTH = 600.
    COMB_MIN_LENGTH = 300.
    NUM_COMBS = int(7)
    COMB_WIDTH = 10.
    FIN_WIDTH = 3.
    COMB_SPACING = 5.
    NUM_FRAME_UNIT = int(4)
    FRAME_CURVE_RADIUS = 30.

    EDGE_CONNECT_LENGTH = 50.
    PAD_BOTTOM_HEIGHT = 20.
    OUTSIDE_SPACING = 10.
    PAD_WIDTH = 100.
    PAD_TOP_HEIGHT = 200.
    GENERAL_SMOOTH_RADIUS = 10.
    NUM_SIDE_BARS = int(8)
    make_design(CHIP, x + 4600, y, start_num, start_num + 1, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                COMB_MIN_LENGTH,
                NUM_COMBS, COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS, EDGE_CONNECT_LENGTH,
                PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                BACKSIDE_MARGIN)
    make_backside(COMB, x + 4600, y, 1, 1, FIN_WIDTH, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH, COMB_WIDTH,
                  EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, NUM_COMBS, PAD_WIDTH, COMB_MIN_LENGTH, COMB_SPACING,
                  line_width)

    # DESIGN D
    line_width = 2.5
    DIAPHRAGM_WIDTH = 300.
    DIAPHRAGM_LENGTH = 600.
    COMB_MIN_LENGTH = 300.
    NUM_COMBS = int(7)
    COMB_WIDTH = 10.
    FIN_WIDTH = 10.
    COMB_SPACING = 5.
    NUM_FRAME_UNIT = int(4)
    FRAME_CURVE_RADIUS = 30.

    EDGE_CONNECT_LENGTH = 50.
    PAD_BOTTOM_HEIGHT = 20.
    OUTSIDE_SPACING = 10.
    PAD_WIDTH = 100.
    PAD_TOP_HEIGHT = 200.
    GENERAL_SMOOTH_RADIUS = 10.
    NUM_SIDE_BARS = int(8)
    make_design(CHIP, x + 4600, y - 3600, start_num, start_num + 3, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                COMB_MIN_LENGTH,
                NUM_COMBS, COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS, EDGE_CONNECT_LENGTH,
                PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                BACKSIDE_MARGIN)
    make_backside(COMB, x + 4600, y - 3600, 1, 1, FIN_WIDTH, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                  COMB_WIDTH,
                  EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, NUM_COMBS, PAD_WIDTH, COMB_MIN_LENGTH, COMB_SPACING,
                  line_width)

    # DESIGN F
    line_width = 3.
    DIAPHRAGM_WIDTH = 300.
    DIAPHRAGM_LENGTH = 600.
    COMB_MIN_LENGTH = 300.
    NUM_COMBS = int(6)
    COMB_WIDTH = 16.
    FIN_WIDTH = 3.
    COMB_SPACING = 6.
    NUM_FRAME_UNIT = int(4)
    FRAME_CURVE_RADIUS = 36.

    EDGE_CONNECT_LENGTH = 30.
    PAD_BOTTOM_HEIGHT = 20.
    OUTSIDE_SPACING = 10.
    PAD_WIDTH = 100.
    PAD_TOP_HEIGHT = 200.
    GENERAL_SMOOTH_RADIUS = 10.
    NUM_SIDE_BARS = int(8)
    make_design(CHIP, x + 4600, y - 2 * 3600, start_num, start_num + 5, line_width, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                COMB_MIN_LENGTH, NUM_COMBS, COMB_WIDTH, FIN_WIDTH, COMB_SPACING, NUM_FRAME_UNIT, FRAME_CURVE_RADIUS,
                EDGE_CONNECT_LENGTH,
                PAD_BOTTOM_HEIGHT, OUTSIDE_SPACING, PAD_WIDTH, PAD_TOP_HEIGHT, GENERAL_SMOOTH_RADIUS, NUM_SIDE_BARS,
                BACKSIDE_MARGIN)
    make_backside(COMB, x + 4600, y - 2 * 3600, 1, 1, FIN_WIDTH, BACKSIDE_MARGIN, DIAPHRAGM_WIDTH, DIAPHRAGM_LENGTH,
                  COMB_WIDTH,
                  EDGE_CONNECT_LENGTH, PAD_BOTTOM_HEIGHT, NUM_COMBS, PAD_WIDTH, COMB_MIN_LENGTH, COMB_SPACING,
                  line_width)
    '''add(d, polygon(xo, yo, [[0, -h], [0, h], [w, h], [w, -h]]))
    processor = pya.ShapeProcessor()
    b = processor.boolean(layout, CHIP, out, layout, d, disc, CHIP.shapes(out),
                          pya.EdgeProcessor.mode_bnota(), True, True, True)'''


# add(COMB, get_arc(0, 0, 1, 1, 45000, 80, 0, 2 * math.pi, 1))


# make_6set(500, 0)
def distance(vertex1, vertex2):
    return math.sqrt(math.pow(vertex2[0] - vertex1[0], 2) + math.pow(vertex2[1] - vertex1[1], 2))


def fill_wafer(start_num, item, generate):
    def in_range(vertices):
        for vertex in vertices:
            if distance(vertex, [0, 0]) <= 45000:
                return True
        return False

    w = chip_width * 2
    h = chip_height * 3
    num_chips = 0
    for y in range(9):
        for x in range(10):
            corner_x = x * w - 45000 - 1000
            corner_y = y * h + chip_height * 1.5 - 45000 - 3500
            if in_range([[corner_x, corner_y - h / 2], [corner_x, corner_y + h / 2], [corner_x + w, corner_y + h / 2],
                         [corner_x + w, corner_y - h / 2]]):
                print("Constructing " + item + " #" + str(num_chips + 1) + " (" + str(x) + ", " + str(y) + ")...")
                #make_6set(corner_x, corner_y, start_num + num_chips * 6)
                generate(corner_x, corner_y, start_num, num_chips)
                num_chips += 1
                print("... Completed.")
    print("Constructed " + str(num_chips) + " " + item + "s.")


make_6set(0, 0, 1111)

def place_6set(x, y):
    cell = pya.CellInstArray(3, pya.Trans(pya.Point(um(x), um(y))))
    COMB.insert(cell)


def construct_chip(xo, yo, start_num, num_chips):
    print("  - Copying chip negative...")

    place_6set(xo, yo)

    print("    ... Done.")
    print("  - Labeling designs...")

    xo += chip_width
    yo += chip_height / 2
    make_label(COMB, xo - 150, yo + 150, start_num, start_num + num_chips * 6, False)
    xo += chip_width
    make_label(COMB, xo - 150, yo + 150, start_num, start_num + num_chips * 6 + 1, False)
    xo -= chip_width
    yo -= chip_height
    make_label(COMB, xo - 150, yo + 150, start_num, start_num + num_chips * 6 + 2, False)
    xo += chip_width
    make_label(COMB, xo - 150, yo + 150, start_num, start_num + num_chips * 6 + 3, False)
    xo -= chip_width
    yo -= chip_height
    make_label(COMB, xo - 150, yo + 150, start_num, start_num + num_chips * 6 + 4, False)
    xo += chip_width
    make_label(COMB, xo - 150, yo + 150, start_num, start_num + num_chips * 6 + 5, False)
    print("    ... Done.")
    # make_6set(xo, yo, start_num + num_chips * 6)

#construct_chip(0, 0, 4000, 0)

#construct_chip(0, chip_height * 3, 4000, 1)
#fill_wafer(1000, "chip", construct_chip)

'''add(d, polygon(0, 0, [[0, -5400], [-0, 5400], [9200, 5400], [9200, -5400]]))
processor = pya.ShapeProcessor()
b = processor.boolean(layout, COMB, combs, layout, d, disc, OUT.shapes(out),
                  pya.EdgeProcessor.mode_bnota(), True, True, True)'''
def generate_file(filename):
    layout.delete_cell(1)
    layout.delete_cell(2)
    layout.delete_cell(3)
    # Export GDS
    layout.write(filename)
