import numpy as np
from Helpers import find_inverse_kinematics
from PartB_hypertuning import cost, BEST_ALPHA


def main():
    destination = np.array((1.2, 0.8, 0.5))
    t1 = np.radians(-90)
    d2 = 0.5
    d3 = 1.0
    t4 = np.radians(-90)
    t5 = np.radians(90)
    t6 = np.radians(40)
    effectors = np.array([t1, d2, d3, t4, t5, t6])
    original_configuration = np.array([i for i in effectors])
    x_axis = [0]
    y_axis = [0]
    # The best Alpha I achieved was 17.5125
    find_inverse_kinematics(destination, effectors, 10000, cost=cost, ALPHA=BEST_ALPHA, ay_axis=y_axis,
                            ax_axis=x_axis, original_configuration=original_configuration)


if __name__ == "__main__":
    main()
