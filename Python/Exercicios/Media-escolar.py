nome = input("Qual o seu nome? ")

try:
    nota1 = float(input("Digite a primeira nota:"))
    nota2 = float(input("Digite a segunda nota:"))
    nota3 = float(input("Digite a terceira nota:"))
    media = (nota1 + nota2 + nota3) / 3
    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")

    if media >= 7:
        print("Aluno aprovado!")
    elif media >= 5:
        print("Aluno em recuperação!")
    else:
        print("Aluno reprovado!")

except Exception:
    print("O valor da nota não é válido!")
