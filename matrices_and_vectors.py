from math import sin

def createAmatrix(N, a1, a2, a3):
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

def createBvector(N):
    b = [sin(n * (8 + 1)) for n in range(N)]
    return b