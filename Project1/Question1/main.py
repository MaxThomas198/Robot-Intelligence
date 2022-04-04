import matplotlib.pyplot as plt
import numpy as np
velocity = 20
length = 4
alpha = -np.pi / 6
rad_curve = 4 / np.tan(alpha)
Psi_dot = (velocity * np.tan(alpha)) / length
time_steps = [.01, 0.1, 1]
total_time = 10

colors = ['blue', 'orange', 'green']
line_width = 1
all_x = []
all_y = []
fig = plt.figure()
diagram = fig.add_subplot(121)
diagram_2 = fig.add_subplot(122)


def exactCoords(t):
    x_ext = rad_curve * np.cos(2 * np.pi * t / 2.173) + -rad_curve
    y_ext = -rad_curve * np.sin(2 * np.pi * t / 2.173)
    return x_ext, y_ext


def magnitude(x, y, x_2, y_2):
    return np.sqrt((x_2 - x) * (x_2 - x) + (y_2 - y) * (y_2 - y))


for i, t_step in enumerate(time_steps):
    x = 0
    y = 0
    psi = 0
    xlist = []
    ylist = []

    x_helper_list = []
    y_helper_list = []
    x_error_list = []
    y_error_list = []
    for dt in np.arange(0.0, total_time, t_step):
        xlist = np.append(xlist, x)
        ylist = np.append(ylist, y)
        x_error_list = np.append(x_error_list, dt)
        exact_coords = exactCoords(dt)
        x_help_list = np.append(x_helper_list, exact_coords[0])
        y_help_list = np.append(y_helper_list, exact_coords[1])
        y_error_list = np.append(y_error_list, magnitude(x, y, exact_coords[0], exact_coords[1]))
        psi = psi + Psi_dot * t_step
        x += -velocity * np.sin(psi) * t_step
        y += velocity * np.cos(psi) * t_step

    all_x = np.append(all_x, xlist)
    all_y = np.append(all_y, ylist)

    if i == 0:
        diagram.plot(x_helper_list, y_helper_list, 'c', label='continuous', linewidth=line_width)
    diagram.plot(xlist, ylist, colors[i], label=f'dt={t_step}', linewidth=line_width)
    diagram_2.plot(x_error_list, y_error_list, colors[i], linewidth=line_width)
    diagram.legend()

plt.show()
