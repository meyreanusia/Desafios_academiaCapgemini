''''Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços. 
A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.'''

def escada (n):
    for i in range(n +1):
        print("*" * i)

(escada(6))

