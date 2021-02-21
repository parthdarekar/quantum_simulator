#Function to calculate the tensor product of all the operator matrices

#Here the we have all the matrices to be applied to all the qubits as the input to the function. This is in the form of an array of matrices called matrices. 
#To calculate the tensor product to get the final matrix, we iterate over the array(using the length of the array as num_matrices and calculate the tensor product recursively.
from numpy import kron
def calc_tensor_product(matrices, i, num_matrices):
    if i==(num_matrices-2):
        final_matrix=kron(matrices[i], matrices[i+1])
        return final_matrix
    else:
        final_matrix=kron(matrices[i], calc_tensor_product(matrices, i+1, num_matrices))
        return final_matrix