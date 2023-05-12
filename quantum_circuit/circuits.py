import functools

from quantum_circuit.gates import Gates


class Circuit:

    CX = 'cx'
    CZ = 'cz'
    HAD = 'hadamard'
    
    def __init__(self, size=3):
        self.size = size
        self.gates = []

    def append_gate(self, gate, qubits):
        self.gates.append({'gate': gate, 'qubits': qubits})

    def cx(self, qubits):
        self.append_gate(self.CX, qubits)

    def cz(self, qubits):
        self.append_gate(self.CZ, qubits)

    def h(self, qubit):
        self.append_gate(self.HAD, qubit)

    def get_implementation(self, gate, number_of_qubits):
        return getattr(Gates, gate['gate'], lambda: None)(gate['qubits'], number_of_qubits)
        
    def apply(self, gate, state):
        return self.get_implementation(gate, state.number_of_qubits).dot(state.state)