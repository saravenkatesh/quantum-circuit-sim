import numpy as np
import math
import functools

HADAMARD = (1 / math.sqrt(2)) * np.array([[1, 1], [1, -1]])
IDENTITY = np.array([[1, 0], [0, 1]])

class GateImplementations:

    def hadamard(qubit, vector):
        matrix_tensor = [IDENTITY if i != qubit else HADAMARD for i in range(vector.number_of_qubits)]
        kronecker_product = functools.reduce(np.kron, matrix_tensor)
        return kronecker_product.dot(vector.state)

    def cx(self, qubits, vector):
        
        pass