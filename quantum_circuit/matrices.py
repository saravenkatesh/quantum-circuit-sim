import math
import numpy as np

HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
ZERO_PROJECTION = np.array([[1, 0], [0, 0]])
ONE_PROJECTION = np.array([[0, 0], [0, 1]])
NOT = np.array([[0, 1], [1, 0]])
PHASE_FLIP = np.array([[1, 0], [0, -1]])