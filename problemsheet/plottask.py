# This displays a plot of the functions:
# f(x) = x, g(x) = x^2 and h(x) = x^3.
# in the range [0, 4] on the one set of axes.
# Author: Jonathon Grealish
# References:
# https://matplotlib.org/2.0.2/users/pyplot_tutorial.html

import matplotlib.pyplot as plt # a collection of command style functions.
import numpy as np              # a collection used to work with numerical data.

# The plot() command will take an arbitrary pair of arguments (x and y).
# There is an optional third argument, the format string.
# This string indicates the color and line type of the plot, it concatenates a color string with a line style string.
# The axis() command takes an array of [xmin, xmax, ymin, ymax].
# All sequences are converted to numpy arrays internally:

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'b--', t, t**3, 'g--')
plt.show()