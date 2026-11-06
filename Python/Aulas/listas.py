frutas = ["Maçã", "Banana", "Mamão", "Uva"]

numeros = [1, 3, 5, 10]

booleanos = [True, False, True]

dados = ["Vitor", 28, True, "Escravo branco"]

for dado in dados:
    print(f"dado {dado}")

    alunos = []

    alunos.append("Ariel")
    alunos.append("Rafa")
    alunos.append("guigay")

    print(f"alunos[0] {alunos[0]}")
    print(f"alunos[1] {alunos[1]}")
    print(f"alunos[1] {alunos[-1]}")

alunos[1] = "Anna"

print(alunos)

alunos.insert(1, "Gabriela")

print(alunos)

alunos.remove("Ariel")

print(alunos)

alunos.pop(1)

print(alunos)

tamanho_lista = len(alunos)

print(f"tamanho lista {tamanho_lista}")