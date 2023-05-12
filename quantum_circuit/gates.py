import numpy as np
import functools

from quantum_circuit.utils import create_controlled_gate, identity
from quantum_circuit.matrices import HADAMARD, NOT, PHASE_FLIP

class Gates:

    def hadamard(qubit, total_number_of_qubits):
        matrix_tensor = [identity(1) if i != qubit[0] else HADAMARD for i in range(1, total_number_of_qubits + 1)]
        return functools.reduce(np.kron, matrix_tensor)

    def cx(qubits, total_number_of_qubits):
        return create_controlled_gate(
            qubits, total_number_of_qubits, NOT
        )

    def cz(qubits, total_number_of_qubits):
        return create_controlled_gate(
            qubits, total_number_of_qubits, PHASE_FLIP
        )
