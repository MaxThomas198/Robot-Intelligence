from itertools import permutations
from Helpers import *
from Question5.PartB_hypertuning import get_config_cost


def total_distance(start, positions):
    d = distance(start, positions[0])
    for pos in range(len(positions) - 1):
        d += distance(positions[pos], positions[pos + 1])
    return d


def find_shortest_path(startPos, destination):
    perms = list(permutations(destination))
    best = perms[0]
    best_distance = np.Infinity
    for perm in perms:
        new_distance = total_distance(startPos, perm)
        if new_distance < best_distance:
            best_distance = new_distance
            best = perm
    return best
tot = 0


def cost(p1, p2, currVariables, plot, ALPHA, ay_axis, ax_axis, original_configuration, tot=None):
    new_vars_cost = get_config_cost(currVariables, original_configuration)
    if tot: tot += new_vars_cost
    if plot:
        ay_axis.append(new_vars_cost)
        ax_axis.append(ax_axis[-1] + 1)
    return distance(p1, p2)


destination = np.array([
    np.array([1, 1, 1]),
    np.array([-1, 2, 1])
])
variables = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])  # t1, d2, d3, t4, t5, t6
newT = get_T_matrix(variables)
newPos = np.array((newT[0, 3], newT[1, 3], newT[2, 3]))
best = find_shortest_path(newPos, destination)
y_axis = [0]
x_axis = [0]
find_inverse_kinematics = find_inverse_kinematics(best[0], variables, 10000, cost=cost, original_configuration=[i for i in variables],
                                                  get_total_cost=get_config_cost, ay_axis=y_axis, ax_axis=x_axis)
next_move = find_inverse_kinematics[3]
total_dist = find_inverse_kinematics[4]
for i in range(len(best) - 1):
    find_inverse_kinematics = find_inverse_kinematics(best[i + 1], next_move, 10000, cost=cost,
                                                      original_configuration=[i for i in variables], get_total_cost=get_config_cost,
                                                      ay_axis=y_axis, ax_axis=x_axis)
    next_move = find_inverse_kinematics[3]
    total_dist += find_inverse_kinematics[4]
print("Optimal goals order: %s, %s" % (best[0], best[1]))
print("The total cost is %.3f" % total_dist)
