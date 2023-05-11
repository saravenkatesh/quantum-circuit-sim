import sys

from quantum_circuit.circuits import Circuit
from quantum_circuit.state_vectors import StateVector
from quantum_circuit.utils import ground


qasm_to_simulator_mapping = {
    'H': 'h',
    'CNOT': 'cx',
    'CZ': 'cz',
}


def qasm_qubit_to_int(qubit):
    """
    Convert a qasm qubit, which looks like q[0], to an index that 
    we can use to refer to that qubit
    """
    # TODO: make qubits 0-indexed
    return int(qubit[2]) + 1


def main():
    filename = sys.argv[1]
    with open(filename) as qasm_file:
        for line in qasm_file:
            line = line.strip().split(" ")
            if line[0] == 'qubits':
                number_of_qubits = int(line[1])
                circuit = Circuit(number_of_qubits)
                # TODO: allow other initial states as dictated by the QASM file
                initial_state = StateVector(ground(number_of_qubits))

            elif line[0] in qasm_to_simulator_mapping.keys():
                try:
                    qubits = [qasm_qubit_to_int(q) for q in line[1:]]
                    getattr(circuit, qasm_to_simulator_mapping[line[0]])(qubits)
                except Exception:
                    # TODO: handle specific exceptions
                    pass

    try:
        initial_state.evolve(circuit)
        return initial_state.state
    except Exception:
        # TODO: handle specific exceptions
        print("Failed to run task")


if __name__ == "__main__":
    print(main())