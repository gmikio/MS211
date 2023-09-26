def f(x):
    return x**3 - 9*x + 3

def erro_relativo(x, x0):
    if x0 != 0:
        return abs(x - x0) / abs(x0)
    else:
        return abs(x)

def bissecao(a, b, E1, E2):
    iteration = 0

    while True:
        c = (a + b) / 2  # Ponto médio do intervalo
        fa = f(a)
        fb = f(b)
        fc = f(c)

        print(f"Iteracao {iteration}: x{iteration} = {a}, x{iteration+1} = {b}, x{iteration+2} = {c}")
        
        if abs(fc) <= E1 or (b - a) / 2 <= E2:
            print("Condicao de parada atingida.")
            break
        
        erro_rel = erro_relativo(c, (a + b) / 2)
        print(f"f(x{iteration}) = {fa}, f(x{iteration+1}) = {fb}, f(x{iteration+2}) = {fc}, Erro Relativo = {erro_rel}")

        if fa * fc < 0:
            b = c  # A raiz está no subintervalo [a, c]
        else:
            a = c  # A raiz está no subintervalo [c, b]

        iteration += 1

    return c

# Intervalo inicial
a = -2
b = 2

# Critérios de parada
E1 = E2 = 5e-4

# Aplicando o método da Bissecção
resultado = bissecao(a, b, E1, E2)

# Exibindo o resultado
print("Resultado aproximado:", resultado)
