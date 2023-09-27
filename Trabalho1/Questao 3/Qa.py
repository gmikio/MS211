import numpy as np

# Definindo a matriz A e o vetor b
A = np.array([[2.0, 2.0, 1.0, 1.0],
              [1.0, -1.0, 2.0, -2.0],
              [3.0, 2.0, 3.0, 2.0],
              [4.0, 3.0, 2.0, 1.0]])

b = np.array([7.0, 1.0, 4.0, 12.0])

# Aplicando o Método de Eliminação de Gauss com pivoteamento parcial
n = len(b)
x = np.zeros(n)

for i in range(n):
    pivot_row = np.argmax(np.abs(A[i:, i])) + i
    A[[i, pivot_row]] = A[[pivot_row, i]]
    b[[i, pivot_row]] = b[[pivot_row, i]]

    for j in range(i + 1, n):
        factor = A[j, i] / A[i, i]
        b[j] -= factor * b[i]
        A[j, i:] -= factor * A[i, i:]

# Resolvendo o sistema triangular superior
for i in range(n - 1, -1, -1):
    x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

# Exibindo a solução
print("Solucao do sistema:")
for i in range(n):
    print(f"x{i + 1} ~ {x[i]:.6f}")
