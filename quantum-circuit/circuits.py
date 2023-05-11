import functools

from gate_implementations import GateImplementations


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

    def get_implementation(self, gate):
        return functools.partial(
            getattr(GateImplementations, gate['gate'], lambda: None), gate['qubits'],
        )
        
    def apply(self, gate, state):
        return self.get_implementation(gate)(state)