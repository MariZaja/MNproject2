from math import sin

def create_matrix(N):
    result = []
    for i in range(N):
        r = [0] * N
        result.append(r)
    return result

def create_A_matrix(N, a1, a2, a3):
    A = []
    for i in range(N):
        if i == 0:
            l = la2times = la3times = 0
            ra2times = ra3times = 1
            r = N - 3
        elif i == 1:
            l = la3times = 0
            la2times = 1
            ra2times = ra3times = 1
            r = N - 4
        elif i == 2:
            l = 0
            la2times = la3times = ra2times = ra3times = 1
            r = N - 5
        else:
            l = i - 2
            la2times = la3times = ra2times = ra3times = 1
            r = N - 5 - l
        if i == N - 2:
            l = i - 2
            la2times = la3times = ra2times = 1
            ra3times = 0
            r = 0
        elif i == N - 1:
            l = i - 2
            la2times = la3times = 1
            ra2times = ra3times = 0
            r = 0
        a = [0] * l + [a3] * la3times + [a2] * la2times + [a1] + [a2] * ra2times + [a3] * ra3times + [0] * r
        A.append(a)
    return A

def create_b_vector(N):
    b = [sin(n * (8 + 1)) for n in range(N)]
    return b


def create_T_matrix(A, N):
    R = create_R_matrix(A, N)
    D = create_minus_reversed_D_matrix(A, N)
    T = multiply_matrices(D, R, N)
    #print_matrix(R, N, "Matrix R:")
    #print_matrix(D, N, "Matrix D:")
    return T

def create_R_matrix(A, N):
    R = create_matrix(N)
    for i in range(N):
        for j in range(N):
            if i != j:
                R[i][j] = A[i][j]
            else:
                R[i][i] = 0
    return R

def create_minus_reversed_D_matrix(A, N):
    D = create_matrix(N)
    for i in range(N):
        if A[i][i] != 0:
            D[i][i] = -(1 / A[i][i])
    return D

def create_reversed_D_matrix(A, N):
    D = create_matrix(N)
    for i in range(N):
        if A[i][i] != 0:
            D[i][i] = 1 / A[i][i]
    return D

def create_C_matrix(A, b, N):
    D = create_reversed_D_matrix(A, N)
    C = multiply_matrix_vector(D, b, N)
    return C

def multiply_matrices(A, B, N):
    result = create_matrix(N)
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
    return result

def multiply_matrix_vector(A, b, N):
    result = [0] * N
    for i in range(N):
        for j in range(N):
            result[i] += A[i][j] * b[j]
    return result

def add_matrices(A, B, N):
    result = create_matrix(N)
    for i in range(N):
        for j in range(N):
            result[i][j] += A[i][j] + B[i][j]
    return result

def add_vectors(a, b, N):
    result = [0] * N
    for i in range(N):
        result[i] += a[i] + b[i]
    return result

def subtract_vectors(a, b, N):
    result = [0] * N
    for i in range(N):
        result[i] += a[i] - b[i]
    return result

def print_matrix(A, N, name):
    print(name)
    print()
    for i in range(N):
        for j in range(N):
            if A[i][j]<10 and A[i][j]>=0:
                print(' ', end="")
            print(round(A[i][j], 3), end="\t")
        print()
    print()

def print_vector(a, N, name):
    print(name)
    print()
    for i in range(N):
        if a[i]<10 and a[i]>=0:
            print(' ', end="")
        print(round(a[i],3), end="\t")
    print("\n")