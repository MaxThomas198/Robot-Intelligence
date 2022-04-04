import numpy as np
ACTUATOR_RADIUS = 0.05
first_effector = 1.1
end_effector = 1.2
ts = np.array([0, 3, 4, 5])
ds = np.array([1, 2])


def random_step(curr_variables, quench=1):
    new_variables = np.array([i for i in curr_variables])
    for index in ts:
        new_variables[index] += np.pi * (np.random.rand() - 0.5) * 2 * quench
    for index in ds:
        new_variables[index] += (np.random.rand() - 0.5) * 0.05 * quench
        TMatrix(new_variables)
    return new_variables


def distance(p1, p2):  # distance between points
    return np.linalg.norm(p1 - p2,)


def cost(p1, p2, _, __, ___, ____, _____, ______,):  # needs to match more complex cost functions
    return distance(p1, p2)


def TMatrix(variables):
    def c(index):
        return np.cos(variables[index - 1])

    def s(index):
        return np.sin(variables[index - 1])

    def d(index):
        return variables[index - 1]

    r11 = c(1) * c(4) * c(5) * c(6) - c(1) * s(4) * s(6) + s(1) * s(5) * c(6)
    r21 = s(1) * c(4) * c(5) * c(6) - s(1) * s(4) * s(6) - c(1) * s(5) * s(6)
    r31 = -s(4) * c(5) * c(6) - c(4) * s(6)
    r12 = -s(1) * c(4) * c(5) * s(6) - c(1) * s(4) * c(6) - s(1) * s(5) * c(6)
    r22 = -s(1) * c(4) * c(5) * s(6) - s(1) * s(4) * c(6) + c(1) * s(5) * c(6)
    r32 = s(4) * c(5) * c(6) - c(4) * c(6)
    r13 = c(1) * c(4) * s(5) - s(1) * c(5)
    r23 = s(1) * c(4) * s(6) + c(1) * c(5)
    r33 = -s(4) * s(5)
    dx = c(1) * c(4) * s(5) * end_effector - s(1) * c(5) * end_effector - s(1) * d(3)
    dy = s(1) * c(4) * s(6) * end_effector + c(1) * c(5) * end_effector + c(1) * d(3)
    dz = -s(4) * s(5) * end_effector + first_effector + d(1)

    T = np.matrix([
        [r11, r12, r13, dx],
        [r21, r22, r23, dy],
        [r31, r32, r33, dz],
        [0, 0, 0, 1]
    ])
    return T


def find_inverse_kinematics(destination, effectors, iterations, cost=cost, ALPHA=None, ay_axis=None, ax_axis=None,
                            original_configuration=None, get_total_cost=None):
    x_axis = []
    y_axis = []
    total_cost = 0
    for i in range(1, iterations):

        currT = TMatrix(effectors)
        currPos = np.array((currT[0, 3], currT[1, 3], currT[2, 3]))
        currCost = cost(currPos, destination, effectors, True, ALPHA, ay_axis, ax_axis, original_configuration)
        newVars = random_step(effectors, quench=1 - (i * 1 / iterations))
        newT = TMatrix(newVars)
        newPos = np.array((newT[0, 3], newT[1, 3], newT[2, 3]))
        newCost = cost(newPos, destination, newVars, False, ALPHA, ay_axis, ax_axis, original_configuration)
        if currCost > newCost:
            effectors = newVars
            if get_total_cost: total_cost += get_total_cost(effectors, original_configuration)
        x_axis.append(x_axis[-1] + 1 if len(x_axis) > 0 else 1)
        y_axis.append(currCost)
    currT = TMatrix(effectors)
    currPos = np.array((currT[0, 3], currT[1, 3], currT[2, 3]))
    print("destination:", destination)
    print("final position:", currPos)
    print("distance to goal: %.5f m" % distance(currPos, destination))
    for i, j in enumerate(ts):
        print("theta %d: %.5f rad" % (j + 1, effectors[j]))
    print("d%d: %.5f m" % (1, first_effector))
    for i, j in enumerate(ds):
        print("d%d: %.5f m" % (j + 1, effectors[j]))
    print("d%d: %.5f m" % (6, end_effector))
    return [[x_axis, y_axis], distance(currPos, destination), [ax_axis, ay_axis], effectors, total_cost]
