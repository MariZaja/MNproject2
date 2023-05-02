def Jacobi_method(A, b, N):
    x = [1] * N
    xNew = [0]*N
    for i in range(N):
        firstElement = first_element_counter(A, x, i)
        secondElement = second_element_counter(A, N, x, i)
        xNew[i] = (b[i] - firstElement - secondElement)/A[i][i]


def first_element_counter(A, x, i):
    sum = 0
    for j in range(1, i):
        sum += A[i][j]*x[j]
    return sum

def second_element_counter(A, N, x, i):
    sum = 0
    for j in range(i+1, N+1):
        sum += A[i][j] * x[j]
    return sum