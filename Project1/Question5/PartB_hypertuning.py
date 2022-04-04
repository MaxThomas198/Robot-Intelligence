from Helpers import *
t1 = np.radians(-90)
d2 = 0.5
d3 = 1.0
t4 = np.radians(-90)
t5 = np.radians(90)
t6 = np.radians(40)
BEST_ALPHA = 17.5125
ACCEPTED_DISTANCE = 0.001


def delta_theta(arc_length):
    return arc_length / ACTUATOR_RADIUS


def get_config_cost(variables, original_configuration):
    c = 0
    for index in ds:
        c += delta_theta(np.absolute(original_configuration[index] - variables[index]))
    for index in ts:
        c += np.absolute(variables[index] - original_configuration[index])
    return c


def cost(p1, p2, currVariables, plot, ALPHA, y_axis, x_axis, original_configuration):
    new_vars_cost = get_config_cost(currVariables, original_configuration)
    if (new_vars_cost > ALPHA):
        return np.Infinity
    if plot:
        y_axis.append(new_vars_cost)
        x_axis.append(x_axis[-1] + 1)
    return distance(p1, p2)


def tune(cost_func, n, m, step, trials, effectors=np.array([t1, d2, d3, t4, t5, t6])):
    bests = {}
    for i in range(trials):
        print('i', i)
        best_alpha = n
        best_alpha_score = np.Infinity
        for ALPHA in np.arange(n, m, step):
            goal = np.array((1.2, 0.8, 0.5))
            effectors = effectors
            original_configuration = np.array([i for i in effectors])
            x_axis = [0]
            y_axis = [0]
            inverse_kinematics = find_inverse_kinematics(goal, effectors, 10000, cost=cost_func, ALPHA=ALPHA, ay_axis=y_axis,
                                               ax_axis=x_axis, original_configuration=original_configuration)
            if inverse_kinematics[1] < ACCEPTED_DISTANCE and y_axis[-1] < best_alpha_score:
                best_alpha = ALPHA
                best_alpha_score = y_axis[-1]
        if best_alpha in bests:
            bests[best_alpha] += 1
        else:
            bests[best_alpha] = 1
    weighted_avg_alpha = 0
    for i in bests:
        weighted_avg_alpha += i * bests[i]
    weighted_avg_alpha /= trials
    print(bests)
    print("The optimal alpha value is: %f" % weighted_avg_alpha)


if __name__ == "__main__":
    n = 20
    m = 30
    step = 0.2
    trials = 15
    tune(cost, n, m, step, trials)
