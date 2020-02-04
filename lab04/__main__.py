import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from itertools import cycle
import matplotlib.colors as clr

matplotlib.use('MacOSX')

colorpoints = [(1 - (1 - q) ** 4, c) for q, c in zip(np.linspace(0, 1, 50),
                                                     cycle(['#ffff88', '#000000',
                                                            '#ffaa00', ]))]
cmap = clr.LinearSegmentedColormap.from_list('mycmap',
                                             colorpoints, N=2048)


def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=200, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints * 1j), qmin:qmax:(qpoints * 1j)]
    c = p + 1j * q
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z ** 2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T


if __name__ == "__main__":
    plt.figure(figsize=(10, 10))
    image_mandelbrot = mandelbrot(-1.5, 0.5, 1500, -1, 1, 1500)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(image_mandelbrot, cmap=cmap, interpolation='none')
    plt.show()
