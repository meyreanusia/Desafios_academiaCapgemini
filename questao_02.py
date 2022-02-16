while True:
    senha = input("Crie a sua senha: ")
    if len(senha) < 6:
        x = 6 - len(senha)
        print(f"Você digitou {len(senha)}\nÉ necessaário no mínimo 6 caracteres. \n")
    else:
        break

print("Senha validada!!")