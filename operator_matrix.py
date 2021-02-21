#Function to return the matrix for the corresponding operator
import numpy as np
def get_unit_matrix(num_qubits, unit_operator):
    
    #Defining all the gates(operators) considered(I,X,Z,H,CNOT)
    
    #Identity operator:
    I=np.identity(2)
    
    #X gate:
    X=np.array([[0,1],[1,0]], dtype=complex)
     
    #Z gate:
    Z=np.array([[1,0],[0,-1]])
    
    #Y gate:
    Y=1j*np.dot(X,Z) 
    
    #H gate:
    H=(1/np.sqrt(2))*np.array([[1,1],[1,-1]])
    
    #CNOT gate(on consecutive qubits):
    CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
    
    
    #Returning the appropriate unitary matrix
    unit_operator=unit_operator.upper()
    
    if(unit_operator=='I'):
        return I
    if(unit_operator=='X'):
        return X
    elif(unit_operator=='Y'):
        return Y
    elif(unit_operator=='Z'):
        return Z
    elif(unit_operator=='H'):
        return H
    elif(unit_operator=="CNOT"):
        return CNOT
    else:
        return []