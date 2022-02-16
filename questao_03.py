import itertools

senha = input(str("Digite a senha: "))
lista = list(senha)

x = list(itertools.combinations(lista, 2))
print(x)
print(len(x))
