print("===== CADASTRO =====")

email_cadastrado = input("Cadastre seu email: ")
senha_cadastrada = input("Cadastre sua senha: ")

print("\nCadastro concluído!")

print("\n===== ENTRAR =====")

email_login = input("Digite seu email: ")
senha_login = input("Digite sua senha: ")

if email_login == email_cadastrado and senha_login == senha_cadastrada:
    print("Login realizado com sucesso!")
else:
    print("Email ou senha incorretos!")

if email_login != email_cadastrado:
    print("Email incorreto!")
elif senha_login != senha_cadastrada:
    print("Senha incorreta!")
else:
    print("Login realizado com sucesso!")