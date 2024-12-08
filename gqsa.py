import math
import numpy as np

def initialize_qubits(n_qubits):
    states = 2 ** n_qubits
    amplitude = 1 / math.sqrt(states)
    return np.full(states, amplitude)


def apply_oracle(amplitudes, target_index):
    amplitudes[target_index] *= -1


def apply_diffuser(amplitudes):
    avg_amplitude = np.mean(amplitudes)
    amplitudes[:] = 2 * avg_amplitude - amplitudes


def grover_algorithm(n_qubits, target_state, iterations=None):
    if iterations is None:
        iterations = int(math.pi / 4 * math.sqrt(2 ** n_qubits))

    amplitudes = initialize_qubits(n_qubits)
    target_index = int(target_state, 2)

    for _ in range(iterations):
        apply_oracle(amplitudes, target_index)
        apply_diffuser(amplitudes)

    probabilities = amplitudes**2
    probabilities /= probabilities.sum()  # Normierung sicherstellen
    return probabilities