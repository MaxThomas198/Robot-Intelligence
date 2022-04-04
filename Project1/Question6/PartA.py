import numpy as np
from Helpers import find_inverse_kinematics
from PartA_hypertuning import cost as p5_cost, BEST_ALPHA


def main():
    goal = np.array((1.2, 0.8, 0.5))
    variables = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    original_configuration = np.array([i for i in variables])
    ax_axis = [0]
    ay_axis = [0]
    find_inverse_kinematics(goal, variables, 100000, cost=p5_cost, ALPHA=BEST_ALPHA, ay_axis=ay_axis, ax_axis=ax_axis,
                            original_configuration=original_configuration)


if __name__ == "__main__":
    main()
