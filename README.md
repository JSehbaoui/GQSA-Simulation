# Grover Algorithm Simulation and Accuracy Plotting

## Project Overview

This project simulates **Grover's Quantum Search Algorithm** across varying numbers of qubits. It leverages parallel processing to evaluate performance and measure failure probabilities. The results are visualized as a **dot plot** showing the accuracy for different qubit counts.
This project is used in my paper in the context of the seminar at RWTH Aachen University.
---

## Features

1. **Simulation of Grover's Algorithm**  
   Implements a classical simulation of Grover's algorithm with configurable qubits, iterations, and runs.

2. **Parallel Processing**  
   Utilizes Python's `concurrent.futures.ProcessPoolExecutor` to speed up simulations.

3. **Accuracy Measurement**  
   Measures the algorithm's failure rates across multiple runs and computes the accuracy.

4. **Visualization**  
   Generates a dot plot to compare accuracies for different qubit counts.

5. **Result Saving**  
   Saves accuracy data to a JSON file for reproducibility and analysis.

---

## Requirements

To run the project, you need the following:

- Python 3.x
- Required libraries: `numpy`, `matplotlib`, `gqsa`, and `json`

Install dependencies via pip:

```bash
pip install numpy matplotlib
```

> **Note:** The `gqsa` library is assumed to provide the `grover_algorithm` function. Ensure it's properly installed.

---

## Project Structure

- **`single_run_grover`**: Executes a single Grover run and counts failures.  
- **`run_grover_parallel`**: Runs multiple Grover simulations in parallel for speedup.  
- **`plot_accuracy_dot`**: Plots the accuracies using a dot plot for visualization.  
- **`save_dict_to_file`**: Saves simulation results (accuracy data) to a JSON file.

---

## How to Run

1. Run the Python script:

```bash
python grover_simulation.py
```

2. The program will:
   - Simulate Grover's Algorithm for qubit counts from 5 to 15.
   - Compute and print failure counts and accuracies.
   - Save results to a file named `fail_by_qubit_count.json`.
   - Display a **dot plot** showing accuracy percentages.

---

## Example Output

### Console Output:

```
Starting the simulation...
Qubits: 5, Failures: 12345
Qubits: 6, Failures: 67890
...
Dictionary successfully saved to fail_by_qubit_count.json
```

### JSON File Example (`fail_by_qubit_count.json`):

```json
{
    "5": 99.876,
    "6": 98.234,
    "7": 97.123
}
```

### Dot Plot:
The generated plot shows accuracy values for each qubit count. A red dashed line highlights the **100% benchmark**.

---

## Configuration Parameters

You can customize the following parameters in the script:

- **`n_qubits`**: Range of qubits to simulate (default: 5–15).  
- **`iterations`**: Number of iterations based on Grover's algorithm formula.  
- **`runs`**: Number of parallel simulation runs (default: 10,000).  
- **`measure_count`**: Number of measurements to perform per run (default: 100,000).

---

## Dependencies

- **NumPy**: Random state measurements and probability handling.  
- **Matplotlib**: Visualization of accuracy data.  

---

## Notes

- This is a classical simulation of a quantum algorithm, and runtime increases with qubit count.  
- For accurate results, ensure sufficient **iterations** and **measurement counts** are configured.

---