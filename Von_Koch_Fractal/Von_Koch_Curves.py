import numpy as np
import matplotlib.pyplot as plt

# Define a general transformation function that takes a line segment and returns new segments
def transform_segment(x, y, angle, transform_fn):
    new_x, new_y = transform_fn(x, y, angle)
    for i in range(len(new_x) - 1):
        plt.plot([new_x[i], new_x[i+1]], [new_y[i], new_y[i+1]], 'k')
    return new_x, new_y

# Define a transformation function for the von Koch curve
def von_koch_transform(x, y, angle):
    l = np.sqrt((x[1] - x[0]) ** 2 + (y[1] - y[0]) ** 2)
    theta = np.arctan2(y[1] - y[0], x[1] - x[0])

    x1 = x[0] + l / 3 * np.cos(theta)
    y1 = y[0] + l / 3 * np.sin(theta)

    x2 = x1 + l / 3 * np.cos(theta - angle)
    y2 = y1 + l / 3 * np.sin(theta - angle)

    x3 = x[0] + 2 * l / 3 * np.cos(theta)
    y3 = y[0] + 2 * l / 3 * np.sin(theta)

    return [x[0], x1, x2, x3, x[1]], [y[0], y1, y2, y3, y[1]]

# Recursive function to draw a fractal using a transformation function
def draw_fractal(N, x, y, angle, transform_fn):
    if N == 0:
        return
    x, y = transform_segment(x, y, angle, transform_fn)
    for i in range(len(x) - 1):
        draw_fractal(N - 1, [x[i], x[i + 1]], [y[i], y[i + 1]], angle, transform_fn)

if __name__ == '__main__':
    # Number of iterations
    N = 4

    # Length of the initial line segment
    r = 1/3

    # Initial direction of the line segment in radians (45 degrees)
    orientation = np.radians(0)

    angle = np.radians(60)
    # Initialize the vertices of the line segment
    x = [0, r * np.cos(orientation)]
    y = [0, r * np.sin(orientation)]

    # Set up the plot
    plt.figure(figsize=(8, 6))
    plt.axis('equal')

    # Call the recursive function to draw the fractal using the von Koch transformation
    draw_fractal(N, x, y, angle, von_koch_transform)

    # Display the plot
    plt.show()
