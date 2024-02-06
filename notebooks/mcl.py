import numpy as np
import matplotlib.pyplot as plt


class MonteCarloLocalization:
    def __init__(self, num_particles, map_):
        self.num_particles = num_particles
        self.map = map_
        self.world_size = map_.world_size
        self.particles = np.random.uniform(0, self.world_size, size=(num_particles, 2))
        self.weights = np.ones(num_particles) / num_particles

    def move(self, motion):
        dx, dy = motion
        self.particles[:, 0] = (self.particles[:, 0] + dx) % self.world_size
        self.particles[:, 1] = (self.particles[:, 1] + dy) % self.world_size

    def _particle_distance(self, particle, measurement):
        """
        :param particle: 1x2 array
        :param measurement: (num_landmarks, 2) array
        returns the distance between particle and landmarks
        """
        particle_measurement = self.map.sense(particle)
        return np.linalg.norm(particle_measurement - measurement)

    def _normalize(self, weights):
        return weights / np.sum(weights)

    def sense(self, measurement):
        for i in range(self.num_particles):
            particle = self.particles[i]
            distance = self._particle_distance(particle, measurement)
            self.weights[i] *= self._measurement_prob(distance)

            if np.isnan(self.weights[i]):
                self.weights[i] = 0

        self.weights = self._normalize(self.weights)

    def resample(self):
        indices = np.random.choice(self.num_particles, size=self.num_particles, p=self.weights)
        self.particles = self.particles[indices]
        self.weights.fill(1.0 / self.num_particles)

    def _measurement_prob(self, distance):
        # Simulate the sensor noise
        prob = 1.0 / (distance + 1e-6)  # Add a small epsilon to avoid division by zero
        return prob

    def localize(self, motion, measurement):
        self.move(motion)
        self.sense(measurement)
        self.resample()


class Map:
    def __init__(self, world_size, view_radius, num_landmarks):
        self.world_size = world_size
        self.landmarks = self.generate_landmarks(num_landmarks)
        self.view_radius = view_radius

    def generate_landmarks(self, num_landmarks):
        return np.random.uniform(0, self.world_size, size=(num_landmarks, 2))

    def sense(self, true_position):
        """
        return the distances to the landmarks plus some noise
        """
        distances = np.linalg.norm(self.landmarks - true_position, axis=1)
        noised_distances = distances + np.random.normal(0, 2, size=len(distances))

        # set not viewable landmarks to infinity
        noised_distances[distances > self.view_radius] = self.world_size
        return noised_distances


class Agent:

    def __init__(self, world_size):
        self.pos = np.random.uniform(0, world_size, size=2)
        self.world_size = world_size

    def move(self, dx, dy):
        self.pos = (self.pos + np.array([dx, dy])) % self.world_size

    def sense(self, map_):
        return map_.sense(self.pos)


def simulate(steps, map_, num_particles=1000):

    # Example usage:
    agent = Agent(map_.world_size)
    mc_localization = MonteCarloLocalization(num_particles, map_)

    for _ in range(steps):
        agent.move(1, 1)
        measurement = agent.sense(map_)
        mc_localization.localize((1, 1), measurement)
        estimated_position = np.mean(mc_localization.particles, axis=0)
        yield agent.pos, mc_localization.particles, estimated_position

    print(f"Estimated position: {estimated_position}")
    print(f"True position: {agent.pos}")


def visualize():
    # simulation config
    view_radius = 10
    world_size = 100
    num_landmarks = 10
    steps = 30
    plot_every = steps // 9
    map_ = Map(world_size, view_radius, num_landmarks)

    # visualization
    fig, axs = plt.subplots(3, 3)

    ax_idx = 0
    for i, (pos, particles, estimated_position) in enumerate(simulate(steps, map_)):
        if i % plot_every != 0:
            continue

        if ax_idx >= 9:
            break

        ax = axs[ax_idx // 3, ax_idx % 3]
        ax.scatter(particles[:, 0], particles[:, 1], alpha=0.2)
        ax.scatter(pos[0], pos[1], c='r', marker='o')
        ax.scatter(map_.landmarks[:, 0], map_.landmarks[:, 1], c='g', marker='x')
        ax.scatter(estimated_position[0], estimated_position[1], c='b', marker='o')
        ax.set_title(f"Step {i}")
        ax.set_xlim(0, world_size)
        ax.set_ylim(0, world_size)

        ax_idx += 1

    fig.legend(['Particles', 'Agent', 'Landmarks', 'Estimated position'], loc='upper right')
    plt.suptitle(f"MCL (view_radius={view_radius})")
    plt.show()


if __name__ == "__main__":
    visualize()


