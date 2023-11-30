import numpy as np
import matplotlib.pyplot as plt

layer = "In1.Cu" # Layer 1; inside to outside
width = 0.1524 # = trace width = trace spacing = 6 mils, from Max Holliday's design
net = 3

# constraints
x_start = 68.4403 # left edge of pcb is 53.2003, gives 15.24 clearance
x_end = 134.4803 # right edge of pcb is 149.7203, gives 15.24 clearance
y_bottom = 133.8199 # bottom edge of pcb is 143.9799, gives 10.16 clearance
y_top = 62.6999 # top edge of pcb is 52.5399, gives 10.16 clearance

num_turns = 5
x_spacing = (x_end - x_start) / (2 * num_turns)
if x_spacing < width:
    print('Error')
y_spacing = y_top - y_bottom

x_left = np.arange(x_start, x_end - x_spacing, 2 * x_spacing) # x coord of left points
x_mid = np.arange(x_start + x_spacing, x_end, 2 * x_spacing) # x coord of middle points
x_right = np.arange(x_start + 2 * x_spacing, x_end, 2 * x_spacing) # x coord of right point


for i in range(num_turns): 
    print('(segment (start {:.4f} {:.4f}) (end {:.4f} {:.4f}) (width {:.4f}) (layer "{}") (net {}) (tstamp 1a34cc44-9e03-4e54-8129-5459824aed35))'.format(
        x_left[i], y_bottom, x_left[i], y_top, width, layer, net)) # left segment
    print('(segment (start {:.4f} {:.4f}) (end {:.4f} {:.4f}) (width {:.4f}) (layer "{}") (net {}) (tstamp 1a34cc44-9e03-4e54-8129-5459824aed35))'.format(
        x_left[i], y_top, x_mid[i], y_top, width, layer, net)) # top segment
    print('(segment (start {:.4f} {:.4f}) (end {:.4f} {:.4f}) (width {:.4f}) (layer "{}") (net {}) (tstamp 1a34cc44-9e03-4e54-8129-5459824aed35))'.format(
        x_mid[i], y_top, x_mid[i], y_bottom, width, layer, net)) # middle segment
    if i < num_turns - 1:
        print('(segment (start {:.4f} {:.4f}) (end {:.4f} {:.4f}) (width {:.4f}) (layer "{}") (net {}) (tstamp 1a34cc44-9e03-4e54-8129-5459824aed35))'.format(
            x_mid[i], y_bottom, x_right[i], y_bottom, width, layer, net)) # bottom segment

def check():
    for i in range(num_turns):
        plt.plot([x_left[i], x_left[i]], [y_bottom, y_top], 'bo', linestyle='solid')
        plt.plot([x_left[i], x_mid[i]], [y_top, y_top], 'bo', linestyle='solid')
        plt.plot([x_mid[i], x_mid[i]], [y_top, y_bottom], 'bo', linestyle='solid')
        if i < num_turns - 1:
            plt.plot([x_mid[i], x_right[i]], [y_bottom, y_bottom], 'bo', linestyle='solid')
    plt.show()

check()