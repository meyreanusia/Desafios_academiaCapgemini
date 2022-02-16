import itertools #o método combinations para fazer combinações.

senha = input(str("Digite a senha: "))
lista = list(senha)

x = list(itertools.combinations(lista, r=2)) #r - parametro para permutaçao com 2 elementos.
print(x)
print(len(x))
