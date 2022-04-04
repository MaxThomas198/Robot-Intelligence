from cartpole import CartPoleEnv


class BasicController:
    def choose(self, state):
        theta = state[2]
        angular_velocity = state[3]
        if abs(theta) < 0.06:
            return 0 if angular_velocity < 0 else 1
        else:
            return 0 if theta < 0 else 1


class AngleAndPositionCalc:
    def __init__(self, expected_value, kone, ktwo, kthree):
        self.expected_value = expected_value
        self.kone = kone
        self.ktwo = ktwo
        self.kthree = kthree
        self.prev_delta = 0
        self.integral_delta = 0

    def output(self, actual_value):
        delta = self.expected_value - actual_value
        one_comparison = delta * self.kone
        self.integral_delta += delta
        two_comparison = self.integral_delta * self.ktwo
        three_comparison = (delta - self.prev_delta) * self.kthree
        self.prev_delta = delta
        output = one_comparison + two_comparison + three_comparison
        return output


class AngleAndPositionFinder:
    def __init__(self, expected_position, expected_angle, kone_position, ktwo_position, kthree_position,
                 kone_angle, ktwo_angle, kthree_angle):
        self.position_pid = AngleAndPositionCalc(expected_position, kone_position, ktwo_position, kthree_position)
        self.angle_pid = AngleAndPositionCalc(expected_angle, kone_angle, ktwo_angle, kthree_angle)

    def chooseState(self, state):
        position = state[0]
        velocity = state[1]
        angle = state[2]
        angular_pole_velocity = state[3]
        pos_output = self.position_pid.output(position)
        angle_output = self.angle_pid.output(angle)
        action = 1 if (angle_output + pos_output) < 0 else 0

        return action


if __name__ == "__main__":
    env = CartPoleEnv()

    state = env.reset()
    done = False
    total_reward = 0
    algorithm = BasicController()
    data = [[], [], [], []]
    time_steps = []
    time = 0
    while not done:
        env.render()

        action = algorithm.choose(state)
        data[0].append(state[0])
        data[1].append(state[1])
        data[2].append(state[2])
        data[3].append(state[3])
        time_steps.append(time)
        time += 1
        new_state, reward, done, _ = env.step(action)

        state = new_state
        total_reward += reward

    env.close()
