import numpy as np
import matplotlib.pyplot as plt

# For Skid Steer Robot with a length of 50cm and a width of 30cm

class hw1():
    class skid_steer:

        def __init__(self, left_wheel_vels, right_wheel_vels, durations, width=.3):
            self.durations = durations
            self.lefts = left_wheel_vels
            self.rights = right_wheel_vels
            self.x_velocities = []
            self.y_velocities = []
            self.width = width
            self.angular_radius = []
            self.radius = []
            self.x_angle = np.pi / 4
            self.y_angle = np.pi / 4
            self.theta = 0

    def xVel(self, v_r, v_l, theta):
        self.x_velocities.append(-(v_r + v_l) / 2 * np.sin(theta))
        self.x_angle = np.sin(theta)
        print("xdots: ", self.x_velocities[-1])
        print("xdot sin: ", np.sin(theta))
        # -(v_r + v_l) / 2 * np.sin(theta)

    def yVel(self, v_r, v_l, theta):
        self.y_velocities.append((v_r + v_l) / 2 * np.cos(theta))
        print("theta: ", self.theta)
        print(("ydots: ", self.y_velocities[-1]))
        self.y_angle = np.cos(theta)
        print("ydot cos: ", np.cos(theta))
        # (v_r + v_l) / 2 * np.sin(theta)

    def rads(self):
        for duration, left, right in zip(self.durations, self.lefts, self.rights):
            if left == right:
                self.angular_radius.append(1000)
            else:
                self.angular_radius.append((right - left) / self.width)
                self.radius.append((left/self.angular_radius[-1]) + self.width/2)

    def x_and_y_velocities(self):
        for duration, left, right, radius in zip(self.durations, self.lefts, self.rights, self.angular_radius):
            print()
            print("duration: ", duration)
            if left == right:
                print("same")
                self.xVel(right, left, self.theta)
                self.yVel(right, left, self.theta)
            else:
                print("theta: ", self.theta)
                for t in range (duration):
                    self.theta += radius
                    self.xVel(right, left, self.theta)
                    self.yVel(right, left, self.theta)

    def print_current_self(self):
        print()
        print("lefts: ", self.lefts)
        print("rights: ", self.rights)
        print("durations: ", self.durations)
        print("angular_radius: ", self.angular_radius)
        print("radius: ", self.radius)
        print("width: ", self.width)
        print("xVel: ", self.x_velocities)
        print("yVel: ", self.y_velocities)
        print("theta: ", self.theta)
        print()

    def plot_robot(self):
        plt.figure()
        plt.clf()
        plt.title("Skid Steer Robot")
        plt.xlabel("x-Velocity")
        plt.ylabel("y-Velocity")
        plt.xlim([-1, 1])
        plt.ylim([-1, 1])
        plt.plot(self.xdots, self.y_velocities)
        plt.savefig("Plot of Durations for Skid Steer")
