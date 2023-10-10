# Quantum Circuit Simulator

A library for simulating a quantum circuit.  Built initially to be a tutorial resource

## Set up

After cloning the repo, install poetry if you haven't already (mac/linux):

    curl -sSL https://install.python-poetry.org | python3 -

activate the virtual environment

    poetry shell

and install dependencies

    poetry install

To test your setup, cd into the root directory and run

    python3 scripts/transform_state_vector.py qasm_files/toy_example.cq

This takes in a simple QASM file preparing and entangling a state, and outputs the results of running
the corresponding circuit.

## Usage

### As a library

Only Hadamard, CX, and CZ gates are supported.  To build a circuit, instantiate a `Circuit` object from 
`quantum_circuits/circuits.py`.  Add gates Qiskit-style to your circuit:

    circuit = Circuit(3) # Create a circuit acting on 3 qubits
    circuit.cx([0, 3]) # Add a cx gate acting on the 3rd qubit, with control the 0th qubit
    circuit.h([1]) # Add a Hadamard gate acting on the 1st qubit

To evaluate a state vector on a circuit, instantiate a `StateVector` object from `quantum_circuit/state_vectors.py`

    state_vector = StateVector(state) # state is a vector of length 2^n, where n is the number of qubits
    state_vector.evolve(circuit)
    state_vector.state # holds the new state
    state_vector.history # holds a historical record of all states

### Reading Qasm Files
  
To read a QASM file from the root directory, run 

    python3 scripts/transform_state_vector.py [path/to/file]

Any instructions in the QASM file that are not state preparation or gate application will be ignored.
Note that this simulation only supports the Hadamard, CX, and CZ gates

## Resources

### Resources for quantum circuits:
[Qiskit tutorial](https://qiskit.org/documentation/tutorials/circuits/01_circuit_basics.html)


### Resources for tensor decomposition of single-qubit gates or controlled-single-qubit gates:
- [General decomposition](https://quantumcomputing.stackexchange.com/questions/4524/matrix-representation-and-cx-gate)
- [3-qubit system](https://quantumcomputing.stackexchange.com/questions/4252/how-to-derive-the-cnot-matrix-for-a-3-qubit-system-where-the-control-target-qu)


### Resources for QASM files:
[Quantum inspire](https://www.quantum-inspire.com/kbase/cqasm/)