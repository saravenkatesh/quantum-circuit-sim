import numpy as np
import math
import functools

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
        if qubits[0] == qubits[1]:
            raise ValueError("the control qubit and the target qubit must be different!")

        if qubits[1] > qubits[0]:
            matrix_tensor_1 = [identity(qubits[0]-1), ZERO_PROJECTION, identity(vector.number_of_qubits - qubits[0])]
            matrix_tensor_2 = [identity(qubits[0]-1), ONE_PROJECTION, identity(qubits[1] - qubits[0] - 1), NOT, identity(vector.number_of_qubits - qubits[1])]
        if qubits[0] > qubits[1]:
            matrix_tensor_1 = [identity(qubits[0] - 1), ZERO_PROJECTION, identity(vector.number_of_qubits - qubits[0])]
            matrix_tensor_2 = [identity(qubits[1]-1), NOT, identity(qubits[0] - qubits[1] - 1), ONE_PROJECTION, identity(vector.number_of_qubits - qubits[0])]
        
        kronecker_product_1 = functools.reduce(np.kron, matrix_tensor_1)
        kronecker_product_2 = functools.reduce(np.kron, matrix_tensor_2)

        return (kronecker_product_1 + kronecker_product_2).dot(vector.state)