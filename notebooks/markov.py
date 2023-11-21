import numpy as np
import random
import matplotlib.pyplot as plt


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


class Markov:

    def __init__(self, env):
        self.env = env
        self.bel = [1 / env.size for _ in range(env.size)]
        self.u = [1, 0, -1]
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
        return sum([self.p_x(x_next, x, u) * self.bel[x] for x in self.x])

    def update(self, z, predicted_bel):
        self.bel = [self.p_z(z, x) * predicted_bel[x] for x in self.x]
        nu = 1 / sum(self.bel)
        self.bel = [nu * b for b in self.bel]

    def __call__(self, steps=10, visualizer=None):

        u = 0

        for i in range(steps):

            self.env.step(u)
            predicted_bel = [self.predict(x, u) for x in self.x]
            z = self.env.sense()
            self.update(z, predicted_bel)

            visualizer(self.bel, self.env._pos)

            u = random.choice(self.u)


class Visualizer:

    def __init__(self, steps):
        self.data = []
        self.steps = steps

    def __call__(self, bel, pos):
        self.data.append((bel, pos))

    def plot(self):
        fig, axs = plt.subplots(self.steps // 3, 3, figsize=(10, 10))
        for i, ax in enumerate(axs.flatten()):
            bel, pos = self.data[i]
            ax.plot(bel)
            ax.scatter(pos, 0, color='red')
            ax.set_ylim(0, 1)
            ax.set_xlim(0, len(bel) - 1)
            ax.set_title(f'step {i}')
            ax.grid()
        plt.show()


def main():
    steps = 12
    env = Environment(6)
    markov = Markov(env)
    visualizer = Visualizer(steps)
    # markov(steps=10)
    markov(steps=steps, visualizer=visualizer)
    visualizer.plot()


if __name__ == '__main__':
    main()
