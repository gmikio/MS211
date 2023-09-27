def f(x):
    return x**3 - 9*x + 3

def erro_abs(x, x0):
    return abs(x - x0)

def bissecao(a, b, E1, E2):
    iteration = 0

    while True:
        c = (a + b) / 2  # Ponto médio do intervalo
        fa = f(a)
        fb = f(b)
        fc = f(c)
        
        err_abs = erro_abs(a, b)

        print(f"Iteracao {iteration}: a{iteration} = {a}, b{iteration} = {b}, c{iteration} = {c}")
        print(f"f(a{iteration}) = {fa}, f(b{iteration}) = {fb}, f(c{iteration}) = {fc}, Erro Relativo = {err_abs}")

        
        if abs(fc) <= E1 and err_abs<= E2:
            print("\nCondicao de parada atingida.")

            break
        

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