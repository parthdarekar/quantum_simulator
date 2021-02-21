#Function to check for errors during input
def error_check(num_qubits, gates, shots, q_state):
    valid_gates=['I','X','Y','Z','H','CNOT']
    num=2**num_qubits
    if len(gates)!=num_qubits:
        print("Error!! Number of gates does not match the number of qubits!")
        return 1
    for gate in gates:
        if gate.upper() not in valid_gates:
            print("Error!! Invalid gate!")
            return 1
    if len(q_state)!=0:
        if len(q_state)!=num:
            print("Error!! Size of previous and current circuit not equal ")
            return 1