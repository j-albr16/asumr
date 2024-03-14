from netpbmfile import NetpbmFile, imwrite
import numpy as np
import matplotlib.pyplot as plt

from dijkstra import MapGenerator


pgm_path = 'world.pgm'


def generate_map(dim, max_tunnels, max_length) -> np.ndarray:
    map_generator = MapGenerator(dim, max_tunnels, max_length, floor=255, wall=0, width=50)
    map_, start, end = map_generator()
    return map_


def generate_pgm(map_: np.ndarray, path: str):
    imwrite(path, map_)


def load_pgm(path: str) -> np.ndarray:
    with NetpbmFile(path) as pgm:
        return pgm.asarray()


if __name__ == '__main__':
    map_ = generate_map(500, 100, 150)
    generate_pgm(map_, pgm_path)
    loaded = load_pgm(pgm_path)
    plt.imshow(loaded, cmap='gray')
    plt.show()


