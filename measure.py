#Function to perform measurement
#This uses numpy.random() to perform weighted random selection
import numpy as np
from numpy import random

def measure(num_qubits, num, q_state, shots):
    q_state_prob=np.abs(q_state)**2  #Calculate modulus squared, contains the prob. of measuring each computational basis state.
    #print(q_state_prob)
    
   
    measure_str=list(range(num))  #Generates all possible basis states, but in decimal representation
    outcomes=random.choice(measure_str, shots, p=q_state_prob)  #gets the measurement results, but are not grouped acc. to index/basis state
    #print(outcomes,type(outcomes))
    counts={}  #dictionary to store the measurement results
    
    #Groups the measurement results acc. to the index/basis state.
    for outcome in outcomes:
        if counts.get(outcome)==None:
            counts[outcome]=1
        else:
            counts[outcome]+=1
    
    return counts
