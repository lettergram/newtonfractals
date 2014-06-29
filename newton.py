# Example z^3 - 1 & z^2 - 2z - 2 fractal
# Written by Austin Walters

from PIL import Image

# -1 <= x <= 1
x_min = -1.0
x_max = 1.0

# -i <= y <= i
y_min = -1.0
y_max = 1.0

colors = [\
(180, 0, 30), (0, 180, 30), (0, 30, 180), \
(0, 190, 180), (180, 0, 175), (180, 255, 0), \
(155, 170, 180), (70, 50, 0), (255, 255, 255)]

def cubed(z): return z * z * z - 1.0
def dcubed(z): return 3.0 * (z*z)

def squared(z): return (z*z) - (2.0 * z) + 2.0
def dsquared(z): return 2.0 * z  - 2.0

def cubedplus(z): return z * z * z - 2.0 * z + 2.0
def dcubedplus(z): return 3.0 * z * z - 2.0

def fun(z): return (z*z*z*z*z*z) - (z*z*z) + 2.0
def dfun(z): return 6.0 * (z*z*z*z*z) - 3.0 * (z*z) 

def fifth(z): return (z*z*z*z*z) - (z)
def dfifth(z): return 5.0 * (z*z*z*z) - 1

def newtons_method(f, f_prime, z):
 
	# Fourty iterations for safe measure
    for i in range(40):
        zplus = z - f(z)/f_prime(z)

        # Checks for Overflow
        if abs(f(z)) > 10e10:
             return None
        # Checks for underflow
        if abs(f(z)) < 10e-14:
            return None
        # Checks for convergence
        if abs(zplus - z) < 10e-4:
            return z
        z = zplus
    return None
 
def draw(f, f_prime, img, size, img_name):
    
    roots = []
    for y in range(size):
        z_y = y * (y_max - y_min)/(size - 1) + y_min
        for x in range(size):
            z_x = x * (x_max - x_min)/(size - 1) + x_min
            root = newtons_method(f, f_prime, complex(z_x, z_y))
            if root:
                flag = False
                for test_root in roots:
                    if abs(test_root - root) < 10e-3:
                        root = test_root
                        flag = True
                        break
                if not flag:
                    roots.append(root)
            if root:
                img.putpixel((x, y), colors[roots.index(root)])
    print roots
    img.save(img_name, "PNG")
 
size = 1024
img = Image.new("RGB", (size, size), (255, 255, 255))
draw(lambda z: cubed(z), lambda z: dcubed(z), img, size, "fig1.png");
draw(lambda z: squared(z), lambda z: dsquared(z), img, size, "fig2.png");
draw(lambda z: fun(z), lambda z: dfun(z), img, size, "fig3.png");
draw(lambda z: cubedplus(z), lambda z: dcubedplus(z), img, size, "fig4.png");
draw(lambda z: fifth(z), lambda z: dfifth(z), img, size, "fig5.png");
