import math

from quantum_circuit.utils import ground

class StateVector:

    def __init__(self, state=ground(3)):
        self._state = state
        self.history = [self._state]

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self.history.append(self.state)
        self._state = value

    @property
    def dimension(self):
        return len(self.state)   
    
    @property
    def number_of_qubits(self):
        return int(math.log2(self.dimension))

    def evolve(self, circuit):
        for item in circuit.gates:
            self.state = circuit.apply(item, self)