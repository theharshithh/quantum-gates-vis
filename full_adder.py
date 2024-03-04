from qiskit import QuantumCircuit

def Full_Adder():
    # Create a Quantum Circuit with 5 qubits (3 input qubits and 2 output qubits)
    qc = QuantumCircuit(5, 2)
    
    # Input qubits: a, b, and carry-in
    qc.barrier()
    qc.x(0)  # Set the first input qubit a to 1 (change as needed)
    qc.x(1)  # Set the second input qubit b to 1 (change as needed)
    
    # Carry-in qubit
    qc.x(3)  # Set the carry-in qubit to 1 (change as needed)
    
    # Output qubits: sum and carry-out
    qc.barrier()
    
    # Apply operations to perform addition using QFT
    qc.cx(0, 4)  
    qc.cx(1, 4)  
    qc.cx(0, 2)  
    qc.cx(1, 2)  # Controlled-X gate (CNOT) between qubit b and the carry-out qubit
    
    # Apply XOR gate to calculate the sum
    qc.cx(3, 4)  # Controlled-X gate (CNOT) between the carry-in qubit and the sum qubit
    
    # Measure the sum and carry-out qubits
    qc.barrier()
    qc.measure(4, 0)  
    qc.measure(2, 1)  
    
    return qc

adder_circuit = Full_Adder()

# Draw the circuit
print(adder_circuit.draw())
