#Function to apply the desired operator onto the quantum state
import numpy as np
from operator_matrix import get_unit_matrix
from tensor_prod import calc_tensor_product

def apply_unit_operator(num_qubits, q_state, gates):
    
    #print(gates)
    gate_matrix=[]
    i=0
    
    #iterates over all gates that have to be applied to the respective qubits and appends the corresponding matrices in a list
    for gate in gates:     
        #print(gate)       
        gate_matrix.append(get_unit_matrix(num_qubits, gate))
        if gate.upper()=='CNOT':
            i+=2
        else:
            i+=1
                
        if i==num_qubits:
            break
    
    i=0
    #print("Gate matrix:",gate_matrix)
    
    #Calculates the final matrix to be applied to the circuit by taking the tensor product of all the matrices
    num_matrices=len(gate_matrix)
    if num_matrices==1:
        final_matrix=gate_matrix[0]
    elif num_matrices==2:
        final_matrix=np.kron(gate_matrix[0], gate_matrix[1])
    else:
        final_matrix=calc_tensor_product(gate_matrix, 0, num_matrices)
           
    
    
    final_q_state=np.zeros((2**num_qubits,1))
    final_q_state=np.dot(final_matrix, q_state)  #calculates the final quantum state after application of the gates/operators(matrices)
    
    return final_q_state
