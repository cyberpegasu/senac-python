class Usuario():
    def __init__(self, nome, idade):
        self.nome = "Guilherme"
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

print("Execução normal do arquivo...")
usuario = Usuario("Guilherme", 27)
usuario2 = Usuario("Douglas", 32)



print(usuario.nome)
print(usuario.idade)


usuario.idade = 28

print(f"nova idade {usuario.idade}")