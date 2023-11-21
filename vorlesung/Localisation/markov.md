---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Markov Lokalisation

## Hintergrund


## Aufgabe

Ziel der Aufgabe ist die erfolgreiche Implementation der Markov Lokalisation.


Zur Aufgabe:

Gegeben ist ein 1D Array der länge `len`, auf welchem sich ein Marker nach rechts, links oder gar nicht bewegen kann. Es kann nach jedem Schritt eine Messung durchgeführt werden.

\begin{align*}
z \in \{wall, way\} \\
x \in \mathbb{N}^{<len} \\
u \in [-1, 0, 1]
\end{align*}

Folgendes sind die Wahrscheinlichkeiten für die Messwerte:

\begin{align*}
p(z='wall' | x=0) = 0.8 \\
p(z='way' | x=0) = 0.2 \\
p(z='wall' | x=len-1) = 0.8 \\
p(z='way' | x=len-1) = 0.2 \\
p(z='wall' | 0 < x < len-1) = 0.05 \\
p(z='way' | 0 < x < len-1) = 0.95
\end{align*}

Folgendes sind die erlaubten Bewegungsmuster des Markers:

- wenn er sich nicht am rand des Arrays befindet, kann er sich in jede Richtung `u` bewegen.
- wenn er sich am linken Rand befindet und nach links geht, verändert er die Position nicht
- wenn er sich am rechten Rand befindet und nach rechts geht, verändert er die Position nicht

Dieser Mechanismus ist duch folgende Wahrscheinlichkeitsverteilungen gegeben:

\begin{align*}
p( x_t = x_{t-1} |  u_t = 0 , x_{t-1}) = 1 \\

p( x_t = x_{t-1} |  u_t = -1 , x_{t-1} = 0) = 1 \\
p( x_t = x_{t-1} |  u_t = 1 , x_{t-1} = len-1) = 1 \\

p( x_t = x_{t-1}+1 |  u_t = 1 , x_{t-1} < len-1) = 1 \\
p( x_t = x_{t-1}-1 |  u_t = -1 , x_{t-1} > 0) = 1 \\

sonst 0
\end{align*}

Implementieren Sie die Klasse `Markov`, die die Methoden `p_x, p_z, predict, update` und `__call__` besitzt. Die `__call__` Methode soll für die Anzahl an Schritten die geglaubte Wahrscheinlichkeitsverteilung `bel(x_t)` berechnen.

```{code-cell} ipython3
import numpy as np
import random
import matplotlib.pyplot as plt
```

Folgendes ist das Environemnt, welches den Schritt entgegen nimmt und Sensordaten zurück gibt. Sie dürfen nicht auf die `_pos` Eigenschaft zugreifen.

```{code-cell} ipython3
:tags: ["hide-input"]
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

```



```{code-cell} ipython3

class Markov:

    def __init__(self, env):
        self.env = env
        self.bel = [1 / env.size for _ in range(env.size)]
        self.u = [1, 0, -1]
        self.x = list(range(env.size))
        self.z = ['wall', 'way']
        self.last = env.size - 1

    def p_z(self, z, x):
        """
        properbility distribution of sensor data z for given position x

        :param z: str (Sensor data 'wall' or 'way')
        :param x: int (Position)
        :return: int (propability [0,1])
        """
        # your code here

    def p_x(self, x_next, x, u) -> int:
        """
        properbility distribution of x_t given control-action u_t and last position x_t-1

        :param x_next: int (next position)
        :param x: int (last position)
        :param u: int (control-action 0,1 or -1)
        :return: int (propability [0,1])
        """
        # your code here
        pass

    def predict(self, x_next, u) -> int:
        # your code here
        pass

    def update(self, z, predicted_bel):
        # your code here
        pass

    def __call__(self, steps=10, visualizer=None):

        u = 0
        for i in range(steps):

            # your code here

            if visualizer is not None:
                visualizer(self.bel, self.env._pos)

            u = random.choice(self.u)

```

```{code-cell} ipython3
:tags: ["hide-input"]
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
```

```{code-cell} ipython3
:tags: ["hide-input"]

def main():
    steps = 12
    env = Environment(6)
    markov = Markov(env)
    visualizer = Visualizer(steps)
    markov(steps=steps, visualizer=visualizer)
    visualizer.plot()


if __name__ == '__main__':
    main()
```



