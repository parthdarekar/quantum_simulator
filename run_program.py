#Function to execute the quantum circuit/program
from initialise import ground_state
from error_check import error_check
from calc_final_state import apply_unit_operator
from measure import measure
def run_program(num_qubits, gates, shots, q_state):
    
    #Error checks
    flag=error_check(num_qubits, gates, shots, q_state)
    if flag==1:
        return []
    
    num=2**num_qubits #no of basis states/dimension of the Hilbert space
    counts={}
   
    
    #Executing the program
    #Initialising the quantum state
    if len(q_state)==0:  #if no input quantum state is given, the ground state is generated
        q_state=ground_state(num_qubits)
    print("Initial quantum state:", q_state)
    print("")
    
    #Applying the operation specified
    final_q_state=apply_unit_operator(num_qubits, q_state, gates)
    #print(final_q_state)
    
    #Performing measurement and displaying the results
    counts=measure(num_qubits, num, final_q_state, shots)
    #print(counts)
    
    print("Measurement results[index:counts]:")
    
    #This sorts the basis states in their standard order and displays them in their binary representation(standard)
    for key in sorted(counts):  
        print(str("{0:b}".format(key)).zfill(num_qubits), counts[key])

    print("")
    return final_q_state
    
    