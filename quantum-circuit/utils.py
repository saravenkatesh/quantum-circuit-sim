from multiprocessing.sharedctypes import Value
import numpy as np
import functools

ZERO_PROJECTION = np.array([[1, 0], [0, 0]])
ONE_PROJECTION = np.array([[0, 0], [0, 1]])

def ground(n: int):
    return np.array([1] + (2**n - 1)*[0])

def identity(i: int):
    return np.identity(2**i)

def created_controlled_gate(qubits, dimension, gate):
    control, target = qubits[0], qubits[1]

    if control == target:
        raise ValueError("control and target cannot be the same qubit!")
    if not set(qubits).issubset(set(range(1, dimension + 1))):
        raise ValueError("control and target qubits are out of the state space!")

    identity_tensor = [
        identity(control - 1), 
        ZERO_PROJECTION, 
        identity(dimension - control)
    ]

    if control < target:
        gate_tensor = [
            identity(control - 1), 
            ONE_PROJECTION, 
            identity(target - control - 1), 
            gate, 
            identity(dimension - target)
        ]
    else:
        gate_tensor = [
            identity(target - 1), 
            gate, 
            identity(control - target - 1), 
            ONE_PROJECTION, 
            identity(dimension - control) 
        ]

    identity_kronecker_product = functools.reduce(np.kron, identity_tensor)
    gate_kronecker_product = functools.reduce(np.kron, gate_tensor)

    return identity_kronecker_product + gate_kronecker_product
