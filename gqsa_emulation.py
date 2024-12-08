from concurrent.futures import ProcessPoolExecutor
from gqsa import grover_algorithm
import numpy as np
import math
import matplotlib.pyplot as plt

def measure_state(probabilities, measure_count):
    states = np.arange(len(probabilities))
    return np.random.choice(states, size=measure_count, p=probabilities)


def single_run_grover(n_qubits, target_state, iterations, measure_count):
    probabilities = grover_algorithm(n_qubits, target_state, iterations)
    measurements = measure_state(probabilities, measure_count)
    target_index = int(target_state, 2)
    return np.sum(measurements != target_index)


def run_grover_parallel(n_qubits, target_state, iterations, runs, measure_count):
    with ProcessPoolExecutor() as executor:
        # Aufteilen in mehrere parallele Prozesse
        futures = [
            executor.submit(single_run_grover, n_qubits, target_state, iterations, measure_count)
            for _ in range(runs)
        ]
        # Ergebnisse zusammenführen
        fail_counts = sum(f.result() for f in futures)
    return fail_counts


def plot_accuracy_dot(data):
    """
    Plots a dot plot for accuracy percentages and shows exact values next to the points.

    Args:
    data (dict): Dictionary with keys as labels and values as accuracy percentages.

    Returns:
    None
    """
    # Sort data for better visualization
    labels = list(data.keys())
    values = list(data.values())

    print("Mapping:")
    for label, value in zip(labels, values):
        print(f"{label} Qubits: {value:.5f}")

    # Create the dot plot
    plt.figure(figsize=(8, 5))
    plt.scatter(values, labels, color='blue', edgecolor='black', s=100, zorder=2)

    # Add values next to the points
    for i, (label, value) in enumerate(zip(labels, values)):
        plt.text(value + 0.05, label, f"{value:.5f}", fontsize=9, verticalalignment='center')

    # Add gridlines and labels
    plt.axvline(x=100, color='red', linestyle='--', linewidth=1, label='100% Benchmark')
    plt.grid(axis='x', linestyle='--', linewidth=0.5, zorder=1)
    plt.xlabel('Accuracy (%)')
    plt.title('Accuracy Comparison (Dot Plot)')
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()

import json

def save_dict_to_file(dictionary, filename):
    """
    Saves a dictionary to a file in JSON format.

    :param dictionary: The dictionary to save
    :param filename: The name of the file to save the dictionary to
    """
    try:
        with open(filename, 'w') as file:
            json.dump(dictionary, file, indent=4)  # `indent=4` makes the JSON more readable
        print(f"Dictionary successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the dictionary: {e}")


if __name__ == "__main__":
    fail_by_qubit_count = {}

    print("Starting the simulation...")
    for n_qubits in range(5, 16):  # Beispiel: Weniger Qubits für schnelle Tests
        target_state = "0" * n_qubits
        iterations = int(math.pi / 4 * math.sqrt(2 ** n_qubits))
        runs = 10000
        measure_count = 100000

        # Parallelisierte Version
        fails = run_grover_parallel(n_qubits, target_state, iterations, runs, measure_count)
        fail_by_qubit_count[n_qubits] = 100 - fails / (runs * measure_count) * 100

        print(f"Qubits: {n_qubits}, Failures: {fails}")

    save_dict_to_file(fail_by_qubit_count, "fail_by_qubit_count.json")
    plot_accuracy_dot(fail_by_qubit_count)
