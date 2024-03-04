from qiskit import QuantumCircuit

#half adder function
def half_adder():
    #defining values for the qiskit lib
    qc = QuantumCircuit(4, 2)
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.measure(2, 0)
    qc.measure(3, 1)
    return qc

#assigning the half adder
half_adder_circuit = half_adder()
print(half_adder_circuit.draw())
