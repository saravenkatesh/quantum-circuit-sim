import numpy as np
import math
import functools

from utils import created_controlled_gate

HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
ZERO_PROJECTION = np.array([[1, 0], [0, 0]])
ONE_PROJECTION = np.array([[0, 0], [0, 1]])
NOT = np.array([[0, 1], [1, 0]])

def identity(i):
    return np.identity(2**i)

class GateImplementations:

    def hadamard(qubit, vector):
        matrix_tensor = [identity(1) if i != qubit else HADAMARD for i in range(vector.number_of_qubits)]
        kronecker_product = functools.reduce(np.kron, matrix_tensor)
        return kronecker_product.dot(vector.state)

    def cx(qubits, vector):
        return created_controlled_gate(
            qubits, vector.number_of_qubits, NOT
        ).dot(vector.state)

    def cz(qubits, vector):
        pass