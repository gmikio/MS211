def f(x):
    return x**3 - 9*x + 3

def erro_relativo(x, x0):
    return abs(x - x0) / abs(x)

def secante(x0, x1, E1, E2):
    iteration = 0
    print(f"Iteracao {iteration}: x{iteration} = {x0},"+
          f"x{iteration+1} = {x1}")

    while True:
        fx0 = f(x0)
        fx1 = f(x1)
        
        erro_rel = erro_relativo(x1, x0)
        
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        
        print(f"Apos {iteration} Iteracoes, x{iteration}"+
              f"= {x0}, x{iteration+1} = {x1},"+
              f" f(x{iteration}) = {fx0}, f(x{iteration+1}) ="+
              f"{fx1}, Erro Relativo = {erro_rel}")
        
        if abs(fx1) <= E1:
            if erro_rel <= E2:
                print("Condicao de parada 1 e 2 atingidas"+
                      f"ao mesmo tempo.")
                break
            else:
                print("Condicao de parada 1 atingida.")
                break
        elif erro_rel <= E2:
            print("Condicao de parada 2 atingida.")
            break
        
        x0 = x1
        x1 = x2
        iteration += 1
    
    return x1

# Valores iniciais
x0 = 0
x1 = 1
E1 = E2 = 5e-4

# Aplicando o metodo da Secante
resultado = secante(x0, x1, E1, E2)

# Exibindo o resultado
print("Resultado aproximado:", resultado)
