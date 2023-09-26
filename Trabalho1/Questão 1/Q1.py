# Funcao para calcular o Somatorio exato S
def somatorio_exato(n, x):
    return n * x

# Funcao para calcular o Somatorio parcela a parcela
def somatorio_parcial(n, x):
    S = 0
    for i in range(1, n+1):
        S += x
    return S

# Funcao para calcular o erro absoluto
def erro_absoluto(somatorio_exato, somatorio_parcial):
    return abs(somatorio_exato - somatorio_parcial)

# Funcao para calcular o erro relativo
def erro_relativo(exato, aproximado):
    return abs(exato - aproximado) / abs(exato)

# Valores dados
n = 30000
x1 = 0.5
x2 = 0.11

# Calculos para xi = 0.5
S_exato_x1 = somatorio_exato(n, x1)
S_parcial_x1 = somatorio_parcial(n, x1)
erro_abs_x1 = erro_absoluto(S_exato_x1, S_parcial_x1)
erro_rel_x1 = erro_relativo(S_exato_x1, S_parcial_x1)

# Calculos para xi = 0.11
S_exato_x2 = somatorio_exato(n, x2)
S_parcial_x2 = somatorio_parcial(n, x2)
erro_abs_x2 = erro_absoluto(S_exato_x2, S_parcial_x2)
erro_rel_x2 = erro_relativo(S_exato_x2, S_parcial_x2)

# Exibindo os resultados
print("Para xi = 0.5:")
print("Somatorio exato:", S_exato_x1)
print("Somatorio parcela a parcela:", S_parcial_x1)
print("Erro absoluto:", erro_abs_x1)
print("Erro relativo:", erro_rel_x1)

print("\nPara xi = 0.11:")
print("Somatorio exato:", S_exato_x2)
print("Somatorio parcela a parcela:", S_parcial_x2)
print("Erro absoluto:", erro_abs_x2)
print("Erro relativo:", erro_rel_x2)