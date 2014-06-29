# Example z^3 - 1 & z^2 - 2z - 2 fractal
# Written by Austin Walters

import matplotlib.pyplot as plt
import numpy as np

# -1 <= x <= 1
x_min = -1.0
x_max = 1.0

# -i <= y <= i
y_min = -1.0
y_max = 1.0

colors = [(180, 0, 30), (0, 180, 30), (0, 30, 180)]

def cubed(z): return z * z * z - 1.0
def dcubed(z): return 3.0 * (z*z)

def squared(z): return (z*z) - (2.0 * z) + 2.0
def dsquared(z): return 2.0 * z  - 2.0

def fun(z): return (z*z) - 1.0
def dfun(z): return 2.0 * z

def newtons_method(f, f_prime, a, z):

    for i in range(40):
        zprime = f_prime(z)
        zplus = z - a*(f(z)/zprime)
        # Checks for underflow
        if abs(f(z)) < 10e-14:
            return None
        # Checks for convergence
        if abs(zplus - z) < 10e-4:
            return z
        z = zplus
    return None

def draw(f, f_prime, a, size):
    
    roots = [[0 for x in xrange(size)] for x in xrange(size)]

    for y in range(size):
        z_y = y * (y_max - y_min)/(size - 1) + y_min
        for x in range(size):
            z_x = x * (x_max - x_min)/(size - 1) + x_min
            
            string = ''
            string += str(z_x)
            if(z_y < 0):
                string += str(z_y)
            else:
                string += '+' + str(z_y)
            string += 'j'
            
            root = newtons_method(f, f_prime, a, complex(string))
            if root:
                roots[x][y] = colors(root)
    plt.pcolor(roots, cmp='RdBu', vmin=0, vmax=size)
    plt.show()

size = 512
draw(lambda z: cubed(z), lambda z: dcubed(z), 1, size);
draw(lambda z: squared(z), lambda z: dsquared(z), 1, size);
draw(lambda z: cubed(z), lambda z: dcubed(z), 2.1, size);
draw(lambda z: fun(z), lambda z: dcubed(z), 1.0 + complex(0, 1.0), size);
