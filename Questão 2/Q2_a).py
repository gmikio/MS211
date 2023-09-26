def f(x):
    return x**3 - 9*x + 3

def df(x):
    return 3*x**2 - 9

def erro_relativo(x, x0):
    return abs(x - x0) / abs(x)

def newton_raphson(x0, E1, E2):
    x = x0
    iteration = 0
    print(f"Iteracao {iteration}: x = {x}")

    while True:
        fx = f(x)
        dfx = df(x)
        erro_rel = erro_relativo(x, x0)
        
        x0 = x
        x = x - fx / dfx
        iteration += 1
        
        print(f"Apos {iteration} Iteracoes, x = {x}, f(x) ="+
              "{fx}, Erro Relativo = {erro_rel}")
        
        if abs(fx) <= E1:
            if erro_rel <= E2:
                print("Condicao de parada 1 e 2 atingidas ao" +
                      "mesmo tempo.")
                break
            else:
                print("Condicao de parada 1 atingida.")
                break
        elif erro_rel <= E2:
            print("Condicao de parada 2 atingida.")
            break
        
           
    return x

# Valores iniciais
x0 = 0.5
E1 = E2 = 1e-4

# Aplicando o metodo de Newton-Raphson
resultado = newton_raphson(x0, E1, E2)

# Exibindo o resultado
print("Resultado aproximado:", resultado)
