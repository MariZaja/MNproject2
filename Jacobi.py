from math import sqrt
from matrices_and_vectors import *

"""
R = L + U
T = -D^-1 * R
C = D^-1 * b
x1 = Tx0 + C
"""

def Jacobi_method(A, b, N, epsilon):
    x0 = [1] * N
    x1 = [0] * N
    norm = 1
    T = create_T_matrix(A, N)
    #print_matrix(T, N, "Matrix T:")
    C = create_C_matrix(A, b, N)
    iter = 0
    #print_vector(C, N, "Vector C:")
    while(norm > epsilon):
        x1 = multiply_matrix_vector(T, x0, N)
        x1 = add_vectors(x1, C, N)
        norm = euclidean_norm(A, x1, b, N)
        #print_vector(x1, N, "Vector x1: ")
        for i in range(N):
            x0[i] = x1[i]
        print("Norm:", norm, "Epsilon:", epsilon)
        iter += 1
    return x0, iter

def second_element_counter(A, N, x, i):
    sum = 0
    for j in range(i, N):
        sum += A[i][j] * x[j]
    return sum

def euclidean_norm(A, x, b, N):
    residuumVector = multiply_matrix_vector(A, x, N)
    residuumVector = subtract_vectors(residuumVector, b, N)
    norm = 0
    for i in range(N):
        norm += residuumVector[i]*residuumVector[i]
    norm = sqrt(norm)
    return norm