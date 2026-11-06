# def saudacao():
#     print("Olá, mundo")

#     saudacao()

# def saudacao_com_nome(nome="Aluno"):
#     print(f"Olá, meu nome é {nome}")

# saudacao_com_nome("Douglas")
# saudacao_com_nome("Guilherme")
# saudacao_com_nome()

# def somar(a, b):
#     soma = a + b
#     return soma

# print(somar(5, 2))


def cadstrar_usuario(nome: str, idade: int = 18):
    print(f"Cadastrando nome {nome} {type(nome)}")
    print(f"Cadastrando idade {idade} {type(idade)}")

cadstrar_usuario("Guilherme", 27)
cadstrar_usuario("João")

cadstrar_usuario(nome="Douglas", idade=32)
cadstrar_usuario(idade=40, nome="Eloi")
# cadstrar_usuario(idade=40, "Marlene") dá erro
cadstrar_usuario("Marlene", idade=40)
cadstrar_usuario(10, "texto")