import numpy as np
import functools

from utils import create_controlled_gate, identity
from matrices import HADAMARD, NOT, PHASE_FLIP

class GateImplementations:

    def hadamard(qubit, vector):
        matrix_tensor = [identity(1) if i != qubit else HADAMARD for i in range(vector.number_of_qubits)]
        kronecker_product = functools.reduce(np.kron, matrix_tensor)
        return kronecker_product.dot(vector.state)

    def cx(qubits, vector):
        return create_controlled_gate(
            qubits, vector.number_of_qubits, NOT
        ).dot(vector.state)

    def cz(qubits, vector):
        return create_controlled_gate(
            qubits, vector.number_of_qubits, PHASE_FLIP
        ).dot(vector.state)