import numpy as np
from Helpers import find_inverse_kinematics
from PartB_hypertuning import cost, BEST_ALPHA


def main():
    destination = np.array((1.2, 0.8, 0.5))
    effectors = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    original_configuration = np.array([i for i in effectors])
    x_axis = [0]
    y_axis = [0]
    find_inverse_kinematics(destination, effectors, 250000, cost=cost, ALPHA=BEST_ALPHA, ay_axis=y_axis,
                            ax_axis=x_axis, original_configuration=original_configuration)


if __name__ == "__main__":
    main()
