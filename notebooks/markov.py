import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


class Environment:

    def __init__(self, size):
        self.arr = np.zeros(size)
        self.size = size
        self._pos = random.randint(0, size - 1)

    def step(self, u):
        if self._pos == 0 and u == -1 or self._pos == self.size - 1 and u == 1:
            return

        self._pos += u

    def sense(self):
        is_wall = self._pos == 0 or self._pos == self.size - 1

        if is_wall:
            return 'wall'
        else:
            return 'way'


class Agent:

    def __init__(self, env):
        self.env = env
        self.bel = [1 / env.size for _ in range(env.size)]
        self.u = [1, -1]
        self.x = list(range(env.size))
        self.z = ['wall', 'way']
        self.last = env.size - 1

    def p_z(self, z, x):
        if x in [0, self.last]:
            if z == 'wall':
                return 0.8
            else:
                return 0.2
        elif 0 < x < self.last:
            if z == 'wall':
                return 0.05
            else:
                return 0.95
        else:
            raise ValueError('x out of range')

    def p_x(self, x_next, x, u):
        # do not change state if u = 0
        if u == 0 and x_next == x:
            return 1
        # if in middle can move anywhere
        elif 0 < x < self.last and x_next == x + u:
            return 1
        # if at end only move left or stay
        elif x == self.last:
            if u == -1 and x_next == x - 1:
                return 1
            elif u == 1 and x_next == x:
                return 1
            else:
                return 0
        # if at start only move right or stay
        elif x == 0:
            if u == 1 and x_next == x + 1:
                return 1
            elif u == -1 and x_next == x:
                return 1
            else:
                return 0
        else:
            return 0

    def predict(self, x_next, u):
        """
        Predicts the next belief state given the current belief state and the action

        :param x_next: the next state
        :param u: the action
        """
        return sum([self.p_x(x_next, x, u) * self.bel[x] for x in self.x])

    def update(self, z, predicted_bel):
        """
        Updates the belief state given the current belief state and the observation

        :param z: the observation
        :param predicted_bel: the predicted belief state
        """
        self.bel = [self.p_z(z, x) * predicted_bel[x] for x in self.x]
        nu = 1 / sum(self.bel)
        self.bel = [nu * b for b in self.bel]

    def __iter__(self):
        self.steps = [0] + [random.choice(self.u)
                            for _ in range(self.num_steps - 1)]

        self.i = 0
        return self

    def __next__(self):
        if self.i < len(self.steps):

            u = self.steps[self.i]
            self.env.step(u)
            predicted_bel = [self.predict(x, u) for x in self.x]
            z = self.env.sense()
            self.update(z, predicted_bel)

            self.i += 1

            return self.bel, self.env._pos
        raise StopIteration

    def __call__(self, num_steps=9):
        self.num_steps = num_steps
        return self


def interpol_bel(bel, size):
    x = np.linspace(0, size, len(bel))
    y = bel
    f = interp1d(x, y, kind='nearest', fill_value='extrapolate')
    x_new = np.linspace(0, size, 100)
    y_new = f(x_new)
    return x_new, y_new


def visualize():
    env = Environment(6)
    agent = Agent(env)
    num_steps = 9
    size = agent.env.size - 1

    fig, axs = plt.subplots(num_steps // 3, 3, figsize=(10, 10))

    axs_flat = axs.flatten()
    for i, (bel, pos) in enumerate(agent(num_steps)):
        ax = axs_flat[i]

        x, y = interpol_bel(bel, size)
        ax.scatter(pos, 0, color='red')
        ax.plot(x, y, color='blue')
        ax.set_ylim(0, 1)
        ax.set_xlim(0, len(bel) - 1)
        ax.set_title(f'step {i}')
        ax.grid()

    plt.show()


if __name__ == '__main__':
    visualize()
