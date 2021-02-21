#Function to initialise the quantum state (in the ground state, i.e. ket(000...) )
from numpy import zeros
def ground_state(num_qubits):
    q_state=zeros(2**num_qubits, dtype=complex)
    q_state[0]=1
    return q_state