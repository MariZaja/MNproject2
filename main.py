from Jacobi import *
import time

N = 991
a1 = 5 + 9
a2 = a3 = -1
A = create_A_matrix(N, a1, a2, a3)
b = create_b_vector(N)
#print_matrix(A, N, "Matrix A: ")
#print_vector(b, N, "Vector b: ")

epsilon = pow(10, -9)

start = time.time()
x, iter = Jacobi_method(A, b, N, epsilon)
end = time.time()
print_vector(x, N, "Vector x: ")
print("Iterations: ", iter)
print("Time: ", end - start, "s", sep="")

